compress: compress.o
	g++ compress.o -o compress
compress.o: compress.cpp
	g++ -std=c++20 -c compress.cpp

.PHONY: check-toc

# Verify every TOC link in incipit.phext resolves (see 1.1.1/2.1.1/1.1.2)
check-toc:
	cargo run --quiet --bin check_toc -- incipit.phext
