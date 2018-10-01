# grep 2
Points: 125

## Category
General Skills

## Question
>This one is a little bit harder. Can you find the flag in /problems/grep-2_3_826f886f547acb8a9c3fccb030e8168d/files on the shell server? Remember, grep is your friend. 

### Hint
>grep [tutorial](https://ryanstutorials.net/linuxtutorial/grep.php)

## Solution
This time, there are multiple folders, each containing it's own set of folders and files.

We can _grep_ recursively by using `-r` to get the flag.

Do `grep -r picoCTF` to filter out the flag.

### Flag
`picoCTF{grep_r_and_you_will_find_556620f7}`
