#Հայտարարել ամբողջ թվային արժեքներով list: 
#Վերադարձրեք unique էլեմնտների քանակը։

ls = [1, 13, 2, 1, 4, 5, 5, 7, 2, 10, 9, 5, 24, 43]
unique_count = 0

for i in ls[:]:  
    if ls.count(i) == 1:  
        unique_count += 1
        ls.remove(i)  

print(unique_count)
