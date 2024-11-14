k = 1
def factorial(n: int) -> int:
    for i in range(n): 
        global k
        k *= n
        n-=1
    return k
n = 5
factorial(n)
print(k)    