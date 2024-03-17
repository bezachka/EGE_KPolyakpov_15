for x in range(1, 17):
    f1 = int(f'12346{x}17', 17)
    f2 = int(f'7{x}171', 17)
    f = f1 + f2
    if f % 16 == 0:
        print(f // 16)