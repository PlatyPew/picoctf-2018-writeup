# Radix's Terminal 
Points: 400

## Category
Reversing

## Question
>Can you find the password to Radix's login? You can also find the executable in /problems/radix-s-terminal_0_b6b476e9952f39511155a2e64fb75248?

### Hint
>https://en.wikipedia.org/wiki/Base64

## Solution
Based off the hint, we can assume the flag is being encoded in base64 just by doing _strings_

```
cGljb0NURntiQXNFXzY0X2VOQ29EaU5nX2lTX0VBc1lfNDE3OTk0NTF9
Please provide a password!
Congrats, now where's my flag?
Incorrect Password!
;*2$"
ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/
GCC: (Ubuntu 5.4.0-6ubuntu1~16.04.10) 5.4.0 20160609

```
putting the string cGljb0NURntiQXNFXzY0X2VOQ29EaU5nX2lTX0VBc1lfNDE3OTk0NTF9 in a base 64 decode will return us the flag


### Flag
`picoCTF{bAsE_64_eNCoDiNg_iS_EAsY_41799451}`
