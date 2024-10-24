year = int(input("Please enter the year for check "))

if (((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0)):
  print("Nahanj e")
else:
  print("Nahanj che")

