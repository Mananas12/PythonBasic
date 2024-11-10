# Հայտարարել string-երից կազմված list, 
# տպել ըստ string-երի երկարության սորտավորված զանգվածը(և՛ աճման կարգով, և՛ նվազման)։

ls = ['mek', 'erku', 'ereq', 'chors']

ls = sorted(ls, key = len)
print(f"in ascending order {ls}")
ls = sorted(ls, key = len, reverse = True)
print(f"in descending order {ls}")

