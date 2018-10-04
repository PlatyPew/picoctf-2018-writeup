all:
	nasm -f elf32 comp.nasm
	gcc -m32 comp.o
	./a.out
clean:
	rm a.out comp.o
