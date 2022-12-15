print('Create a Parent Class')
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname,' and ', self.lastname)

  def __str__(self):
      return f"{self.lastname} and {self.firstname}"

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()
print(x,'\n')

print('Create a Child Class')
class Student(Person):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname)

y = Student("Mike", "Olsen")
y.printname()
print(y,'\n')

class Student_2(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year
  def __str__(self):
      return f"{self.lastname} in {self.graduationyear} and {self.firstname} in {self.graduationyear+3}"
z = Student_2("Pavel", "Petr", 2019)
print(z,'\n')