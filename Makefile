compress: compress.o
	g++ compress.o -o compress
compress.o: compress.cpp
	g++ -std=c++20 -c compress.cpp
