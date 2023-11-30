numlist = [i+1 for i in range(int(input("N: ")))]
numlist.remove(1)
j=0
while 1:
    for i in numlist:
        if i > numlist[j] and i % numlist[j] == 0:
            numlist.remove(i)
    j += 1
    try:
        a = numlist[j]
    except:
        break
print(numlist)
