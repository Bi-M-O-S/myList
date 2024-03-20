myList = []
myList.append(10)
myList.append(20)
myList.append(30)
myList.append(40)

myList[1] = 15
anotherList = [50,60,70]
myList.extend(anotherList)
myList.pop()
myList.sort()
print(myList.index(30))