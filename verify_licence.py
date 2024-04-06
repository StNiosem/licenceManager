import base64

retcode = 0

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
if (lic.startswith("b'") == True) :
    print(bcolors.WARNING + "STRING IS NOT CONCATENATED. THIS WILL FAIL!!!" + bcolors.ENDC)
    retcode = 3
    exit(retcode)
elif (lic == "") :
    print("You did not input a licence.")
    retcode = 4
else :
    print(bcolors.OKGREEN + "Licence properly concatenated" + bcolors.ENDC)

licName = input("Name of the licence owner:\n")
print("\n")
if (licName == "") : 
    print("Licence holder name cannot be blank.")
    retcode = 5
    exit(retcode)

licVerifCode = input("Input the licence verification code:\n")
print("\n")
if (licVerifCode == "") :
    print("The Licence Verification Code cannot be blank.")
    retcode = 6
    exit(retcode)

licPassPhrase = input("Input your licence passphrase:\n")
print("\n")
if (licPassPhrase == "") :
    print("The Licence Passphrase cannot be empty.")
    retcode = 7
    exit(retcode)


licbytes = bytes(licName+licVerifCode+licPassPhrase, 'utf-8')

licb64 = base64.b64encode(licbytes)
licb64_decoded = licb64.decode("utf-8")

if (str(licb64_decoded) == str(lic)) :
    licstatus = bcolors.OKGREEN + "VALID" + bcolors.ENDC
    retcode = 0
else : 
    licstatus = bcolors.FAIL + "INVALID" + bcolors.ENDC
    retcode = 1

print("Your licence status :\n")
print(licstatus + "\n")
print("licence input : " + str(lic))
print("licence verification : " + str(licb64_decoded))
exit(retcode)