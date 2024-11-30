# Implement a memoization decorator memoize that caches the results of a function to improve performance. 
# Apply this decorator to a recursive function that computes the Fibonacci sequence. 
# Demonstrate the speed improvement by calling the decorated function multiple times.

from time import time

def memoize(original_foo):
  cache = {}
  def inner(*args, **kwargs):
    keys = (args, tuple(kwargs.values()))
    if keys in cache:
       return cache[keys]
    cache[keys] = original_foo(*args, **kwargs)
    print(cache)
    return cache[keys]
  return inner

@memoize
def fib_mem(n):
  if n < 2:
    return 1
  return fib(n - 1) + fib(n - 2)

# @memoize
# def fib_helper(n):
#   return fib_mem(n)

def fib(n):
  if n < 2:
    return 1
  return fib(n - 1) + fib(n - 2)

start = time()
print(f"fib = {fib_mem(20)}")
end = time()
print(f"{(end - start):.5f}")

start = time()
print(f"fib = {fib(30)}")
end = time()
print(f"{(end - start):.5f}")

start = time()
print(f"fib = {fib_mem(30)}")
end = time()
print(f"{(end - start):.5f}")


