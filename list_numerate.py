# Գրել  ծրագիր, որը ստեղծում է list համարակալելով տրված զանգվածի էլեմենտները։
# Sample list : ['p', 'q']
# n =5
# Sample Output : ['p1', 'q1', 'p2', 'q2', 'p3', 'q3', 'p4', 'q4', 'p5', 'q5']

ls = ['p', 'q', 't']
ls1 = []
num = int(input("Please input the number: "))

for i in range(1, num + 1):
    for j in range(len(ls)):
        ls1.append(ls[j] + str(i))
print(ls1) 