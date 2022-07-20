import random
import base64
from os.path import basename, splitext
ASCII_SIZE = 256

def enigmaRotor():
    rotor = [None for _ in range(ASCII_SIZE)]

    cur_num = 0
    while None in rotor:
        index = random.randint(0, ASCII_SIZE - 1)
        if rotor[index] is None:
            rotor[index] = cur_num
            cur_num += 1

    return rotor

def enigmaReflector():
    reflector = [None for _ in range(ASCII_SIZE)]
    tmp = [x for x in range(ASCII_SIZE)]

    for i in range(ASCII_SIZE):
        if reflector[i] is None:
            num = random.choice(tmp)
            while num == i:
                num = random.choice(tmp)
            tmp.pop(tmp.index(num))
            tmp.pop(tmp.index(i))
            reflector[i] = num
            reflector[num] = i

    return reflector

def enigmaEncrypt(s, rotor1, rotor2, rotor3, reflector):
    s1 = rotor1.index(s)
    s2 = rotor2.index(s1)
    s3 = rotor3.index(s2)
    s4 = reflector.index(s3)
    s5 = rotor3[s4]
    s6 = rotor2[s5]
    s7 = rotor1[s6]

    return s7


def enigmaEncryptMsg(msg, rotor1, rotor2, rotor3, reflector):
    nums = [ord(c) for c in msg]
    res_msg = []
    shift1 = 0
    shift2 = 0
    shift3 = 0
    for s in nums:
        res_msg.append(enigmaEncrypt(s, rotor1, rotor2, rotor3, reflector))
        if shift1 < ASCII_SIZE:
            rotor1 = rotor1[1:] + rotor1[:1]
            shift1 += 1
        elif shift2 < ASCII_SIZE:
            rotor1 = rotor1[1:] + rotor1[:1]
            rotor2 = rotor2[1:] + rotor2[:1]
            shift1 = 0
            shift2 += 1
        elif shift3 < ASCII_SIZE:
            rotor1 = rotor1[1:] + rotor1[:1]
            rotor2 = rotor2[1:] + rotor2[:1]
            rotor3 = rotor3[1:] + rotor3[:1]
            shift1 = 0
            shift2 = 0
            shift3 += 1
        else:
            rotor1 = rotor1[1:] + rotor1[:1]
            rotor2 = rotor2[1:] + rotor2[:1]
            rotor3 = rotor3[1:] + rotor3[:1]
            shift1 = 0
            shift2 = 0
            shift3 = 0

    return ''.join([chr(c) for c in res_msg])


def saveEnigmaStt(rotor1, rotor2, rotor3, reflector, file_path):
    with open("encode.inf", 'a') as file:
        file.write(file_path + '\n' + str(rotor1) + '\n' + str(rotor2) + '\n'
                   + str(rotor3) + '\n' + str(reflector) + '\n')
        file.close()


def getEnigmaStt(file_name):
    file = open("encode.inf")
    data = file.read().split('\n')
    r1, r2, r3, ref = None, None, None, None
    for i in range(len(data)):
        if data[i] == file_name:
            r1 = data[i + 1]
            r2 = data[i + 2]
            r3 = data[i + 3]
            ref = data[i + 4]
    if ref == None:
        return [], [], [], []

    rotor1 = list(map(int, r1[1:-1].split(', ')))
    rotor2 = list(map(int, r2[1:-1].split(', ')))
    rotor3 = list(map(int, r3[1:-1].split(', ')))
    reflector = list(map(int, ref[1:-1].split(', ')))

    return rotor1, rotor2, rotor3, reflector


def encodeFile(file_path, rotor1, rotor2, rotor3, reflector):
    try:
        with open(file_path, 'rb') as f:
            msg = base64.b64encode(f.read()).decode('ascii')
            msg_enc = enigmaEncryptMsg(msg, rotor1, rotor2, rotor3, reflector)
            f.close()

        file_name = basename(file_path)
        new_file_name = splitext(file_name)[0] + ".enc"
        with open(new_file_name, 'wb') as file:
            file.write(msg_enc.encode("UTF-8"))
            file.close()
        print("\nResult in file {}\n".format(new_file_name))
        saveEnigmaStt(rotor1, rotor2, rotor3, reflector, new_file_name)
        return new_file_name

    except FileNotFoundError:
        print("file " + file_path + " not found")
    return ""
        
def decodeFile(file_path):
    file_name = basename(file_path)
    try:
        with open(file_path, 'rb') as f:
            msg_enc = f.read().decode("UTF-8")
            rotor1, rotor2, rotor3, reflector = getEnigmaStt(file_name)
            if len(rotor1) == 0:
                print("Cònigure File not Found")
            else:
                msg_decr = enigmaEncryptMsg(msg_enc, rotor1, rotor2, rotor3, reflector)
                new_file_name = splitext(file_name)[0] + ".dec"
                with open(new_file_name, 'wb') as file:
                    file.write(base64.b64decode(msg_decr))
                    file.close()
            f.close()
            
            print("Result Decode in File {}\n".format(new_file_name))
    except FileNotFoundError:
        print("file " + file_path + " not found")

def main():

    choice = None
    while choice != '0':
        print("1. Enigma Encode\n2. Enigma Decode\n0. Exit")
        choice = input("Input Your Choise: ")

        #Encode
        if choice == '1':
            next_choice = None
            while next_choice != '0':
                print("What do you want to Encode?\n1. String\n2. File\n0. Back")
                next_choice = input("Your Choise: ")

                #Back
                if (next_choice == '0'):
                    continue
                rotor1 = enigmaRotor()
                rotor2 = enigmaRotor()
                rotor3 = enigmaRotor()
                reflector = enigmaReflector()

                #Encode String
                if next_choice == '1':
                    msg = input("Input String to Encode: ")
                    msg = base64.b64encode(msg.encode("UTF-8")).decode('ascii')
                    msg_enc = enigmaEncryptMsg(msg, rotor1, rotor2, rotor3, reflector)
                    print("String After Encode: ", msg_enc)

                    flag = input("Decode?[Y\\N]")
                    if flag == 'Y':
                        msg_decr = enigmaEncryptMsg(msg_enc, rotor1, rotor2, rotor3, reflector)
                        msg_decr = base64.b64decode(msg_decr).decode("UTF-8")
                        print("String Aftẻ Decode: " + msg_decr)

                #Encode File
                elif next_choice == '2':
                    file_path = input("Input File Name: ")
                    encode_file_name = encodeFile(file_path, rotor1, rotor2, rotor3, reflector)
                    flag = input("Decode?[Y\\N]")
                    if flag == 'Y':
                        decode_file_name = decodeFile(encode_file_name)
                        print("\nResult in file {}\n".format(decode_file_name))

        #Decode File
        elif choice == '2': 
            file_path = input("Input File Name: ")
            decodeFile(file_path)


if __name__ == '__main__':
    main()
