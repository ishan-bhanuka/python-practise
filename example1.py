class example:
    name_count=0
    
    def __init__(self,name):
        self.name=name
        self.__class__.name_count+=1
        
x=[]

e1=example('ishan')
e2=example('bhanuka')
e3=example('amal')
print(example.name_count)
names=[32,36,7,4,3,34,34]
print(names)
print(len(names))
for i in range(4):
    x.append(i)
print(x)
name='ishan bhanuka'
y=list(x)
y.append(45243)
print(x,y)