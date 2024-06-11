n =  int(input())
for _ in range(n):
    a, b = map(int, input().split())
    md = (a+b)%3
    dv =(a+b)//3
    if(md == 0 and a>=dv and b>=dv):
        print("YES")
    else:
        print("NO")