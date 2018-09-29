# assembly-0
Points: 150

## Category
Reversing

## Question
>What does asm0(0xc9,0xb0) return? Submit the flag as a hexadecimal value (starting with '0x'). NOTE: Your submission for this question will NOT be in the normal flag format. [Source](files/intro_asm_rev.S) located in the directory at /problems/assembly-0_4_0f197369bfc00a9211504cf65ac31994. 

### Hint
>basical assembly [tutorial](https://www.tutorialspoint.com/assembly_programming/assembly_basic_syntax.htm)
>
>assembly [registers](https://www.tutorialspoint.com/assembly_programming/assembly_registers.htm)

## Solution
In assembly, the return value is always _eax_

```asm
asm0:
	push	ebp
	mov	ebp,esp
	mov	eax,DWORD PTR [ebp+0x8]
	mov	ebx,DWORD PTR [ebp+0xc]
	mov	eax,ebx
	mov	esp,ebp
	pop	ebp	
	ret
```

_eax_ has value _0xc9_ and _ebx_ has value _0xb0_. As the value of _eax_ is replaced with _ebx_ when `mov eax,ebx` is executed, the returned value is _0xb0_.

### Flag
`0xb0`
