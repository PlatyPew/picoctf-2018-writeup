# learn gdb
Points: 300

## Category
General Skills

## Question
>Using a debugging tool will be extremely useful on your missions. Can you run this [program](files/run) in gdb and find the flag? You can find the file in /problems/learn-gdb_0_716957192e537ac769f0975c74b34194 on the shell server. 

### Hint
>Try setting breakpoints in gdb
>
>Try and find a point in the program after the flag has been read into memory to break on
>
>Where is the flag being written in memory?

## Solution
Do `cat file | grep picoCTF` to filter out the flag.

### Flag
`picoCTF{grep_and_you_will_find_cdf2e7c2}`
