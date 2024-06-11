n = int(input())
div_factor = 5
count = 0
while n >= div_factor:
    count += n//div_factor
    div_factor *=5
print(count)