import base64
from pwn import xor 
import binascii

foo = "label"

hexFoo = binascii.hexlify(foo.encode()).decode()

print("Result of hex:", hexFoo)

bFoo = bytes.fromhex(hexFoo)

result = xor(bFoo, 13)

print("Result of Xor:", result.decode())