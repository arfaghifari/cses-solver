def num_spiral(x,y):
    res = 0
    if x >= y and x%2 == 0:
        res = (x)**2 -y +1
    elif x >= y and x%2 == 1:
        res = (x-1)**2 +y
    elif y> x and y%2 == 0:
        res = (y-1)**2 +x
    else:
        res = (y**2) - x +1


    print(res)

t = int(input())
for _ in range(t):
    x, y = map(int,input().split())
    num_spiral(x,y)