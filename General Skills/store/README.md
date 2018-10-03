# store
Points: 400

## Category
General Skills

## Question
>We started a little [store](files/store), can you buy the flag? [Source](files/source.c). Connect with `2018shell1.picoctf.com 53220`. 

### Hint
>Two's compliment can do some weird things when numbers get really big!

## Solution
Based off the hint, we can assume it's probably an integer overflow. HOWEVER, just by doing _strings_

```
$ strings store | grep pico
YOUR FLAG IS: picoCTF{numb3r3_4r3nt_s4f3_cbb7151f}
```

Don't store the flag in the local binary next time.

### Flag
`picoCTF{numb3r3_4r3nt_s4f3_cbb7151f}`
