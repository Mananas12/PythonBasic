num = int(input("Please enter the number for check: "))

count = 1
sum = 0

while count <= num/2:
  if num % count == 0:
    sum += count 
  count += 1

if sum == num:
  print("The number is perfect")
else:
  print("The number is not perfect")