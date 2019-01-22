# be-quick-or-be-dead-2
Points: 275

## Category
Reversing

## Question
>As you enjoy this [music](https://www.youtube.com/watch?v=CTt1vk9nM9c) even more, another executable [be-quick-or-be-dead-2](files/be-quick-or-be-dead-2) shows up. Can you run this fast enough too? You can also find the executable in /problems/be-quick-or-be-dead-2_4_aeb39eed03c948aec1bf7fa3d03dad0c. 

### Hint
>Can you call stuff without executing the entire program?
>
>What will the key finally be?

## Solution
Patch the binary to remove the _set_timer_ function using NOPs.

```asm
[0x0040085f]> wx 9090909090 @ 0x0040087d
[0x0040085f]> pdf
            ;-- main:
/ (fcn) sym.main 62
|   sym.main (int argc, char **argv, char **envp);
|           ; var int local_10h @ rbp-0x10
|           ; var int local_4h @ rbp-0x4
|           ; arg int argc @ rdi
|           ; arg char **argv @ rsi
|           ; DATA XREF from entry0 (0x4005bd)
|           0x0040085f      55             push rbp
|           0x00400860      4889e5         mov rbp, rsp
|           0x00400863      4883ec10       sub rsp, 0x10
|           0x00400867      897dfc         mov dword [local_4h], edi   ; argc
|           0x0040086a      488975f0       mov qword [local_10h], rsi  ; argv
|           0x0040086e      b800000000     mov eax, 0
|           0x00400873      e8a9ffffff     call sym.header
|           0x00400878      b800000000     mov eax, 0
|           0x0040087d      90             nop
|           0x0040087e      90             nop
|           0x0040087f      90             nop
|           0x00400880      90             nop
|           0x00400881      90             nop
|           0x00400882      b800000000     mov eax, 0
|           0x00400887      e842ffffff     call sym.get_key
|           0x0040088c      b800000000     mov eax, 0
|           0x00400891      e863ffffff     call sym.print_flag
|           0x00400896      b800000000     mov eax, 0
|           0x0040089b      c9             leave
\           0x0040089c      c3             ret
```

Studying the binary, it seems that it's doing the Fibonacci sequence recursively, that's why it takes so long.

We can use Python to calculate the result iteratively. This will make the process a lot faster.

Code stolen from: https://gist.github.com/sgammon/4185115

```python
n = 1083

def fib(n):
    i = 0
    nextterm = 1
    present = 1
    previous = 0

    while i < n:
        nextterm = present + previous
        present = previous
        previous = nextterm
        i = i + 1
    return nextterm

result = fib(n)
print(result & (2 ** 64 - 1))
```

We need to convert the huge number into a 64-bit number so that our program can process it. This is done by doing `result & (2 ** 64 - 1)`. We get `13519797236961659458`

Now all we have to do is to patch the binary, and set `rax = 13519797236961659458`. We will need 10 bytes to create this instruction. We can ovewrite from addresses `0x004007dc` to `0x004007e5`.

```asm
/ (fcn) sym.get_key 43
|   sym.get_key ();
|           ...
|           ...
|           0x004007d7      e854fdffff     call sym.imp.puts           ; int puts(const char *s)
|           0x004007dc      b800000000     mov eax, 0
|           0x004007e1      e865ffffff     call sym.calculate_key
|           0x004007e6      8905d4082000   mov dword [obj.key], eax    ; obj.__TMC_END ; [0x6010c0:4]=0
|           0x004007ec      bfcb094000     mov edi, str.Done_calculating_key ; 0x4009cb ; "Done calculating key" ; const char *s
|           0x004007f1      e83afdffff     call sym.imp.puts           ; int puts(const char *s)
|           ...
\           ...
```

Now all we have left to do is to patch it and run it.

```asm
[0x004007ce]> wa mov rax, 13519797236961659458 @ 0x004007dc
Written 10 byte(s) (mov rax, 13519797236961659458) = wx 48b8424a68c0f4f79fbb
[0x004007ce]> pdf
/ (fcn) sym.get_key 43
|   sym.get_key ();
|           ; CALL XREF from sym.main (0x400887)
|           0x004007ce      55             push rbp
|           0x004007cf      4889e5         mov rbp, rsp
|           0x004007d2      bfb8094000     mov edi, str.Calculating_key... ; 0x4009b8 ; "Calculating key..." ; const char *s
|           0x004007d7      e854fdffff     call sym.imp.puts           ; int puts(const char *s)
|           0x004007dc      48b8424a68c0.  movabs rax, 0xbb9ff7f4c0684a42
|           0x004007e6      8905d4082000   mov dword [obj.key], eax    ; obj.__TMC_END ; [0x6010c0:4]=0
|           0x004007ec      bfcb094000     mov edi, str.Done_calculating_key ; 0x4009cb ; "Done calculating key" ; const char *s
|           0x004007f1      e83afdffff     call sym.imp.puts           ; int puts(const char *s)
|           0x004007f6      90             nop
|           0x004007f7      5d             pop rbp
\           0x004007f8      c3             ret
```

```
$ ./be-quick-or-be-dead-2_patched
Be Quick Or Be Dead 2
=====================

Calculating key...
Done calculating key
Printing flag:
picoCTF{the_fibonacci_sequence_can_be_done_fast_88f31f48}
```

And we get the flag.

### Flag
`picoCTF{the_fibonacci_sequence_can_be_done_fast_88f31f48}`
