from sys import setrecursionlimit

setrecursionlimit(30000)

def f(curr, end):
    if curr > end:  return 0
    if curr == end: return 1
    if curr < end:  return f(curr + 2, end) + f(curr + 4, end) + f(curr + 5, end)



for n in range(31, 3000):
    if f(31, n) == 1001:
        print(n)
