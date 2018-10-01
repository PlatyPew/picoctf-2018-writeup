# General Warmup 2
Points: 50

## Category
General Skills

## Question
>Can you convert the number 27 (base 10) to binary (base 2)? 

### Hint
>Submit your answer in our competition's flag format. For example, if you answer was '11111', you would submit 'picoCTF{11111}' as the flag.

## Solution
We can use Python to convert an integer to a binary number.

```python
>>> bin(27)[2:]
'11011'
```

### Flag
`picoCTF{11011}`
