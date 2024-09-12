#create class dog
class Dog:
    def __init__(self, name):
        self.name = name
         
    def bark(self):
        print("bark")
 #you can create as many functions as you want in a class
     def add_one(self, x):
         return x + 1

#create an instance 
d  = Dog()

d.bark()
print(d.add_one(5))
print(type(d))
