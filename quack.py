class Duck:
    def quack(self):
        print('quack')

class Person:
    def quack(self):
        print('I quack like a duck!')

def eee(just):
    just.quack()

x=Duck()

for _ in range(3):
    print(_)

class student:
    def __init__(self,name,age):
        self.name=name 
        self.age=age

    def show_name(self):
        print(self.name)

ishan=student('Ishan',20)
ishan.show_name()
ishan.__init__(33.33,33)
ishan.show_name()
print(type(Duck()))
print(isinstance(x,Duck))