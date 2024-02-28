#using part 1
outerList = []
for i in range(5):
    innerList = []
    for j in range(1,6):
        innerList.append(j+i*5)
    for k in range(len(innerList)):
        if innerList[k] % 3 == 0:
            innerList[k] = "?"
    outerList.append(innerList)
print(outerList)

#For this problem, the main problem was syntax.
#I understood that I wanted to find multiples
#of 3 in each of my inner lists, so I used a
#modulus statement. Mainly, knowing where to put
#it and how to write it took some trial and error.
#I reasoned that I wanted to create a statement
#after making the inner list for each iteration
#that would find the multiples of 3 and change them.
#I kept trying to use 'for k in innerList:' to access
#the values at each spot, but weirdly found that
#nothing happened with this approach. I then recalled
#our work with lists and decided to go through each
#element spot, access its value, then change the value
#(instead of doing one less step like before).

#for k in range(len(outerList)):
#    for l in range(len(outerList[k])):
#        if outerList[k][l] % 3 == 0:
#            outerList[k][l] == "?"
#print(outerList)