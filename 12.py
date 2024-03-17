for n in range(51, 57):

    s = '0' + '1' * 100 + ('2' * n) + '0'

    while '00' not in s:
        
            s = s.replace('02', '101', 1)
        
            s = s.replace('11', '2', 1)
        
            s = s.replace('012', '30', 1)
        
            s = s.replace('010', '00', 1)

    summ = count = 0
    summ = s.count('3') * 3 + s.count('2') * 2 + s.count('1')
    if summ % 2 != 0:

        for i in range(2, summ):
            if summ % i == 0:
                count += 1
        if count == 0:
            print(summ)
            print(n)