# Super Safe RSA 3 
Points: 600

## Category
Cryptography

## Question
>The more primes, the safer.. right.?.? Connect with `nc 2018shell1.picoctf.com 11423`. 

### Hint
>How would you find d if there are more than 2 prime factors of n?

## Solution
Use msieve to install to factorise the primes

Calculate the totient by doing `(prime_1 - 1) * (prime_2 - 1) ... (prime_n - 1)` where `n` is the total number of primes

Reconstruct the private key, and decrypt the message

Recommended reads: https://crypto.stackexchange.com/questions/44110/rsa-with-3-primes

### Flag
`picoCTF{p_&_q_n0_r_$_t!!_6629910}`
