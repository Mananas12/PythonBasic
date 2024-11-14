# Իրականացնել int տիպի արժեք վերադարձնող ֆունկցիա, որը վերադարձնում է՝ 1, 
# եթե ֆունկցային փոխանցված ամբողջ թիվը կարող է արտահայտվել երկու պարզ թվերի գումարով, 
# հակառակ դեպքում ֆունկցիան կվերադարձնի՝ 0:

def is_prime(n: int)-> bool:
    if n <= 1:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

def checker(num: int)-> int:
    for i in range(1,num):
        if is_prime(i) and is_prime(num - i):
            return 1
    else:
        return 0
    
print(checker(2))