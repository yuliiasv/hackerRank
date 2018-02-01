firstList = list(range(5))
secondList = list(range(6))

sumList = sum(firstList)
sumList2 = sum(secondList)
print(sumList2-sumList)

for i in firstList: #[0,1,2,3,4] i =0
    for j in secondList:#[0,1,2,3,4,5] j =0
        if i == j:
            i = i + 1
        else:
            print (j)
            
