all:
	gcc -m32 -c loop.s -o loop.o
	gcc -m32 -c solve.c -o solve.o
	gcc -m32 -o a.out solve.o loop.o
	./a.out
clean:
	rm a.out *.o
