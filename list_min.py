ls = [3, 2.1, 1.23, 4.2, 5, 6.3, 7, 8.4, 9]

min = ls[0]

for i in ls:
  if i < min:
    min = i

print(f"The minimum number is {min}")