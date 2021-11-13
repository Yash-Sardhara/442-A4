from urllib.request import urlopen, hashlib

sha1hash = "E34CDD05DA9262F8F770EAE65E2C1267F3E22CC0"

# LIST_OF_COMMON_PASSWORDS = str(urlopen('https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-1000000.txt').read(), 'utf-8')
higest_bound = pow(2, 128)
for guess in range(0, higest_bound): #LIST_OF_COMMON_PASSWORDS.split('\n'):
    hashedGuess = hashlib.sha1(bytes(guess)).hexdigest()
    if hashedGuess == sha1hash:
        print("The Password is ", str(guess))
        quit()
print("Password not in the database!")