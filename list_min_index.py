ls = [1, 2, 3, 4, 0, 6, 7, 8, 9]

min = ls[0]

for i in ls:
  if i < min:
    min = i

index = ls.index(min)

print(f"Index of the minimum element in list {index}")