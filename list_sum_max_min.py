ls = [13, 2, 3, 4, 5, 6, 7, 8, 9]

min = ls[0]

for i in ls:
  if i < min:
    min = i

max = ls[0]

for i in ls:
  if i > max:
    max = i

sum = min + max

print(f"Sum of min and max in list {sum}")