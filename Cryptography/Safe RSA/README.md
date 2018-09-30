# Safe RSA
Points: 250

## Category
Cryptography

## Question
>Now that you know about RSA can you help us decrypt this [ciphertext](files/ciphertext)? We don't have the decryption key but something about those values looks funky..  

### Hint
>RSA [tutorial](https://en.wikipedia.org/wiki/RSA_(cryptosystem))
>
>Hmmm that e value looks kinda small right?
>
>These are some really big numbers.. Make sure you're using functions that don't lose any precision!

## Solution
Since _n_ is really huge and _e_ is really tiny, we can figure out the message without needing to factorise _n_!

We can assume that `m ** e < n`. Therefore we do a cube root on _c_, and convert the value into ascii.

Working solution [solve.py](solution/solve.py)

### Flag
`picoCTF{e_w4y_t00_sm411_81b6559f}`
