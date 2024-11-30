# Implement a decorator time_it that measures the time taken by a function to execute and prints it. 
# Apply this decorator to a function that calculates the sum of squares of numbers from 1 to 1000.

from time import time
from functools import wraps

def time_it(original_foo):
  @wraps(original_foo)
  def inner(*args, **kwargs):
      start = time()
      res = original_foo(*args, **kwargs)
      end = time() - start
      print("Time: %.6f" % end)
      print(res)
      return res
  return inner

@time_it

#with for
# def sum_(n):
#   ls = []
#   for i in range(1, n + 1):
#     ls.append(i**2)
#   return sum(ls)

# with comprehension
def sum_(n):
   return sum(i**2 for i in range(1, n + 1))
   
sum_(1000)
