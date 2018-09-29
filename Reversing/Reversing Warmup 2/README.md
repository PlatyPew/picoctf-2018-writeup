# Reversing Warmup 2
Points: 50

## Category
Reversing

## Question
>Can you decode the following string `dGg0dF93NHNfczFtcEwz` from base64 format to ASCII? 

### Hint
>Submit your answer in our competition's flag format. For example, if you answer was 'hello', you would submit 'picoCTF{hello}' as the flag.

## Solution
```python
>>> print 'dGg0dF93NHNfczFtcEwz'.decode('base64')
th4t_w4s_s1mpL3
```

### Flag
`picoCTF{th4t_w4s_s1mpL3}`
