# Implement a decorator count_calls that tracks how many times a function has been called. 
# After each call, it should print the current count. Test this on a function that adds two numbers, 
# calling it multiple times

def count_calls(original_foo):
  def inner(*args,**kwargs):
    global count
    count+=1
    print(count)
  return inner

count = 0
@count_calls
def add(num1, num2):
  return num1 + num2

add(1,2)
add(2,3)
add(3,4)
add(4,5)