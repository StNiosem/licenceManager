import base64
import hashlib


import base64

retcode = 0

print("Register a licence code\n")

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
        EncodedResult = hashlib.md5(licbytes)
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
    print()
    print("Your " + algo +"-based licence is:")
    print(result)
    print()

main()