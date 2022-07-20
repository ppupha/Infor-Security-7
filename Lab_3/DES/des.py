from struct import pack

MAX_LEN = 1024
ROUNDS = 16
ENCRYPT = 0
DECRYPT = 1

PI = [58, 50, 42, 34, 26, 18, 10, 2,
      60, 52, 44, 36, 28, 20, 12, 4,
      62, 54, 46, 38, 30, 22, 14, 6,
      64, 56, 48, 40, 32, 24, 16, 8,
      57, 49, 41, 33, 25, 17, 9, 1,
      59, 51, 43, 35, 27, 19, 11, 3,
      61, 53, 45, 37, 29, 21, 13, 5,
      63, 55, 47, 39, 31, 23, 15, 7]

PI_1 = [40, 8, 48, 16, 56, 24, 64, 32,
        39, 7, 47, 15, 55, 23, 63, 31,
        38, 6, 46, 14, 54, 22, 62, 30,
        37, 5, 45, 13, 53, 21, 61, 29,
        36, 4, 44, 12, 52, 20, 60, 28,
        35, 3, 43, 11, 51, 19, 59, 27,
        34, 2, 42, 10, 50, 18, 58, 26,
        33, 1, 41, 9, 49, 17, 57, 25]

C0_D0 = [57, 49, 41, 33, 25, 17, 9,
        1, 58, 50, 42, 34, 26, 18,
        10, 2, 59, 51, 43, 35, 27,
        19, 11, 3, 60, 52, 44, 36,
        63, 55, 47, 39, 31, 23, 15,
        7, 62, 54, 46, 38, 30, 22,
        14, 6, 61, 53, 45, 37, 29,
        21, 13, 5, 28, 20, 12, 4]

C1_D1 = [14, 17, 11, 24, 1, 5, 3, 28,
        15, 6, 21, 10, 23, 19, 12, 4,
        26, 8, 16, 7, 27, 20, 13, 2,
        41, 52, 31, 37, 47, 55, 30, 40,
        51, 45, 33, 48, 44, 49, 39, 56,
        34, 53, 46, 42, 50, 36, 29, 32]

SHIFT = [1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1]

E = [32, 1, 2, 3, 4, 5,
     4, 5, 6, 7, 8, 9,
     8, 9, 10, 11, 12, 13,
     12, 13, 14, 15, 16, 17,
     16, 17, 18, 19, 20, 21,
     20, 21, 22, 23, 24, 25,
     24, 25, 26, 27, 28, 29,
     28, 29, 30, 31, 32, 1]

P = [16, 7, 20, 21, 29, 12, 28, 17,
     1, 15, 23, 26, 5, 18, 31, 10,
     2, 8, 24, 14, 32, 27, 3, 9,
     19, 13, 30, 6, 22, 11, 4, 25]

S = [
         
[[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
 [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
 [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
 [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13],
],

[[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
 [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
 [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
 [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9],
],

[[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
 [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
 [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
 [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12],
],

[[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
 [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
 [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
 [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14],
],  

[[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
 [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
 [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
 [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3],
], 

[[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
 [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
 [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
 [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13],
], 

[[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
 [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
 [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
 [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12],
],
   
[[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
 [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
 [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
 [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11],
]
]

class DES():
    
    def __init__(self, key):
        if len(key) < 8:
            raise "Key lenght must be 64 bits"
        if len(key) > 8:
            key = key[:8]

        self.key = key
        self.keys = self.generate_16_keys()

    def generate_16_keys(self):
        keys = []
        key = self.to_bit_array(self.key) 
        key = self.permut(key, C0_D0) # 64 -> 56
        l, r = self.split_on_blocks(key, 28) # 2 * 28
        for i in range(ROUNDS):
            # left shift 
            l = self.shift(l, SHIFT[i])
            r = self.shift(r, SHIFT[i])
            keys.append(self.permut(l + r, C1_D1)) #  48 bit
        return keys

    # encode / decode string
    def process_string(self, string, action=ENCRYPT):
        res = b''
        for block in self.split_on_blocks(string, 8): # 8 * 8 = 64
            res += self.process(block, action)
        return res
  
    # encode / decode block data
    def process(self, data, action=ENCRYPT):
        
        if len(data) != 8: 
            raise "Lenght of data must be 64 bits"
        
        data = self.to_bit_array(data)
        #print(data)
        data = self.permut(data, PI) # IP 64 -> 64

        l, r = self.split_on_blocks(data, 32) # 32 * 2
        t = None
        for i in range(ROUNDS):
            if action == ENCRYPT:
                t = r
                r = self.xor(l, self.funcFeistel(r, self.keys[i])) # function f(32bit, 48bit)
                l = t
            else:
                t = l
                l = self.xor(r, self.funcFeistel(l, self.keys[::-1][i]))
                r = t

        data =  self.permut(l + r, PI_1) # IP-1 64-> 64

        return self.to_bytestring(data)

    def funcFeistel(self, data, key): # (32bit, 48bit)
        data = self.permut(data, E) # E: 32 ->48 bit
        data = self.xor(data, key)

        blocks = self.split_on_blocks(data, 6) # 32 -> 8 block (6 bit)

        res = []
        for i in range(len(blocks)):
            block = blocks[i]
            row = int(str(block[0]) + str(block[5]), 2)
            column = int(''.join([str(x) for x in block[1:5]]), 2)
            value = S[i][row][column] # 6 bit -> 10sys
            bin_value = self.binvalue(value, 4) # 10sys -> 4 bit
            res += [int(x) for x in bin_value]
        
        return self.permut(res, P) # P  res (32) -> 32

    def permut(self, data, table):
        return [data[x-1] for x in table]

    def split_on_blocks(self, data, block_size):
        count = int(len(data) / block_size)
        blocks = []
        for i in range(count):
            blocks.append(data[block_size * i : block_size * (i + 1)])
        
        return blocks

    def shift(self, data, n):
        return data[n:] + data[:n]

    def xor(self, arr1, arr2):
        return [x^y for x,y in zip(arr1, arr2)]
        
    def binvalue(self, val, bitsize): 
        binval = bin(val)[2:] if isinstance(val, int) else bin(ord(val))[2:]
        while len(binval) < bitsize:
            binval = '0' + binval
        return binval

    def to_bit_array(self, data):
        array = list()
        for item in data:
            binval = self.binvalue(item, 8)
            array.extend([int(x) for x in list(binval)])
        return array
    def to_bytestring(self, data):
        n = int(len(data) / 8)
        res = b''
        for i in range(n):
            arr = data[8 * i: 8 * (i + 1)]
            num = int(''.join([str(x) for x in arr]), 2)
            res += pack('B', num)
        return res

        

