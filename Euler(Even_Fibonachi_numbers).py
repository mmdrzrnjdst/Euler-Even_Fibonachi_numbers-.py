def IsEven(n):
    if n % 2 == 0:
        return True
    else:
        return False


first = 1
seccond = 2
sum = 0

while (first < 4*10**6):
    # print('my first number is', first)
    if IsEven(first):
        # print('oh it is even')
        sum = sum + first
        # print('-------------> now the sum is', sum)
    new = first + seccond
    first = seccond
    seccond = new


print(sum)
