# Licence Manager
The licence manager is a test repo, whiwh hopefully one day could verify licences for projects.
Currently, it only works by taking a name, licence code and passphrase and putting them together like this :
    NameLicencecodePassphrase

and Base64-ing the whole of it.

example
Name = StNiosem
Licence Code = 123456
Passphase = correct horse battery staple

outputs
b'U3ROaW9zZW0xMjM0NTZjb3JyZWN0IGhvcnNlIGJhdHRlcnkgc3RhcGxl'

The licence verifyer works by asking the licence, and asking name, licence and passphrase. 
It generates the licence using the provided info and compares it to the inputted licence. 
If it matches it outputs 'VALID' in green, if it does not it outputs 'INVALID' in red-ish orange