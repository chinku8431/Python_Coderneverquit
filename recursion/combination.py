def combination(mylist,r):
    if r == 0:
        return [[]]
    L = []
    for i in range(0,len(mylist)):    
        first = mylist[i]
        rem = mylist[i+1:]
        combList = combination(rem,r-1)
        for x in combList:
            L.append([first]+x)
    return L        


print(combination(["A","B","C","D"],3))