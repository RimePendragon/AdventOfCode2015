import hashlib

key = "ckczppom"

index = 0
found = False
while found is False:
    index += 1
    testString = key + str(index)
    result = hashlib.md5(testString.encode()).hexdigest()
    if result[0:5] == "000000":
        found = True


print(index)

