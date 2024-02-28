#outerList = [
#    [1,2,3,4,5]
#    [6,7,8,9,10]
#    [11,12,13,14,15]
#    [16,17,18,19,20]
#    [21,22,23,24,25]
#]
#print(myList) 

outerList = []
for i in range(5):
    innerList = []
    for j in range(1,6):
        innerList.append(j+i*5)
    outerList.append(innerList)
print(outerList)

#I was able to reason that I wanted to iterate
#through an outer list 5 times (once for each
#list element) and 5 times for each inner list
#(because of there being 5 elements in each inner
#list). I kept trying to add 1 each time I went
#through the inner list iteration, and then add
#1 when I got through each outerlist iteration,
#but I kept getting the same [1,2,3,4,5] for 
#every inner list and could not add to these
#exisiting lists (the items all had the same value).
#I went to office hours and got help. We found that
#I could implement the for loop for the outer list
#into the inner list by using 'i' in my append statement.