# Python Object Oriented Programming by Joe Marini course example
# Basic class definitions


# TODO: create a basic class
class Book:
  def __init__(self,title):
    self.title = title

# TODO: create instances of the class
book1 = Book("Wings of fire")

# TODO: print the class and property
print(f'Object', book1)
print('title : ', book1.title)