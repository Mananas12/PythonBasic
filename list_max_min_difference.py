# Գրեք ծրագիր, որը օգտվողին թույլ կտա մուտքագրել ամբողջ թվային 
# զանգվածի էլեմենտների արժեքները և  կգտնի զանգվածի ամենամեծ և 
# ամենափոքր տարրերի ինդեքսների տարբերությունը:

ls = []
# ls = map(int,input("Enter the list elements by seperated by space: ").split())

count_elem = int(input("Please input count of elements in list: "))
for i in range(count_elem):
    ls.append(int(input("Enter the value: ")))

min_in = ls.index(min(ls))
max_in = ls.index(max(ls))

print(ls)
print(min_in)
print(max_in)
print(max_in - min_in)