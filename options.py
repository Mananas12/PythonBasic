print("Please enter two numbers")
x = int(input("First number "))
y = int(input("Second number "))
#|x - y| / x + y
num = abs(x - y) / (x + y)
print(f"The answer is {num}")