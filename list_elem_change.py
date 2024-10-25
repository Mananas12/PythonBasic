ls = [1, 2, 3, 4, 5, 6, 7, 8, 9]

count = len(ls)

for i in range(len(ls)):
  ls[i] /= count

print(f"The new list is {ls}")