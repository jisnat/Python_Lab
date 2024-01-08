class Rectangle:
    def __init__(self,length,breadth):
        self.__length=length
        self.__breadth=breadth
    def get_length(self):
        return self.__length
    def get_breadth(self):
        return self.__breadth
    def area(self):
        return self.get_length()*self.get_breadth()
    def __lt__(self,ob):
        if(self.area()<ob.area()):
            return "First rectangle is small"
        else:
            return "Second rectangle is small"

l1=int(input("Enter length 1 : "))
b1=int(input("Enter breadth 1 : "))
ar1=Rectangle(l1,b1)
l2=int(input("Enter length 2 : "))
b2=int(input("Enter breadth 2 : "))
ar2=Rectangle(l2,b2)

print("Area of the rectangle 1 is ",ar1.area())
print("Area of the rectangle 2 is ",ar2.area())

comparison_result = ar1 < ar2
print(comparison_result)
