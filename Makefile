compress: compress.o
	g++ compress.o -o compress
compress.o: compress.cpp
	g++ -c compress.cpp
