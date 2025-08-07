class Employee:
	def __init__(self, name, id, dept, title):
		self.emp_name = name
		self.emp_id = id
		self.emp_dept = dept
		self.emp_title = title
		
	def get_emp_name():
		return emp_name
		
	def __str__(self):
		print(self.emp_name, self.emp_id, self.emp_dept, self.emp_title)