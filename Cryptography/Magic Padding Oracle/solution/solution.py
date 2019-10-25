import nclib, sys, binascii

# Generate all 256 binary combinations of 1 byte
byte_combinations = []
for i in range(0, 256):
    i = hex(i)[2:]
    byte_combinations.append('0' + i if len(i) == 1 else i)

# Add zeros to the front of hex string.
def add_zeros(string, desired_length):
    while len(string) < desired_length:
        string = '0' + string
    return string

# Uses the padding oracle to return the decrypted hex string of the input cipherblock
def decrypt_ciphertext(cipherblock):
    # Queries the server and submits the ciphertext
    # If invalid padding, return False. Else True (might be buggy if input is wrongly formatted)
    def check_pad(s: str) -> bool:
        print(s[:32]) # Print the IV
        nc = nclib.Netcat(connect = ('2018shell1.picoctf.com', 27533), verbose = False)
        nc.settimeout(2)

        # Receive the first 2 messages given by the server
        nc.recv()
        nc.recv()

        # Send the cipherblocks with new line char behind to signify the end of the input
        nc.send(s.encode() + b'\n')

        # Receive data
        data = nc.recv(100000)
        if b'invalid padding' in data:
            return False
        else:
            print(data) # Make sure data is error about JSON string
            return True
    
    decrypted_cipherblock = ''
    for i in range(1, 17): # Block length is 128 bits = 16 bytes
        # Try all combination of bits
        for byte in byte_combinations:
            found = False

            iv_prime = '0' * (32 - i * 2) + byte
            if i != 1: # Account for the padding for 2nd byte onwards
                # Get the values required to achieve the back padding by XOR-ing the pad with the known D(C)
                pad = (byte_combinations[i] * (i - 1))
                padding_for_iv = hex(int(pad, base=16) ^ int(decrypted_cipherblock, base=16))[2:]
                padding_for_iv = add_zeros(padding_for_iv, len(pad))
                iv_prime += padding_for_iv

            # Send to padding oracle
            res = check_pad(iv_prime + cipherblock)
            if res == True: # Correct padding obtained, calculate D(C)'s byte
                val = int(byte_combinations[i], base=16) ^ int(byte, base=16)
                val = hex(val)[2:]
                decrypted_cipherblock = '0' + val + decrypted_cipherblock if len(val) == 1 else val + decrypted_cipherblock
                found = True
                break

        # If all 256 bytes have been exhausted without a valid padding, then something went wrong.
        if found == False:
            print('Error - couldn\'t find proper padding.')
            return
    return decrypted_cipherblock

# Encrypts a given plaintext by using the padding oracle attack as a decryption oracle.
def encrypt_plaintext(plaintext):
    # Splits input string into blocks of 16 bytes and pads the last block according to PKCS #7
    def split_input_string(input_string):
        BLOCK_LENGTH = 16 # 16 bytes
        splitted_input_string = []

        # Split into blocks of 16 bytes
        for _ in range(len(input_string) // BLOCK_LENGTH):
            splitted_input_string.append(input_string[:BLOCK_LENGTH])
            input_string = input_string[BLOCK_LENGTH:]
        
        # Pad the last block
        padding_required = BLOCK_LENGTH - len(input_string)
        padding_required = '0' + hex(padding_required)[2:] if len(hex(padding_required)[2:]) == 1 else hex(padding_required)[2:]
        while len(input_string) < BLOCK_LENGTH:
            input_string += binascii.unhexlify(padding_required.encode())
        
        # Append to output array of blocks of 16 bytes and return
        splitted_input_string.append(input_string)
        return splitted_input_string
    
    # Get 16 byte blocks of the plaintext
    plaintext = split_input_string(plaintext.encode())
    arbitrary_ciphertext_block = 'cafebabecafebabecafebabecafebabe'

    # Ciphertext should end with this arbitrary block
    ciphertext = [arbitrary_ciphertext_block]

    # Get blocks from the back of the plaintext
    current_cipher_block = arbitrary_ciphertext_block
    for block in plaintext[::-1]:
        # Get D(C_n)
        current_decrypted_block = decrypt_ciphertext(current_cipher_block)

        # Get C_n-1 by XOR-ing with plaintext block
        previous_cipher_block = int.from_bytes(block, byteorder='big') ^ int(current_decrypted_block, base=16)
        previous_cipher_block = hex(previous_cipher_block)[2:]
        previous_cipher_block = add_zeros(previous_cipher_block, 32)

        ciphertext.append(previous_cipher_block) # Append to ciphertext
        current_cipher_block = previous_cipher_block # Make prev cipherblock current cipherblock

    return ciphertext

plaintext = '{"username": "cafebabe!","is_admin": "true","expires": "2020-1-1"}'
ciphertext = encrypt_plaintext(plaintext)

# Print out ciphertext
for block in ciphertext[::-1]:
    print(block, end=' ')
