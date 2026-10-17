//! check_toc: verify that every coordinate link in a phext's table of contents
//! resolves to a non-empty scroll.
//!
//! Usage: cargo run --quiet --bin check_toc -- [file.phext ...]
//! Defaults to incipit.phext. Exits 1 if any link dangles.
//!
//! A TOC entry is any line in the root scroll (1.1.1/1.1.1/1.1.1) shaped like
//!   * <library>/<collection>/<chapter>: <title>
//! Duplicate addresses are reported as warnings, not failures.
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

fn check(path: &str) -> Result<(usize, usize), String> {
    let text = std::fs::read_to_string(path).map_err(|e| format!("{path}: {e}"))?;
    let scrolls = phext::explode(&text);
    let root = scrolls
        .get(&phext::to_coordinate("1.1.1/1.1.1/1.1.1"))
        .cloned()
        .unwrap_or_default();

    let mut ok = 0;
    let mut dangling = Vec::new();
    let mut seen: HashMap<String, Vec<String>> = HashMap::new();

    for (i, line) in root.lines().enumerate() {
        let Some(rest) = line.trim().strip_prefix("* ") else { continue };
        let Some((addr, title)) = rest.split_once(':') else { continue };
        let addr = addr.trim();
        if !is_address(addr) {
            continue;
        }
        seen.entry(addr.to_string()).or_default().push(title.trim().to_string());
        let resolves = scrolls
            .get(&phext::to_coordinate(addr))
            .map_or(false, |t| !t.trim().is_empty());
        if resolves {
            ok += 1;
        } else {
            dangling.push(format!("  line {}: {} -> {}", i + 1, addr, title.trim()));
        }
    }

    println!("{path}: {} scrolls, {ok} TOC links resolve, {} dangling", scrolls.len(), dangling.len());
    for d in &dangling {
        println!("{d}");
    }
    let mut dups: Vec<_> = seen.iter().filter(|(_, v)| v.len() > 1).collect();
    dups.sort();
    for (addr, titles) in dups {
        println!("  warning: {addr} listed {} times ({})", titles.len(), titles.join(" | "));
    }
    Ok((ok, dangling.len()))
}

fn main() -> ExitCode {
    let mut files: Vec<String> = std::env::args().skip(1).collect();
    if files.is_empty() {
        files.push("incipit.phext".to_string());
    }
    let mut failed = false;
    for f in &files {
        match check(f) {
            Ok((_, 0)) => {}
            Ok(_) => failed = true,
            Err(e) => {
                eprintln!("{e}");
                failed = true;
            }
        }
    }
    if failed { ExitCode::FAILURE } else { ExitCode::SUCCESS }
}
