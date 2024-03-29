class Student1:
    rollno=int(input("Enter the Rollno. :- "))
    name=input("Enter the name of the student: ")
    percentage=input("Enter the percentage of the Student: ")
    print(f"The nmae  of the Student is {name} and the roll no. is {rollno}. {name} gained the {percentage} percentage")

stud1=Student1()   


class Student:
    def __init__(self):
        self.rollno = int(input("Enter the Roll no. of the student: "))
        self.marks = []
        self.total_marks = 0
        
        for i in range(5):
            sub = int(input(f"Enter the marks out of 100 marks of the subject {i+1}: "))
            self.marks.append(sub)
            self.total_marks += sub
    
    def percentage(self):
        per = (self.total_marks / 500) * 100
        return per

stud = Student()
print("Percentage:", stud.percentage(),"%")