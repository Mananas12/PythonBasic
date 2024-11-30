# Implement a decorator repeat(times) that repeats the execution of a function a specified number of times. 
# Apply it to a function that prints a message, and test it with different values of times.

def repeat(count):
  def outer(original_foo):
    def inner(*args, **kwargs):
      for i in range(count):
        original_foo(*args,**kwargs)
    return inner
  return outer

count = 3
@repeat(count)
def foo():
  print("Hello world")

foo()