file = open('24-191.txt')
f = file.readline().replace('A', ' *').replace('B', '& ').split()
count = 0
for i in f:
    if len(i) < 16 and i[0] == '*' and i[-1] == '&':
        if 'F' in i:
            count += 1
            print(i)

print(count)