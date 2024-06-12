# 1
# 1
# 1 2 1 end1

# 2
# 3
# 1 2 1 end1
# 1 3 2 
# 2 3 1 end2


# 3
# 7
# 1 2 1 end1
# 1 3 2
# 2 3 1 end2
# 1 2 3 
# 3 1 1
# 3 2 2
# 1 2 1 end3 

# 15
# 7
# 1 2 1 end1
# 1 3 2
# 2 3 1 end2
# 1 2 3 
# 3 1 1
# 3 2 2
# 1 2 1 end3
# 1 3 4
# 2 3 1 
# 2 1 2
# 3 1 1 
# 2 3 3
# 1 2 1
# 1 3 2
# 2 3 1 end4





# 11
# 1 2 1
# 1 3 2
# 2 3 1
# 1 2 
# 3 2
# 3 1
# 2 1
# 3 2
# 1 3
# 1 2
# 3 2

# 3
# 11
# 1 2
# 1 3
# 2 3
# 1 2
# 3 2
# 3 1
# 2 1
# 3 2
# 1 3
# 1 2
# 3 2
# minimum_move = -1
# visited = []



# def is_can_pop(stack1,stack2):
#     if len(stack1) == 0 or len(stack2) == 0:
#         return True
#     else:
#         return stack1[1] < stack2[-1]
    
# def find_minimum_move(counter, curr_comb):
#     global minimum_move
#     if counter >= minimum_move:
#         return
#     if curr_comb in visited:
#         re
    

# high = int(input())
# dest = [[],[],[i for i in range(high)]]
# first_comb = [[i for i in range(high)],[],[]]
# visited.append(curr_comb)



# print(minimum_move)


def move(source, dest, count):
    if count == 1:
        print(str(source) + " " + str(dest))
    else:
        mid = 6 - source - dest
        move(source, mid, count -1)
        move(source,dest,1)
        move(mid, dest, count-1)

n = int(input())
print(2**(n)-1)
move(1,3,n)

