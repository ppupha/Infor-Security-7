from os import path, remove, rename, chdir, system, replace
from subprocess import check_output
from hashlib import sha256


raw_uuid = check_output("wmic csproduct get UUID")
print("raw_uuid is: [{}]".format(raw_uuid))
raw_uuid = raw_uuid.decode()
print("raw_uuid after decode is [{}]".format(raw_uuid))
uuid = raw_uuid.split("\n")[1][:-4]


raw_inum = check_output("wmic csproduct get identifyingnumber").decode()
inum = raw_inum.split("\n")[1][:-4]


code = uuid + inum
#return str(sha256(code.encode('utf-8')).hexdigest())

print("uuid = #{}#".format(uuid))
print("inum = #{}#".format(inum))

print(code)
print(code.encode('utf-8'))



str_original = input('Please enter string data:\n')

bytes_encoded = str_original.encode()

str_decoded = bytes_encoded.decode()

print('Encoded bytes =', bytes_encoded)
print('Decoded String =', str_decoded)
print('str_original equals str_decoded =', str_original == str_decoded)
