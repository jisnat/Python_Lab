class Student:
    def __init__(self,rlno,name):
        self.rlno=rlno
        self.name=name
    def display(self):
        print("roll no: ",self.rlno)
        print("name ",self.name)
stud1=Student(10,"Amritha")
stud1.display()
