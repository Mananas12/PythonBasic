# Իրականացնել shuffle(list)  ֆունկցիային համարժեք ֆունկցիա, 
# այն խառնում է list-ի էլեմենտները։

import random

def shuffle_(ls):
    n = len(ls)
    for i in range(n):
        j = random.randint(0, n-1)
        ls[i], ls[j] = ls[j], ls[i]
       
list = [1, 2, 3, 4, 5, 6]
shuffle_(list)
print(list)
