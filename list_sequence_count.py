# Հայտարարել ամբողջ թվային արժեքներով list: 
# Տպեք էկրանին այն էլեմենտների արժեքները որոնք հանդիպում են հաջորդաբար, 
# տպեք նաև հանդպման քանակը։
# Input : [4, 5, 5, 5, 3, 8]
# Output : 5 -3
# Input : [1, 1, 1, 64, 23, 64, 22, 22, 22, 22]
# Output : 1-3, 22-4

ls = [4, 8, 5, 5, 5, 8, 3, 8, 8, 8, 8]
ls1 = []

for i in range(len(ls)):
    if ls[i] not in ls1:
        count = 1 
        for j in range(i + 1, len(ls)):
            if ls[i] == ls[j]:
                count += 1
            else:
                break
        if count > 1:
            print(f"{ls[i]} - {count}")
            ls1.append(ls[i])
