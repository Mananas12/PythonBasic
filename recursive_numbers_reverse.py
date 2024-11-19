#Գրել ռեկուրսիվ ֆունկցիա, որը ստանում է n բնական թիվ և տպում է 0-ից n թվերը։

def numbers(n):
    
    if n < 0:
        return
    numbers(n - 1)  
    print(n) 

numbers(12)