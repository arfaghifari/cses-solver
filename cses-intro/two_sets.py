def append_md4(sets1, sets2, start, finish):
    while start < finish:
        sets1.append(start)
        sets1.append(finish)
        start +=1
        finish -=1
        sets2.append(start)
        sets2.append(finish)
        start +=1
        finish -=1
    

sets1 =[]
sets2 =[]
n = int(input())

md = n%4

if md == 0:
    append_md4(sets1,sets2,1,n)
elif md == 3:
    sets1.append(1)
    sets1.append(2)
    sets2.append(3)
    append_md4(sets1,sets2,4,n)

if len(sets1) == 0 :
    print("NO")
else:
    print("YES")
    print(len(sets1))
    print(" ".join([str(x)  for x in sets1]))
    print(len(sets2))
    print(" ".join([str(x)  for x in sets2]))
