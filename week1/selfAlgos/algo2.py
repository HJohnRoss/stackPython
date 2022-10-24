def zipIt(list1, list2):
    newList = []
    for i in range(len(list1)):
        newList.append(list1[i])
    for x in range(len(list2)):
        newList.append(list2[x])
    return newList


result = zipIt([1, 2], [10, 20, 30, 40])
print(result)


def listReverse(list):
    newList = []
    for i in range(len(list), -1, -1):
        newList.append(list[i])
    return newList


result = listReverse([10, 20, 30, 40])
print(result)
