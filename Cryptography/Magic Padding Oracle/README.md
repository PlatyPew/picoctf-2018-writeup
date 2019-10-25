# Magic Padding Oracle
Points: 450

## Category
Cryptography

## Question
>Can you help us retreive the flag from this crypto service? Connect with `nc 2018shell1.picoctf.com 27533`. We were able to recover some [Source](files/pkcs7.py) Code.  

### Hint
>Paddding Oracle [Attack](https://blog.skullsecurity.org/2013/padding-oracle-attacks-in-depth)

## Solution
We have to submit the encrypted JSON string with the `"is_admin"` property set to a string called `"true"` and the `"expires"` property changed to a date later than the date the string was submitted. Also take note that the date string has to adhere to the following format: `%Y-%m-%d`. The `"username"` property has to be present but can be of any value.

This JSON string: `{"username": "cafebabe!","is_admin": "true","expires": "2020-1-1"}` was accepted.
The encrypted JSON string is: `bab23fa6e34b02b1b4279bf85d89e03e4d8fc9cc9dee572b7c40c9c710f27426437ce07b7d4356c9a97dff9840209d50c9b18d4547f557437fe70d5c62f66283590c5cdaf042515720b8879e43de91e4cafebabecafebabecafebabecafebabe`

In order to encrypt it without the key, we can use the padding oracle attack to make a decryption oracle. This decryption oracle is able to take in a ciphertext block and output the corresponding decrypted ciphertext block.

We are able to do this by submitting 2 ciphertext blocks. The first is the IV, which we will use to brute force the decrypted ciphertext block, and the second is the actual ciphertext block.

We try all bytes (`0x00` to `0xff`) on the last byte of the IV until we get a valid padding response (in this case, the server would respond with an error from `json.loads()` because what was being submitted is not a valid JSON string).

Because we know the padding bytes (`0x01`, `0x02 0x02`, ... `0x0f 0x0f ... 0x0f`, `0x10 0x10 ... 0x10`), we can continue with the 2nd last byte all the way until the first byte to figure out what the decrypted ciphertext is.

By using the decryption oracle, we can encrypt the JSON string by working from the back of the plaintext string (properly padded, split into 16 byte blocks) by setting the last ciphertext block as an arbitrary 16 byte ciphertext block (I used `0xcafebabecafebabecafebabecafebabe`).

Then by XOR-ing the decrypted ciphertext block and the last 16 bytes of the plaintext, we can get the previous ciphertext block. We repeatedly can do this all the way from the back until we get to the first ciphertext block (the IV).

Then we concatenate the IV and all the ciphertext blocks and submit it to the server, which will decrypt into the JSON string and return the flag.

#### Note

For some reason the communication with the server is really slow. I am not sure whether it is a limitation of the nclib library, but as a result each 16 byte block takes ~1 hour to decrypt.

Hence encrypting the entire JSON string takes around -4 hours because it's 4 blocks long.

### Flag
`picoCTF{0r4cl3s_c4n_l34k_c644af03}`
