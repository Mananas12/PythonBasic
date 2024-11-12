# Հայտարարել երկու set: Տպել դրանց միավորումը, հատումը, սիմետրիկ տարբերությունը:

set1 = {1, 2, 3, 4, 5, 8}
set2 = {11, 34, 1, 2, 5}

miavorum = set1 | set2
hatum = set1 - set2
simetrik = miavorum - hatum

print(miavorum)
print(hatum)
print(simetrik)