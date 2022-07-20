from os import path, remove, rename, chdir, system, replace
from subprocess import check_output
from hashlib import sha256


def get_key():
    raw_uuid = check_output("wmic csproduct get UUID").decode()
    uuid = raw_uuid.split("\n")[1][:-4]

    raw_inum = check_output("wmic csproduct get identifyingnumber").decode()
    inum = raw_inum.split("\n")[1][:-4]

    code = uuid + inum
    return str(sha256(code.encode('utf-8')).hexdigest())


def rewrite_file(filename, key):
    if not path.isfile(filename):
        return False
    f = open(filename, 'r')
    new_f = open("new.txt", 'w')
    lines = f.readlines()

    new_f.write("magic_number = " + '\'' + str(key) + '\'' + '\n')
    for i in range(1, len(lines)):
        new_f.write(lines[i])

    f.close()
    new_f.close()
    remove(path.abspath(filename))
    rename("new.txt", filename)

    return True


def build_image():
    try:
        chdir("venv")
        chdir("Scripts")
        system(".\pyinstaller.exe -F ../../main.py")
        replace("C:\\Users\\vlad2\\Desktop\\7th_part\\Infomation_Security\\lab_01\\venv\\Scripts\\dist\\main.exe",
                "C:\\Users\\vlad2\\Desktop\\7th_part\\Infomation_Security\\lab_01\\main.exe")
    except:
        print("Something went wrong")
    return


def run_installation(filename):
    key = get_key()
    if not rewrite_file(filename, key):
        print(f"Error: file {filename} doesn't exist")
        return False
    build_image()
    return True


if __name__ == '__main__':
    run_installation("main.py")

