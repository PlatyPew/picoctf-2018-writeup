# strings
Points: 100

## Category
General Skills

## Question
>Can you find the flag in this [file]() without actually running it? You can also find the file in /problems/strings_2_b7404a3aee308619cb2ba79677989960 on the shell server. 

### Hint
>[strings](https://linux.die.net/man/1/strings)

## Solution
We are given a file with non-printable characters.

The _strings_ command prints all human-readable characters.

We can use the _strings_ command and _grep_ the flag.

Do `strings strings | grep pico` to get flag.

### Flag
`picoCTF{sTrIngS_sAVeS_Time_3f712a28}`
