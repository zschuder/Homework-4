myList = list(range(0,51)) #From part 1
result = []
def square(myList, result):
    for i in myList:
        result.append(i**2)
    print(result)
print(square(myList, result))
#I like this approach better because I am not
#fundamentally changing the original list. I
#am creating a new list instead.

#I did not run into many mistakes here.

#def square(myList):
#    for i in range(len(myList)):
#        myList[i] = myList[i]**2
#    return myList
#print(square(myList))