import sys
from base64 import *
from random import randrange
from Crypto.Util.number import inverse
from math import sqrt


def gcd_extend(a, b):
    x0, x1 = 1, 0
    y0, y1 = 0, 1
    while b:
        r = a % b
        if r == 0:
            break
        q = a // b
        a, b = b, r

        x0, x1 = x1, x0-x1*q
        y0, y1 = y1, y0-y1*q

    return b, x1, y1


def mod_inverse(a, m):
    '''
    ax = 1 (mod m)
    '''
    g, x, _ = gcd_extend(a, m)
    if g != 1:
        return -1
    return (x % m + m) % m


def get_prime(c = None):
    while (1):
        r = randrange(256, 256*2) * 2  +  1
        if (not isPrime(r)):
            continue
        print("r = {}".format(r))
        if (c == None):
            return r
        if c != r:
            return r

def isPrime(n):
    if (n <= 0):
        return False
    for i in range(2, int(sqrt(n))):
        if (n % i == 0):
            return False
    return True
    
def power(a, n, m):
    res = 1
    for i in range(n):
        res = (res * a) % m
    return res


class RSA(object):
    def __init__(self, p, q):
        #if (not isPrime(p) or isPrime(q)):
        #    return
        self.n = p * q
        self.phi = (p - 1) * (q - 1)
        self.e = self.get_e(self.phi)
        self.d = self.get_d(self.e, self.phi)
        print(" p = {}\n q = {}\n e = {}\n d = {}\n".format(p, q, self.e, self.d))
        

    def crypt(self, char, key):
        res = 1
        for i in range(key):
            res = res * char % self.n
        return res
        #return char ** key % self.n

    def encrypt_string(self, string):
        result = ""
        for char in string:
            current_char = self.crypt(ord(char), self.e)
            result += chr(current_char)
        return result

    def decrypt_string(self, string):
        result = ""
        for char in string:
            #print(char)
            current_char = self.crypt(ord(char), self.d)
            result += chr(current_char)
        return result

    def euclid(self, a, b):
        while b != 0:
            a, b = b, a % b
        return a

    def get_d(self, e, phi):
        return mod_inverse(e, phi)

    def get_e(self, phi):
        result = 2
        while True:
            #result = randrange(2, phi)
            result += 1
            if self.euclid(result, phi) == 1:
                return result


if __name__ == '__main__':

    if len(sys.argv) < 2:
        source_str = "Hello World"
        print("Source: ", source_str)
        PRIME1 = get_prime()
        PRIME2 = get_prime(PRIME1)
        rsa = RSA(PRIME1, PRIME2)

        encoded = b64encode(source_str.encode("UTF-8")).decode('ascii')
        rsa_decoded = rsa.encrypt_string(encoded)
        print("Encrypted: ", rsa_decoded)

        print("Starting Decrypt")
        decrypted_rsa = rsa.decrypt_string(rsa_decoded)
        decoded = b64decode(decrypted_rsa)
        print("Decrypted: ", decoded.decode("UTF-8"))
    else:
        filename = sys.argv[1]
        PRIME1 = get_prime()
        PRIME2 = get_prime(PRIME1)
        with open(filename, 'rb') as input_file:
            data = input_file.read()
            rsa = RSA(PRIME1,PRIME2)

            source_str = b32encode(data)
            decoded_str = source_str.decode("ascii")
            print("Encrypting...")

            encrypted = rsa.encrypt_string(decoded_str)
            with open("encrypted_" + filename, 'wb') as encrypted_file:
                encrypted_file.write(encrypted.encode())
                encrypted_file.close()
            print("Write to file encrypted_{}\n".format(filename))
            print("Decrypting...")

            decrypted = rsa.decrypt_string(encrypted)
            restored = b32decode(decrypted)
            with open("decrypted_" + filename, 'wb') as restored_file:
                restored_file.write(restored)
                restored_file.close()
            print("Write to file decrypted_{}\n".format(filename))
