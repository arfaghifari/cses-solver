line = input()
my_map =[0 for _ in range(26)]

for c in line:
    my_map[ord(c)-ord("A")] +=1

new_line = ""
valid = True
flag_num = 0
flag = ""
for i, x in enumerate(my_map):
    if x%2 != 0 and flag_num ==0:
        flag = i
        flag_num = x
    elif x%2 != 0 and flag_num> 0:
        valid = False
        break
    else:
        new_line += x//2 * (chr(i +ord("A")))

if valid and flag_num >0:
    new_line += flag_num*(chr(flag +ord("A")))

if valid:
    for i in range(25, -1, -1):
        if i == flag:
            continue
        new_line += my_map[i]//2 * (chr(i +ord("A")))
    print(new_line)
else:
    print("NO SOLUTION")
