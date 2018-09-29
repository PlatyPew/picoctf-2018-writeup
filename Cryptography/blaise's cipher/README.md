# blaise's cipher
Points: 200

## Category
Cryptography

## Question
>My buddy Blaise told me he learned about this cool cipher invented by a guy also named Blaise! Can you figure out what it says? Connect with `nc 2018shell1.picoctf.com 46966`. 

### Hint
>There are tools that make this easy.
>
>This cipher was NOT invented by Pascal

## Solution
This is a Vigenère Cipher, this time without a key. Bruteforce using an online tool. Online tool: https://www.mygeocachingprofile.com/codebreaker.vigenerecipher.aspx

### Flag
`picoCTF{v1gn3r3_c1ph3rs_ar3n7_bad_cdf08bf0}`
