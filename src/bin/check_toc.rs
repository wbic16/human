//! check_toc: verify that every coordinate link in a phext's table of contents
//! resolves to a non-empty scroll.
//!
//! Usage: cargo run --quiet --bin check_toc -- [file.phext ...]
//! Defaults to incipit.phext. Exits 1 if any link dangles.
//!
//! The TOC is the root scroll (1.1.1/1.1.1/1.1.1). A TOC entry is any line
//! shaped like
//!   * <library>/<collection>/<chapter>: <title>
//! (the leading "* " is optional). Any other non-blank line starts a new
//! section, named by that line. The same address may appear in several
//! sections on purpose; listing it twice within one section is reported
//! as a warning, not a failure.
//!
//! Oracle: libphext. Born from the Counterexample Orchard (1.1.1/2.1.1/1.1.2).

use libphext::phext;
use std::collections::HashMap;
use std::process::ExitCode;

fn is_address(s: &str) -> bool {
    let parts: Vec<&str> = s.split('/').collect();
    parts.len() == 3
        && parts.iter().all(|p| {
            let n: Vec<&str> = p.split('.').collect();
            n.len() == 3 && n.iter().all(|x| !x.is_empty() && x.chars().all(|c| c.is_ascii_digit()))
        })
}

/// Parse a TOC entry line into (address, title), if it is one.
fn parse_entry(line: &str) -> Option<(&str, &str)> {
    let rest = line.trim();
    let rest = rest.strip_prefix("* ").unwrap_or(rest);
    let (addr, title) = rest.split_once(':')?;
    let addr = addr.trim();
    is_address(addr).then_some((addr, title.trim()))
}

fn check(path: &str) -> Result<usize, String> {
    let text = std::fs::read_to_string(path).map_err(|e| format!("{path}: {e}"))?;
    let scrolls = phext::explode(&text);
    let root = scrolls
        .get(&phext::to_coordinate("1.1.1/1.1.1/1.1.1"))
        .cloned()
        .unwrap_or_default();

    let mut ok = 0;
    let mut dangling = Vec::new();
    let mut warnings = Vec::new();
    let mut section = String::from("(top)");
    let mut seen: HashMap<String, usize> = HashMap::new(); // address -> first line, within the current section

    for (i, line) in root.lines().enumerate() {
        let line_no = i + 1;
        if line.trim().is_empty() {
            continue;
        }
        let Some((addr, title)) = parse_entry(line) else {
            section = line.trim().to_string();
            seen.clear();
            continue;
        };
        if let Some(first) = seen.get(addr) {
            warnings.push(format!(
                "  warning: line {line_no}: {addr} ({title}) already listed at line {first} in section \"{section}\""
            ));
        } else {
            seen.insert(addr.to_string(), line_no);
        }
        let resolves = scrolls
            .get(&phext::to_coordinate(addr))
            .map_or(false, |t| !t.trim().is_empty());
        if resolves {
            ok += 1;
        } else {
            dangling.push(format!("  line {line_no}: {addr} -> {title} (section \"{section}\")"));
        }
    }

    println!("{path}: {} scrolls, {ok} TOC links resolve, {} dangling", scrolls.len(), dangling.len());
    for d in &dangling {
        println!("{d}");
    }
    for w in &warnings {
        println!("{w}");
    }
    Ok(dangling.len())
}

fn main() -> ExitCode {
    let mut files: Vec<String> = std::env::args().skip(1).collect();
    if files.is_empty() {
        files.push("incipit.phext".to_string());
    }
    let mut failed = false;
    for f in &files {
        match check(f) {
            Ok(0) => {}
            Ok(_) => failed = true,
            Err(e) => {
                eprintln!("{e}");
                failed = true;
            }
        }
    }
    if failed { ExitCode::FAILURE } else { ExitCode::SUCCESS }
}
