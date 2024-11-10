# Հայտարարել 2 list(էլեմենտները կարող են լինել կամայական տիպերի):
#  Տպել զանգվածների տարբերությունը։
# Sample data:
# Color1 =  ["red", "orange", "green", "blue", "white"]
# Color2 =  ["black", "yellow", "green", "blue"]
# Expected Output:
# Color1-Color2: ['red','white', 'orange']
# Color2-Color1: ['black', 'yellow']

ls1 = [1, 'abc', 12, (1,2,3)]
ls2 = ['def', 8, 12, (1,2,3)] 

ls = set(ls1) - set(ls2)
print(ls)
ls = set(ls2) - set(ls1)
print(ls)


