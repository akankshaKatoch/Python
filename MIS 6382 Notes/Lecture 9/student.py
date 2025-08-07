class StudentComposition:
	def __init__(self,id, n, gpa, fac_name, fac_title):
		self.__stu_id = id
		self.__stu_name = n
		self.__stu_gpa = gpa
		self.__stu_advisor = Fac(fac_name, fac_title) #  Here we create the Faculty object inside the __init__ method

class StudentAggregation:
	def __init__(self,id, n, gpa, fac):
		self.__stu_id = id
		self.__stu_name = n
		self.__stu_gpa = gpa
		self.__stu_advisor = fac #Note the variable fac is an object of the Faculty class

stu1 = Student(001, 'Carla', 3.85)
stu2 = Student(002, 'Mehdi', 4.0)
#Some more lines of code

print(stu1.stu_id, stu1.stu_name, stu1.stu_gpa)
print(stu2.stu_id, stu2.stu_name, stu2.stu_gpa)