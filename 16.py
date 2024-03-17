f = [0] * 23025
for i in range(23024):
    if i > 2:
        f[i] = f[i - 2] + i

    if i <= 2:
        f[i] = 5

print(f[23023])