# Forensics Warmup 2
Points: 50

## Category
Forensics

## Question
>Hmm for some reason I can't open this [PNG](files/flag.png)? Any ideas?

### Hint
>How do operating systems know what kind of file it is? (It's not just the ending!
>
>Make sure to submit the flag as picoCTF{XXXXX}

## Solution
Do `file flag.png` to find the actual filetype.

However, most image viewer software should be able to open the _.png_ file without any problem.

If this doesn't work change the file extension to _.jpg_

### Flag
`picoCTF{extensions_are_a_lie}`
