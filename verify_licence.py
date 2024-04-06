import base64

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

print("LICENCE CHECKER\n")

lic = input("Input your licence: \n")
licName = input("Name of the licence owner:\n")
licVerifCode = input("Input the licence verification code:\n")
licPassPhrase = input("Input your licence passphrase:\n")
licbytes = bytes(licName+licVerifCode+licPassPhrase, 'utf-8')

licb64 = base64.b64encode(licbytes)

if (str(licb64) == str(lic)) :
    licstatus = bcolors.OKGREEN + "VALID" + bcolors.ENDC
else : 
    licstatus = bcolors.FAIL + "INVALID" + bcolors.ENDC

print("Your licence status :\n")
print(licstatus + "\n")
print("licence input : " + str(lic))
print("licence verification : " + str(licb64))