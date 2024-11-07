num = int(input("Plese enter the number for check "))

ls = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in ls:
    if i == num:
        print("YES")
        exit()

print("NO")
