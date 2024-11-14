# Իրականացնել ֆունկցիա, որն ընդունում է թիվ և 
# վերադարձնում նրա թվանշանների գումարը:

sum = 0
def number(num : int)-> int:
    for i in range(len(str(num))):
        global sum
        sum = sum + (num % 10)
        num //= 10
    return sum

print(number(123))
