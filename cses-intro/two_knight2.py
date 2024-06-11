n = int(input())
 
 
 
def is_valid_field(bx,by,dim):
    if bx < 1 or by <1 or bx>dim or by>dim:
        return False
    return True
 
 
 
 
def count_not_valid(ax, ay,k):
    counter = 0
    counter += is_valid_field(ax-1,ay-2,k)
    counter += is_valid_field(ax+1,ay-2,k)
    counter += is_valid_field(ax-1,ay+2,k)
    counter += is_valid_field(ax+1,ay+2,k)
 
    counter += is_valid_field(ax-2,ay-1,k)
    counter += is_valid_field(ax+2,ay-1,k)
    counter += is_valid_field(ax-2,ay+1,k)
    counter += is_valid_field(ax+2,ay+1,k)
    return counter
    
 
 
 
def find_result(k):
    counter = 0
    for i in range(1,k+1):  
        for j in range(1, k+1):
            ax = i
            ay = j
            res = count_not_valid(ax,ay,k)
            # print(res, "res")
            counter +=  k**2 - 1 - res
            # print("counter", counter)
    return  counter//2
 
 
for k in range(1,n+1):
    print(find_result(k))