import base64

print("Register a licence code\n")

licName = input("Name of the licence owner:\n")
licVerifCode = input("Input the licence verification code:\n")
licPassPhrase = input("Input your licence passphrase:\n")
licbytes = bytes(licName+licVerifCode+licPassPhrase, 'utf-8')
 
licb64 = base64.b64encode(licbytes)
print("Your licence:\n")
print(licb64)