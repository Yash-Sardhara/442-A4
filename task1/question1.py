from Crypto.Hash import SHA256

COURSE_NAME = "CPEN 442 Coin"
COURSE_YEAR = "2021"
HASH_OF_PRECEDING_COIN = "a9c1ae3f4fc29d0be9113a42090a5ef9fdef93f5ec4777a008873972e60bb532"
STUDENT_ID = "60312485"

id_of_miner = SHA256.new(data=STUDENT_ID.encode()).hexdigest()
print(id_of_miner)
upper_bound = pow(2, 256)
for i in range(0, upper_bound):
    coin_blob = str(i.to_bytes(4, 'big'))
    sha256_hash_code = SHA256.new(data=(COURSE_NAME + COURSE_YEAR + HASH_OF_PRECEDING_COIN + coin_blob + id_of_miner).encode()).hexdigest()
    if sha256_hash_code[0:8] == "00000000":
        print("Miner ID: {}".format(id_of_miner))
        print("Coin Blob: {}".format(coin_blob))
        print("Hash Code: {}".format(sha256_hash_code))
        break
