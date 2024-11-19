#Գրել ռեկուրսիվ ֆունկցիա, որը ստանում է n բնական թիվ և տպում է n-ից 0 թվերը։

def numbers(n):
    
    if n < 0:
        return
    print(n)
    numbers(n - 1)

numbers(10)
