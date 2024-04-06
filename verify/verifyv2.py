import base64
import hashlib

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

retcode = 0

print("CHECK A LICENCE CODE\n")

lic = input("Input your licence: \n")
if (lic.startswith("b'") == True) :
    print(bcolors.WARNING + "STRING IS NOT CONCATENATED. THIS WILL FAIL!!!" + bcolors.ENDC)
    retcode = 3
    exit(retcode)
elif (lic == "") :
    print("You did not input a licence.")
    retcode = 4

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


def main():
    print("Choose a licence generation method")
    print("1. Base64")
    print("2. Base32")
    print("3. SHA-1")
    print("4. MD5")

    choice = int(input("Choose an option (1-4): "))
    if choice == 1:
        EncodedResult = base64.b64encode(licbytes)
        algo = "base64"
    elif choice == 2:
        EncodedResult = base64.b32encode(licbytes)
        algo = "base32"
    elif choice == 3:
        EncodedResult = hashlib.sha1(licbytes)
        algo = "SHA-1"
    elif choice == 4:
        EncodedResult = hashlib.sha1(licbytes)
        algo = "MD5"
    else:
        return "Invalid choice"

    if choice == 1:
        result = EncodedResult.decode("utf-8")
    elif choice == 2:
        result = EncodedResult.decode("utf-8")
    elif choice == 3:
        result = EncodedResult.hexdigest()
    elif choice == 4:
        result = EncodedResult.hexdigest()
    else:
        return "Invalid choice"
    
    if (result == lic) :
        licstatus = bcolors.OKGREEN + "VALID" + bcolors.ENDC
        retcode = 0
    else :
        licstatus = bcolors.FAIL + "INVALID" + bcolors.ENDC
        retcode = 1


    print()
    print("Your " + algo +"-based licence is:")
    print(result)
    print()
    print("The licence you have input is :")
    print(lic)
    print()
    print("LICENCE IS " + licstatus)
    print()
    exit(retcode)

main()