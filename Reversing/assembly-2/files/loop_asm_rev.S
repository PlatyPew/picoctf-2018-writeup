.intel_syntax noprefix
.bits 32
	
.global asm2

asm2:
	push   	ebp
	mov    	ebp,esp
	sub    	esp,0x10
	mov    	eax,DWORD PTR [ebp+0xc]
	mov 	DWORD PTR [ebp-0x4],eax
	mov    	eax,DWORD PTR [ebp+0x8]
	mov	DWORD PTR [ebp-0x8],eax
	jmp    	part_b
part_a:	
	add    	DWORD PTR [ebp-0x4],0x1
	add	DWORD PTR [ebp+0x8],0x76
part_b:	
	cmp    	DWORD PTR [ebp+0x8],0xa1de
	jle    	part_a
	mov    	eax,DWORD PTR [ebp-0x4]
	mov	esp,ebp
	pop	ebp
	ret
