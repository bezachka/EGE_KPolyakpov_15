def f(n):
    ost = ''

    while n != 0:
        ost += str(n % 3)
        n = n // 3

    return ost[::-1]

for n in range(300):
    n3 = f(n)
    summ = 0
    for i in n3:
        summ += int(i)

    if summ % 3 == 0:
        n3 = '20' + n3

    if summ % 3 != 0:
        n3 = '10' + n3

    r = int(n3, 3)
    if r < 100:
        print(n)
