# what base is this?
Points: 200

## Category
General Skills

## Question
>To be successful on your mission, you must be able read data represented in different ways, such as hexadecimal or binary. Can you get the flag from this program to prove you are ready? Connect with `nc 2018shell1.picoctf.com 1225`. 

### Hint
>I hear python is a good means (among many) to convert things.
>
>It might help to have multiple windows open

## Solution
Convert to ASCII for the respective bases. Python or online tools can be used to help convert.

1. Convert from binary
2. Convert from hex
3. Convert from octal

Working solution [solve.py](solution/solve.py).

### Flag
`picoCTF{delusions_about_finding_values_451a9a74}`
