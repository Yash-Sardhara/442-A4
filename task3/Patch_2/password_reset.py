from Crypto.Hash import SHA1

new_password = input("Please input a new password: ")
new_hash = SHA1.new()
new_hash.update(new_password.encode('utf-8'))
print(new_hash.hexdigest())
with open("60312485.program2.exe", "r+b") as f:
    f.seek(119810)
    f.write(new_hash.digest())
    f.close
    print("Done: password reset!")