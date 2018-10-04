#include <stdio.h>

int main() {
	int n = 1083;

	long previous = 1;
	long current = 1;
	long next = 1;

	for (int i = 3; i <= n; ++i) {
		next = current + previous;
		previous = current;
		current = next;
	}
	printf("%d\n", next);
	return 0;
}
