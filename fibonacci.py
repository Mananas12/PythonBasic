# Իրականացնել ֆունկցիա, որը ստանում է ամբողջ թվային պարամետր և 
# վերադարձնում է n-րդ Ֆիբոնաչիի թիվը։

def fib(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

n = 0
print(fib(n))
