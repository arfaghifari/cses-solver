# FAILED

n = int(input())

line = list(n * '0')
final_line = list('1' +( 1 + ((n-1)* '1')))
while (line != final_line):
    print(''.join(line))
    index_change = n-1
    while line[index_change] != '0' and index_change > 0:
        line[index_change] = '0'
        index_change -=1
    if line[index_change] == '0':
        line[index_change] = '1'


print(''.join(final_line))


# 0000
# 0001
# 0011
# 0010

# 0100
# 0101
# 0111
# 0110

# 0110
# 0111
# 0101
# 0100

# 1100
# 1110
# 1111
# 111
# 0111
# 0101
# 0100
