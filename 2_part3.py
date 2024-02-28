listA = list(range(1,11))
listB = list(range(20,31))
def newList(listA, listB):
    for i in listA:
       if i % 2 == 0:
           listA.remove(i)
    for i in listB:
       if i % 2 == 0:
           listB.remove(i)
    return listA + listB
print(newList(listA,listB))

#I originally thought about removing the
#even numbers, but was unsure if there was
#a function to remove these, so I went online
#to look up the syntax

#for i in listA:
#    if i % 2 == 0:
#       listA.remove(i)
#print(listA)