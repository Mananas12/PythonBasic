# Create a decorator double_result that modifies the return value of a function by doubling it. 
# Apply this decorator to a function that returns a number and verify that the result is doubled.

def double_result(original_foo):
  def inner(*args, **kwargs):
    res = original_foo(*args,**kwargs)
    return res*2
  return inner

@double_result
def foo(num):
  return num

print(foo(5))