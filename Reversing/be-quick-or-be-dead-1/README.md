# be-quick-or-be-dead-1
Points: 200

## Category
Reversing

## Question
>You [find](https://www.youtube.com/watch?v=CTt1vk9nM9c) this when searching for some music, which leads you to [be-quick-or-be-dead-1](files/be-quick-or-be-dead-1). Can you run it fast enough? You can also find the executable in /problems/be-quick-or-be-dead-1_3_aeb48854203a88fb1da963f41ae06a1c. 

### Hint
>What will the key finally be?

## Solution
Overwrite the _set_timer_ function with nops by patching the program.

```asm
[0x00400849]> pdf
|           ;-- main:
/ (fcn) sym.main 62
|   sym.main (int arg1, int arg2);
|           ; var int local_10h @ rbp-0x10
|           ; var int local_4h @ rbp-0x4
|           ; DATA XREF from entry0 (0x4005bd)
|           0x00400827      55             push rbp
|           0x00400828      4889e5         mov rbp, rsp
|           0x0040082b      4883ec10       sub rsp, 0x10
|           0x0040082f      897dfc         mov dword [local_4h], edi   ; arg1
|           0x00400832      488975f0       mov qword [local_10h], rsi  ; arg2
|           0x00400836      b800000000     mov eax, 0
|           0x0040083b      e8a9ffffff     call sym.header
|           0x00400840      b800000000     mov eax, 0
|           0x00400845      90             nop
|           0x00400846      90             nop
|           0x00400847      90             nop
|           0x00400848      90             nop
|           0x00400849      90             nop
|           0x0040084a      b800000000     mov eax, 0
|           0x0040084f      e842ffffff     call sym.get_key
|           0x00400854      b800000000     mov eax, 0
|           0x00400859      e863ffffff     call sym.print_flag
|           0x0040085e      b800000000     mov eax, 0
|           0x00400863      c9             leave
\           0x00400864      c3             ret
[0x00400849]> exit
```

Save and run the program to get the flag.

Patched binary [be-quick-or-be-dead-1_patched](solution/be-quick-or-be-dead-1_patched).

### Flag
`picoCTF{why_bother_doing_unnecessary_computation_27f28e71}`
