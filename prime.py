# 7.Իրականացնել ֆունկցիա, որը ստուգում է՝ թիվը պարզ է, թե ոչ։ 
# Պարզ է համարվում այն թիվը, որը առանց մնացորդ կարող է բաժանվել ինքը իր վրա և 
# մեկի վրա (մեկը պարզ թիվ չէ)։

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

n = 11
if is_prime(n):
    print("Prime")
else:
    print("None prime")
