// C program to generate random numbers 
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
	if (argc < 2) {
		return -1;
	}
	srand(atoi(argv[1])); 
	for (int i = 0; i < 8; i++) {
		long k = (rand() % 36) + 1;
		if (i % 2 == 0){
			printf("%ld ", k);
		}
	}
	puts("");
	return 0; 
} 
