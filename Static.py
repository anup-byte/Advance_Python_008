class Student:
    passingPercentage = 40
    
    def studentDetails(self):
        self.name = "Anup"
        print("Name : ", self.name)
        self.percentage = 75
        print("Percentage : ", self.percentage)
        
    
    def isPassed(self):
        if self.percentage > Student.passingPercentage:
            print("Student is passed")
            
        else:
            print("Student is not passed")
            
            
    @staticmethod
    def welcomeToSchool():
        print("Welcome to AI KI PATHSHALA")

s1 = Student()
print()
s1.studentDetails()
print()
Student.studentDetails(s1)
print()
s1.isPassed()
print()
s1.welcomeToSchool()
print()
Student.welcomeToSchool()


