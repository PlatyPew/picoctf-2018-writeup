# in out error
Points: 275

## Category
General Skills

## Question
>Can you utlize stdin, stdout, and stderr to get the flag from this [program](files/)? You can also find it in /problems/in-out-error_2_c33e2a987fbd0f75e78481b14bfd15f4 on the shell server 

### Hint
>Maybe you can split the stdout and stderr output?

## Solution
The flag will be printed as stderr. Just pipe stdout to null and get the flag.

```
$ ./in-out-error 1> /dev/null
Please may I have the flag?
picoCTF{p1p1ng_1S_4_7h1ng_b6f5a788}picoCTF{p1p1ng_1S_4_7h1ng_b6f5a788}picoCTF{p1p1ng_1S_4_7h1ng_b6f5a788}picoCTF{p1p1ng_1S_4_7h1ng_b6f5a788}picoCTF{p1p1ng_1S_4_7h1ng_b6f5a788}picoCTF{p1p1ng_1S_4_7h1ng_b6f5a788}picoCTF{p1p1ng_1S_4_7h1ng_b6f5a788}picoCTF{p1p1ng_1S_4_7h1ng_b6f5a788}picoCTF{p1p1ng_1S_4_7h1ng_b6f5a788}picoCTF{p1p1ng_1S_4_7h1ng_b6f5a788}picoCTF{p1p1ng_1S_4_7h1ng_b6f5a788}picoCTF{p1p1ng_1S_4_7h1ng_b6f5a788}picoCTF{p1p1ng_1S_4_7h1ng_b6f5a788}picoCTF{p1p1ng_1S_4_7h1ng_b6f5a788}picoCTF{p1p1ng_1S_4_7h1ng_b6f5a788}picoCTF{p1p1ng_1S_4_7h1ng_b6f5a788}picoCTF{p1p1ng_1S_4_7h1ng_b6f5a788}picoCTF{p1p1ng_1S_4_7h1ng_b6f5a788}picoCTF{p1p1ng_1S_4_7h1ng_b6f5a788}picoCTF{p1p1ng_1S_4_7h1ng_b6f5a788}picoCTF{p1p1ng_1S_4_7h1ng_b6f5a788}picoCTF{p1p1ng_1S_4_7h1ng_b6f5a788}picoCTF{p1p1ng_1S_4_7h1ng_b6f5a788}picoCTF{p1p1ng_1S_4_7h1ng_b6f5a788}picoCTF{p1p1ng_1S_4_7h1ng_b6f5a788}picoCTF{p1p1ng_1S_4_7h1ng_b6f5a788}picoCTF{p1p1ng_1S_4_7h1ng_b6f5a788}picoCTF{p1p1ng_1S_4_7h1ng_b6f5a788}picoCTF{p1p1ng_1S_4_7h1ng_b6f5a788}picoCTF{p1p1ng_1S_4_7h1ng_b6f5a788}picoCTF{p1p1ng_1S_4_7h1ng_b6f5a788}picoCTF{p1p1ng_1S_4_7h1ng_b6f5a788}picoCTF{p1p1ng_1S_4_7h1ng_b6f5a788}picoCTF{p1p1ng_1S_4_7h1ng_b6f5a788}picoCTF{p1p1ng_1S_4_7h1ng_b6f5a788}picoCTF{p1p1ng_1S_4_7h1ng_b6f5a788}picoCTF{p1p1ng_1S_4_7h1ng_b6f5a788}picoCTF{p1p1ng_1S_4_7h1ng_b6f5a788}picoCTF{p1p1ng_1S_4_7h1ng_b6f5a788}picoCTF{p1p1ng_1S_4_7h1ng_b6f5a788}picoCTF{p1p1ng_1S_4_7h1ng_b6f5a788}picoCTF{p1p1ng_1S_4_7h1ng_b6f5a788}picoCTF{p1p1ng_1S_4_7h1ng_b6f5a788}picoCTF{p1p1ng_1S_4_7h1ng_b6f5a788}picoCTF{p1p1ng_1S_4_7h1ng_b6f5a788}picoCTF{p1p1ng_1S_4_7h1ng_b6f5a788}picoCTF{p1p1ng_1S_4_7h1ng_b6f5a788}picoCTF{p1p1ng_1S_4_7h1ng_b6f5a788}picoCTF{p1p1ng_1S_4_7h1ng_b6f5a788}picoCTF{p1p1ng_1S_4_7h1ng_b6f5a788}picoCTF{p1p1ng_1S_4_7h1ng_b6f5a788}picoCTF{p1p1ng_1S_4_7h1ng_b6f5a788}picoCTF{p1p1ng_1S_4_7h1ng_b6f5a788}picoCTF{p1p
```

### Flag
`picoCTF{p1p1ng_1S_4_7h1ng_b6f5a788}`
