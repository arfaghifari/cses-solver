n = int(input())


def not_valid(ax, ay, bx, by):
    if abs(bx-ax) == 2 and abs(by-ay) ==1:
        return True
    if abs(bx-ax) == 1 and abs(by-ay) ==2:
        return True
    return False


def find_result(k):
    counter = 0
    for i in range(1,k+1):
        for j in range(1, k+1):
            ax = i
            ay = j
            for l in range(1, k+1):
                for m in range(1, k+1):
                    if i == l and j==m:
                        continue
                    bx = l
                    by = m
                    if not not_valid(ax,ay,bx,by):
                        counter +=1
            # print("counter", counter)
    return counter//2


for k in range(1,n+1):
    print(find_result(k))

# print("res", find_result(2))