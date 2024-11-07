#5.Հայտարարել list,  որը բաղկացած է string-ներից: 
#Տպել թե քանի անգամ է յուրաքանչյուրը հանդիպում list-ում: 

ls = ['barev', 'hello', 'hola', 'barev', 'barev', 'hola']

for i in range(len(ls)):
    count = 0  
    for j in range(i , len(ls)):
        if ls[i] == ls[j]:
            count += 1
#sxal ka
    print(f"{ls[i]} - {count} ")

