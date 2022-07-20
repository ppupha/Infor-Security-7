from os import path, remove, rename, chdir, system, replace
from subprocess import check_output
from hashlib import sha256

def get_key():
    raw_uuid = check_output("wmic csproduct get UUID").decode()
    uuid = raw_uuid.split("\n")[1][:-4]

    code = uuid
    return str(sha256(code.encode('utf-8')).hexdigest())



def create_license(filename):
    with open(filename, "w+") as license:
        license.write(get_key())

def run_installation(filename):
    key = get_key()
    if not rewrite_file(filename, key):
        print(f"Error: file {filename} doesn't exist")
        return False
    system("pyinstaller.exe -F .\main.py")
    return True


if __name__ == '__main__':
    system("pyinstaller.exe -F .\main.py")
    create_license(".\\dist\\license.key")
