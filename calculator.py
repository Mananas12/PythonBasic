# Table of a Number: Գրել ֆունկցիա, որը կտպի տրված թվի բազմապատկման աղյուսակը։

def calculator(num: int):
    for i in range(10):
        print(f"{num} * {i} = {num * i}")

calculator(3)