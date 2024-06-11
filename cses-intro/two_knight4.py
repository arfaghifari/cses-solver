

n = int(input())

def comb2(n):
    return (n * (n-1))//2



count = 0

for i in range(1, n+1):
    print(comb2(i**2)- count)
    count += 8 * (i-1)