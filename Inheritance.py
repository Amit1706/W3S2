class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()

class Cars:
  def __init__(self, model, brand) :
    self.firstname = model
    self.lastname = brand

  def printname(self):
    print(self.lastname, self.firstname)  
y = Cars("ZS", "MG")    
y.printname()

# Create a child class
class BMW(Cars):
z = BMW("325", "i")
z.printname()
