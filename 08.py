def f(n):
    ost = ''

    while n != 0:
        ost += str(n % 4)
        n = n // 4

    return ost[::-1]
count = 0
for n in range(300):
    n4 = f(n)
    if len(n4) == 4:
        for i in range(len(n4)):
            if n4.count(n4[i]) > 1:
                count += 1
                break

print(count)