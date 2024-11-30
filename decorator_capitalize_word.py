# Implement a decorator capitalize_words that capitalizes the first letter of each word in the string 
# returned by the function. Test it with a function that returns a sentence.

def capitalize_words(orirginal_foo):
  def inner(*args,**kwargs):
    res = orirginal_foo(*args, **kwargs)
    return " ".join(i.title() for i in res.split())
  return inner

@capitalize_words
def sentance(sent):
  return sent

print(sentance("aram amen inch karam"))