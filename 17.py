f = [int(i) for i in open('17-370.txt')]
ms = count = g = 0
mx = -100000000
for i in f:
    summ = 0
    if 99 < i < 1000:
        for j in str(i):
            summ += int(j)

        if summ % 10 == 3:
            ms = max(ms, i)

for i in range(1, len(f) - 1):
    count1 = count2 = count3 = 0
    if 999 < abs(f[i-1]) < 10000:
        
        count1 = 1
    if 999 < abs(f[i]) < 10000:
        
        count2 = 1
    if 999 < abs(f[i+1]) < 10000:
        
        count3 = 1

    c1 = count1 + count2
    c2 = count2 + count3

    if c1 == 1:
        s = (f[i - 1] ** 2) + (f[i] ** 2)
        
        if s % ms == 0:
            count += 1
            mx = max(mx, s)
        if g == 1:
            count = count - 1
            g = 0


    if c2 == 1:
        s = (f[i + 1] ** 2) + (f[i] ** 2)
    
        if s % ms == 0:
            mx = max(mx, s)     
            count += 1
            g = 1

print(count, mx)