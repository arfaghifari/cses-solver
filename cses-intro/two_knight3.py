import math
 
n = int(input())
 
def is_valid_field(bx,by,dimx,dimy):
    if bx < 1 or by <1 or bx>dimx or by>dimy:
        return False
    return True
 
 
 
 
def count_not_valid(ax, ay,dimx,dimy):
    counter = 0
    counter += is_valid_field(ax-1,ay-2,dimx,dimy)
    counter += is_valid_field(ax+1,ay-2,dimx,dimy)
    counter += is_valid_field(ax-1,ay+2,dimx,dimy)
    # counter += is_valid_field(ax+1,ay+2,dimx,dimy)
 
    counter += is_valid_field(ax-2,ay-1,dimx,dimy)
    counter += is_valid_field(ax+2,ay-1,dimx,dimy)
    counter += is_valid_field(ax-2,ay+1,dimx,dimy)
    # counter += is_valid_field(ax+2,ay+1,dimx,dimy)
    return counter
    
 
 
 
# def find_result(k):
#     counter = 0
#     for i in range(1,k+1):  
#         for j in range(1, k+1):
#             ax = i
#             ay = j
#             counter += count_not_valid(ax,ay,k)
#     return  counter//2
 
counter = 0
for i in range(1, n+1):
    for j in range(1,i+1):
        ax, ay = i,j
        counter += count_not_valid(ax,ay,i,i)
 
    for j in range(1, i):
        a2x,a2y = j,i
        counter += count_not_valid(a2x,a2y,i-1,i)
    print(math.comb(i**2,2),counter)