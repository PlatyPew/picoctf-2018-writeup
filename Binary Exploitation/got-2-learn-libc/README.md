# got-2-learn-libc
Points: 250

## Category
Binary Exploitation

## Question
>This program gives you the address of some system calls. Can you get a shell? You can find the [program](files/vuln) in /problems/got-2-learn-libc_3_6e9881e9ff61c814aafaf92921e88e33 on the shell server. [Source](files/vuln.c). 

### Hint
>try returning to systems calls to leak information
>
>don't forget you can always return back to main().

## Solution
Working solution [solve.py](solution/solve.py)

Thanks to [@LFlare](https://github.com/LFlare) for making the code compatible with ASLR

### Flag
`picoCTF{syc4al1s_4rE_uS3fUl_6319ec91}`
