.intel_syntax noprefix
.bits 32
	
.global asm3

asm3:
	push   	ebp
	mov    	ebp,esp
	mov	eax,0xbc
	xor	al,al
	mov	ah,BYTE PTR [ebp+0x9]
	sal	ax,0x10
	sub	al,BYTE PTR [ebp+0xc]
	add	ah,BYTE PTR [ebp+0xd]
	xor	ax,WORD PTR [ebp+0x10]
	mov	esp, ebp
	pop	ebp
	ret
