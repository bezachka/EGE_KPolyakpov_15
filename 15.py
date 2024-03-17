count = 0
for a in range(1, 300):
    flag = 1
    for x in range(1, 300):
        f = (x % 12 == 0) and (70 <= x <= 80) and (not(x % a == 0))

        if f == True:
            flag = 0
            break

    if flag == 1:
        count += 1

print(count)
