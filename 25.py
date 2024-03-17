from fnmatch import *

pattern = '9?979*8'

for n in range(0, 10**10, 50068):
    if fnmatch(str(n), pat=pattern) and '0' in str(n):
        print(n, n //50068)
