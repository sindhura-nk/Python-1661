'''
This module calculates fibionacci numbers for N series
'''
def fibonacci(n):
    a,b=0,1
    for _ in range(n):
        yield a
        a,b = b,a+b
