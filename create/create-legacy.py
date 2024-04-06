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
 
licb64 = base64.b64encode(licbytes)
licb64_decoded = licb64.decode("utf-8")

print("Your licence:\n")
print(licb64_decoded)