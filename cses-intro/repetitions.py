my_arr = input()

max_count = 1
count = 1
prev = my_arr[0]
for i in range(1, len(my_arr)):
    if my_arr[i] == prev:
        count += 1
        if count > max_count:
            max_count = count
    else:
        prev = my_arr[i]
        count = 1
print(max_count)