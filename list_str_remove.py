# Հայտարարել list,  list-ից հեռացնել այն list-երը, 
# որոնք պարունակում են գոնե 1 string։

ls = [1, [], [1,2], ['barev'], [1,'a']]

ls = [i for i in ls if not (isinstance(i, list) and any(isinstance(x, str) for x in i))]

print(ls)