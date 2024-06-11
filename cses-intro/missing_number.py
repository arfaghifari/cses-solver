n = int(input())
my_arr = list(map(int,input().split()))
print(((n+1)*n//2) - sum(my_arr))