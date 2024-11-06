from  math import  pi
class Figure:
    def __init__(self): #p=(a+b+c)/2 sqrt(p*(p-a)*(p-b)*(p-c))
        pass

    def calc_area(self):
        pass

class Triangle(Figure):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def calc_area(self):
        p = (self.a + self.b + self.c) / 2
        return (p*(p-self.a)*(p-self.b)*(p-self.c))**0.5

class Circle(Figure):
    def __init__(self,radius):
        self.radius=radius
    def calc_area(self):
        return

My_triangle = Triangle(3,4,5)
print(My_triangle.calc_area())

class Triangle(Figure):
    def __init__(self, a, b, c,):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
    def calc_area(self):
        p = (self.a + self.b + self.c+self.d) / 2
        return (p*(p-self.a)*(p-self.b)*(p-self.c))**0.5


