# 1

def countdown(num):
    list = []
    for num in range(num, -1, -1):
        list.append(num)
    return list


newList = countdown(5)
print(newList)

# 2


def printReturn(list):
    print(list[0])
    return list[1]


newList = printReturn([1, 2])
print(newList)

# 3


def firstPlusLength(list):
    for i in range(len(list)):
        print(list[i])


firstPlusLength([1, 2, 3, 4, 5])


# 4


def greaterThanSecond(list):
    newList = []
    for i in range(len(list)):
        if list[i] > list[1]:
            newList.append(list[i])
    return newList


result = greaterThanSecond([5, 2, 3, 2, 1, 4])
print(result)

# 5


def length_and_value(size, value):
    newList = []
    for i in range(size):
        newList.append(value)
    return newList

result = length_and_value(4, 7)
print(result)