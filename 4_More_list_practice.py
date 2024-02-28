myList = []
n = int(input("Enter a number of elements: "))
for i in range(n):
    element = int(input("Enter an element: "))
    myList.append(element)
print(myList)
#I just wanted to have users have the freedom
#of creating their own list

def removeDuplicates(myList):
    result = []
    j=0
    while j <= len(myList):
        for k in myList:
            if k not in result:
                result.append(k)
        j = j + 1
    return result
print(removeDuplicates(myList))

#I knew I wanted to use a for loop in order
#to check if an element value already existed
#in myList. I originally ran this without a
#while loop and found that I would only get
#the first element I entered because it was
#not in my results, so the loop ended.
#Therefore, by adding a while loop, I could
#keep going through the entire course of
#myList.