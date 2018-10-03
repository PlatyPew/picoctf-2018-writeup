# assembly-2
Points: 250

## Category
Reversing

## Question
>What does asm2(0x7,0x28) return? Submit the flag as a hexadecimal value (starting with '0x'). NOTE: Your submission for this question will NOT be in the normal flag format. [Source](files/loop_asm_rev.S) located in the directory at /problems/assembly-2_4_f8bfecf223768f4cac035751390ea590. 

### Hint
>assembly [conditions](https://www.tutorialspoint.com/assembly_programming/assembly_conditions.htm)

## Solution
Compile the asm together with another function that calls the _asm2_ function and prints it out

```asm
[0x000011f4]> pdf
/ (fcn) loc.asm2 44
|   loc.asm2 (int arg_8h, int arg_ch);
|           ; var int local_8h @ ebp-0x8
|           ; var int local_4h @ ebp-0x4
|           ; arg int arg_8h @ ebp+0x8
|           ; arg int arg_ch @ ebp+0xc
|           ; CALL XREF from sym.main (0x11ca)
|           0x000011f4      55             push ebp
|           0x000011f5      89e5           mov ebp, esp
|           0x000011f7      83ec10         sub esp, 0x10
|           0x000011fa      8b450c         mov eax, dword [arg_ch]     ; [0xc:4]=0
|           0x000011fd      8945fc         mov dword [local_4h], eax
|           0x00001200      8b4508         mov eax, dword [arg_8h]     ; [0x8:4]=0
|           0x00001203      8945f8         mov dword [local_8h], eax
|       ,=< 0x00001206      eb08           jmp loc.part_b
|       |   ;-- part_a:
|      .--> 0x00001208      8345fc01       add dword [local_4h], 1
|      :|   0x0000120c      83450876       add dword [arg_8h], 0x76    ; 'v'
|      :|   ;-- part_b:
|      :|   ; CODE XREF from loc.asm2 (0x1206)
|      :`-> 0x00001210      817d08dea100.  cmp dword [arg_8h], 0xa1de  ; [0xa1de:4]=-1
|      `==< 0x00001217      7eef           jle loc.part_a
|           0x00001219      8b45fc         mov eax, dword [local_4h]
|           0x0000121c      89ec           mov esp, ebp
|           0x0000121e      5d             pop ebp
\           0x0000121f      c3             ret
```

```
$ make all
gcc -m32 -c loop.s -o loop.o
gcc -m32 -c solve.c -o solve.o
solve.c: In function ‘main’:
solve.c:4:28: warning: implicit declaration of function ‘asm2’ [-Wimplicit-function-declaration]
     printf("Flag: 0x%x\n", asm2(0x7, 0x28));
                            ^~~~
gcc -m32 -o a.out solve.o loop.o
./a.out
Flag: 0x188
```

Working solution [solve.sh](solution/solve.sh)

Thanks to [@LFlare](https://github.com/LFlare) for basically solving this.

### Flag
`0x188`
