def sumToOne(num):
    num = str(num)
    add = 0
    for i in range(len(num)):
        add += int(num[i])
    return add


result = sumToOne(928)
print(result)


def isPrime(num):
    count = 0
    for i in range(1, num):
        if i % num == 0:
            count += 1
        if count > 0:
            return str(num) + " is not a prime number"
        else:
            return str(num) + " is a prime number"


result = isPrime(13)
print(result)