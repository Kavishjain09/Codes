class Student():
    def __init__(self,v1,v2):
        self.m1 = v1
        self.m2 = v2
        print(self.m1+self.m2)
    def __add__(self,other):
        s1=self.m1+ other.m1
        s2=self.m2+ other.m2
        s3=Student(s1,s2)
        return s3

Obj1=Student(12,56)
Obj2=Student(10,30)
s3=Obj1+Obj2
print(s3.m1,s3.m2)
