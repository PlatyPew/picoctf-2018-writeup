# net cat
Points: 75

## Category
General Skills

## Question
>Using netcat (nc) will be a necessity throughout your adventure. Can you connect to `2018shell1.picoctf.com` at port `49387` to get the flag? 

### Hint
nc [tutorial](https://linux.die.net/man/1/nc)

## Solution
_Netcat_ allows users to read and write data over network connections.

Do `nc 2018shell1.picoctf.com 49387` to connect to the remote service and get the flag.

### Flag
`picoCTF{NEtcat_iS_a_NEcESSiTy_8b6a1fbc}`
