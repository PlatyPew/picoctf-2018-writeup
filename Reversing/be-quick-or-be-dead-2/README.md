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

First, we patch the binary so that it does not use such a huge number.

```asm
[0x0040074b]> wa mov edi, 5 @ 0x0040074f
[0x0040074b]> pdf
/ (fcn) sym.calculate_key 16
|   sym.calculate_key ();
|           ; CALL XREF from sym.get_key (0x4007e1)
|           0x0040074b      55             push rbp
|           0x0040074c      4889e5         mov rbp, rsp
|           0x0040074f      bf05000000     mov edi, 5
|           0x00400754      e8adffffff     call sym.fib
|           0x00400759      5d             pop rbp
\           0x0040075a      c3             ret
```

Instead of doing the fibonacci sequence recurvsively, we can do it iteratively in c.

```c
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
```

We can see that there's an integer overflow because it's negative. But it's just what we need to feed into our register.

```
$ gcc calculate.c 
$ ./a.out 
-1066907070
```

Set a break point after the _fib_ function and edit _rax_ to the value we calculated using the C program (-1066907070)

```asm
[0x0040074b]> db 0x00400759
[0x0040074b]> dc
Be Quick Or Be Dead 2
=====================

Calculating key...
hit breakpoint at: 400759
[0x0040074b]> dr rax = -1066907070
0x00000005 ->0xffffffffc0684a42
[0x0040074b]> dc
Done calculating key
Printing flag:
picoCTF{the_fibonacci_sequence_can_be_done_fast_88f31f48}
[0x7f1d298a3916]>
```

And we get the flag.

### Flag
`picoCTF{the_fibonacci_sequence_can_be_done_fast_88f31f48}`
