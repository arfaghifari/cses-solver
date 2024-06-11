n = int(input())
if n == 1:
    print(n)
elif 1 < n < 4:
    print("NO SOLUTION")
else:
    mid = n//2 +1
    md = n%2

    print(mid, end ="")
    if  md == 1:
        for i in range(mid-1):
            print(" "+ str(i+1) +" " +str(n-i), end= "")
        print()

    if md == 0:
        for i in range(mid-2):
            print(" " + str(i+1) +" " +str(n-i), end= "")
        print("", str(mid-1))

