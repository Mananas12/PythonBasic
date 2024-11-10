# Հայտարարել ամբողջ թվային արժեքներով list: 
# Առանձնացնել այդ զանգվածից կենտ և զույգ թվերից բաղկացած ենթազանգվածները։

ls = [1, 2, 3, 4, 5, 6, 7, 8, 9]

even = [i for i in ls if i % 2 == 0]
odd = [i for i in ls if i % 2 != 0]

ls = [even,odd]

# ls = []
# ls.append(even)
# ls.append(odd)

print(ls)