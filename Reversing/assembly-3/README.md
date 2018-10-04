# assembly-3
Points: 400

## Category
Reversing

## Question
>What does asm3(0xbda42100,0xb98dd6a5,0xecded223) return? Submit the flag as a hexadecimal value (starting with '0x'). NOTE: Your submission for this question will NOT be in the normal flag format. [Source](files/end_asm_rev.S) located in the directory at /problems/assembly-3_4_05ce5be4420bf9bd2ff37caf87e32898. 

### Hint
>more(?) [registers](https://wiki.skullsecurity.org/index.php?title=Registers)

## Solution
Compile the asm together with another function that calls the _asm3_ function and prints it out

```asm
/ (fcn) loc.asm3 31
|   loc.asm3 (int arg_9h, int arg_ch, int arg_dh, int arg_10h);
|           ; arg int arg_9h @ ebp+0x9
|           ; arg int arg_ch @ ebp+0xc
|           ; arg int arg_dh @ ebp+0xd
|           ; arg int arg_10h @ ebp+0x10
|           ; CALL XREF from sym.main (0x11d5)
|           0x000011ff      55             push ebp
|           0x00001200      89e5           mov ebp, esp
|           0x00001202      b8bc000000     mov eax, 0xbc
|           0x00001207      30c0           xor al, al
|           0x00001209      8a6509         mov ah, byte [arg_9h]       ; [0x9:1]=0
|           0x0000120c      66c1e010       shl ax, 0x10
|           0x00001210      2a450c         sub al, byte [arg_ch]
|           0x00001213      02650d         add ah, byte [arg_dh]
|           0x00001216      66334510       xor ax, word [arg_10h]
|           0x0000121a      89ec           mov esp, ebp
|           0x0000121c      5d             pop ebp
\           0x0000121d      c3             ret

```

```
$ make all
gcc -m32 -c end.s -o end.o
gcc -m32 -c solve.c -o solve.o
solve.c: In function ‘main’:
solve.c:4:28: warning: implicit declaration of function ‘asm3’ [-Wimplicit-function-declaration]
     printf("Flag: 0x%x\n", asm3(0xbda42100, 0xb98dd6a5, 0xecded223));
                            ^~~~
gcc -m32 -o a.out solve.o end.o
./a.out
Flag: 0x478
```

### Flag
`0x478`
