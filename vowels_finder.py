str = input("Please input the string ")
count = 0
i = 0
#a, e, i, o, u
while i < len(str):
  if ((str[i] == 'a') or (str[i] == 'e') or (str[i] == 'i') or (str[i] == 'o') or (str[i] == 'u')):
    count += 1
  i += 1

print(count)


