n = int(input())
my_arr = list(map(int,input().split()))

count = 0
prev = my_arr[0]
for i in range(1, len(my_arr)):
    if my_arr[i] < prev:
        count += prev - my_arr[i]
    else:
        prev = my_arr[i]
print(count)