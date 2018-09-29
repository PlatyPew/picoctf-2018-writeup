# HEEEEEEERE'S Johnny!
Points: 100

## Category
Cryptography

## Question
>Okay, so we found some important looking files on a linux computer. Maybe they can be used to get a password to the process. Connect with `nc 2018shell1.picoctf.com 5221`. Files can be found here: [passwd](files/passwd) [shadow](files/shadow). 

### Hint
>If at first you don't succeed, try, try again. And again. And again.
>
>If you're not careful these kind of problems can really "rockyou".

## Solution
Do `john --wordlist=rockyou.txt shadow`

The file _rockyou.txt_ can be found from _/usr/share/wordlists/rockyou.txt.gz_.

Extract the file by doing `gzip -d rockyou.txt.gz`

Connect to service and enter in credentials to get the flag.

```
$ nc 2018shell1.picoctf.com 5221
Username: root
Password: thematrix
picoCTF{J0hn_1$_R1pp3d_289677b5}
```

### Flag
`picoCTF{J0hn_1$_R1pp3d_289677b5}`
