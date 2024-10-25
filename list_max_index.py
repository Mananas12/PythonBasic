ls = [1, 2, 3, 4, 55, 6, 7, 8, 9]

min = ls[0]

for i in ls:
  if i < min:
    min = i

index = ls.index(max)

print(f"Index of the maximum element in list {index}")