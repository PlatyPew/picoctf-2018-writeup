# pipe
Points: 110

## Category
General Skills

## Question
>During your adventure, you will likely encounter a situation where you need to process data that you receive over the network rather than through a file. Can you find a way to save the output from this program and search for the flag? Connect with `2018shell1.picoctf.com 48696`. 

### Hint
>Remember the flag format is picoCTF{XXXX}
>
>Ever heard of a pipe? No not that kind of pipe... This [kind](http://www.linfo.org/pipes.html)

## Solution
The _pipe_ or the `|` passes standard output into standard input.

Connect to the service and pipe output to _grep_

Do `nc 2018shell1.picoctf.com 48696 | grep pico` to get flag.

### Flag
`picoCTF{almost_like_mario_f617d1d7}`
