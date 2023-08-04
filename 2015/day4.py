import hashlib
select = input("1 or 2: ")

if select == "1":
    i = 0
    while True:
        input = 'ckczppom' + str(i)
        j = hashlib.md5(input.encode()).hexdigest()
        if j[:6] == '000000':
            print('md5 result: ' + j)
            print('first number with 5 zeroes: ' + str(i))
            break
        i += 1