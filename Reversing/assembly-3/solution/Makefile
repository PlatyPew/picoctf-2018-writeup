all:
	gcc -m32 -c end.s -o end.o
	gcc -m32 -c solve.c -o solve.o
	gcc -m32 -o a.out solve.o end.o
	./a.out
clean:
	rm a.out *.o
