class Point:
  #생성자
  def __init__(self,x,y):
    self.x = x
    self.y = y
  def move(self):
    print("move")
  def draw(self):
    print("draw")

# point1 = Point()
# point1.x = 10
# point1.y = 20
# print(point1.x)
# point1.draw()

# point2 = Point()
# point2.x = 10
# point2.y = 20
# print(point2.x)
# point2.draw()

point = Point(10, 20)
print(point.x)

class Person:
  def __init__(self,name):
    self.name = name
  def talk(self):
    print("talk")

hyo = Person('hyo')
print(hyo.name)

tion = Person('tion')
print(tion.name)

#상속
class Mammal:
  def walk(self):
    print("walk")

class Dog(Mammal):
  def bark(self):
    print("bark")

class Cat(Mammal):
  pass
    
dog1 = Dog()
dog1.walk()
dog1.bark()