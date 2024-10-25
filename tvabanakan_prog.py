count = int(input("Please enter count of list: "))
ls = []
flag = 0
for i in range(count):
  ls.append(int(input()))
#count = len(ls)
#d = ls[1] - ls[0]
#s = (((2 * ls[0]) +((count - 1) * d))/2) * count
print(ls)
for i in range(len(ls) - 2):
  if (int(ls[i + 1]) - int(ls[i])) == (int(ls[i + 2]) - int(ls[i + 1])):
    flag = 1
  else:
    flag = 0
    break

if flag == 1:
  print("tvabanakan e")
else:
  print("tvabanakan che") 
