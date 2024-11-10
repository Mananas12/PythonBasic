#.Հայտարարել list,  list-ից հեռացնել բոլոր դատարկ list-երը։

ls = [1, [], 'wood', [1,2,3], []]

for i in ls:
    if i == []:
        ls.remove(i)

print(ls)