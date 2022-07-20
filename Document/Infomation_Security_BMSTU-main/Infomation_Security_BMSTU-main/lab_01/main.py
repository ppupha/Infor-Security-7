magic_number = '9c8687917825b09672924625e21aff828d88b34c067e393b53453aa9efe240f9'

import program
from hashlib import sha256
from subprocess import check_output

def get_key():
    raw_uuid = check_output("wmic csproduct get UUID").decode()
    uuid = raw_uuid.split("\n")[1][:-4]

    raw_inum = check_output("wmic csproduct get identifyingnumber").decode()
    inum = raw_inum.split("\n")[1][:-4]

    code = uuid + inum
    return str(sha256(code.encode('utf-8')).hexdigest())


def main():
    print("Get Key = {}".format(get_key()))
    if not magic_number == get_key():
        print("access denied")
        input()
        #return False
    program.run()


if __name__ == '__main__':
    main()
