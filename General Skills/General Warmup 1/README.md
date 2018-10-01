# General Warmup 1
Points: 50 

## Category
General Skills

## Question
>If I told you your grade was 0x41 in hexadecimal, what would it be in ASCII?

### Hint
>Submit your answer in our competition's flag format. For example, if you answer was 'hello', you would submit 'picoCTF{hello}' as the flag.

## Solution
We can use Python to get the ASCII value of _0x41_.

```python
>>> chr(0x41)
'A'
```

### Flag
`picoCTF{A}`
