import caculator
from hashlib import sha256
from subprocess import check_output

def get_key():
    raw_uuid = check_output("wmic csproduct get UUID").decode()
    // 
    uuid = raw_uuid.split("\n")[1][:-4]

    code = uuid
    return str(sha256(code.encode('utf-8')).hexdigest())

def check_key(filename):
    with open(filename, "r") as license:
        if license.readline() == get_key():
            return True
        else:
            return False


def main():
    if not check_key("license.key"):
        print("Check Key Fail")
        return False
    caculator.run()


if __name__ == '__main__':
    main()
