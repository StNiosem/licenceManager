# Licence Manager
The licence manager is a test repo, whiwh hopefully one day could verify licences for projects.

## Licence creator
Currently, it only works by taking a name, licence code and passphrase and putting them together like this :
    
    NameLicencecodePassphrase

and Base64-ing the whole of it.

### example
Name = `StNiosem`  
Licence Code = `123456`  
Passphase = [correct horse battery staple](https://xkcd.com/936/)

```shell
Name of the licence owner:
StNiosem

Input the licence verification code:
123456

Input your licence passphrase:
correct horse battery staple

Your licence:

U3ROaW9zZW0xMjM0NTZjb3JyZWN0IGhvcnNlIGJhdHRlcnkgc3RhcGxl
```

outputs `U3ROaW9zZW0xMjM0NTZjb3JyZWN0IGhvcnNlIGJhdHRlcnkgc3RhcGxl`


## Licence Verifyer
The licence verifyer works by asking the licence, and asking name, licence and passphrase. 
It generates the licence using the provided info and compares it to the inputted licence. 
If it matches it outputs 'VALID' in green, if it does not it outputs 'INVALID' in red-ish orange

Variables are the same.

Correct licence  
lic = `U3ROaW9zZW0xMjM0NTZjb3JyZWN0IGhvcnNlIGJhdHRlcnkgc3RhcGxl`
```shell
LICENCE CHECKER

Input your licence: 
U3ROaW9zZW0xMjM0NTZjb3JyZWN0IGhvcnNlIGJhdHRlcnkgc3RhcGxl
Licence properly concatenated (is green)
Name of the licence owner:
StNiosem


Input the licence verification code:
123456


Input your licence passphrase:
correct horse battery staple


Your licence status :

VALID (is green)

licence input : U3ROaW9zZW0xMjM0NTZjb3JyZWN0IGhvcnNlIGJhdHRlcnkgc3RhcGxl
licence verification : U3ROaW9zZW0xMjM0NTZjb3JyZWN0IGhvcnNlIGJhdHRlcnkgc3RhcGxl
```

Incorrect Licence
lic = `obviously incorrect b64`
```shell
Input your licence: 
obviously incorrect b64
Licence properly concatenated (is green)
Name of the licence owner:
StNiosem


Input the licence verification code:
123456


Input your licence passphrase:
correct horse battery staple


Your licence status :

INVALID (is red-ish)

licence input : obviously incorrect b64
licence verification : U3ROaW9zZW0xMjM0NTZjb3JyZWN0IGhvcnNlIGJhdHRlcnkgc3RhcGxl
```