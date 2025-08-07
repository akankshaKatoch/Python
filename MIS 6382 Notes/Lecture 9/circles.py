'''
Write a class definition for the Circle class.
The class has two instance variables, center and radius.
Note that the center is a tuple and contains two values - the x and y values.
All instance variables should be hidden.  
When the object is created, your code should check to make sure that the
radius is strictly positive.  If not, print an appropriate message.
In addition to the constructor, your class definition should also have the following methods:
1. Accessor methods for all instance variables
2. Mutator methods for all instance variables
3. A redefined __str__() method to print the center and radius of each circle object.
4. The definition should also have the following methods
	a. get_area():  This should compute and return the area of the circle
	b. get_circumference():  This should compute and return the circumference of the circle
	c. grow():  Each time this method is called, the radius of the circle object will increase by 1 
	d. shrink():  Each time this method is called, the radius of the circle object will decrease by 1 
'''
class Circle:

	def __init__(self, center, radius):
		if radius <= 0:
			print('Error')
		else:
			self.radius = radius
		self.center = center
		
	def get_radius(self):
		return self.radius
		
	def get_center(self):
		return self.center
		
	def get_area(self):
		from math import pi
		return self.radius ** 2 * pi
		
	def get_circumference(self):
		from math import pi
		return self.radius * 2 * pi
		
	def grow(self):
		self.radius += 1
		
	def shrink(self):
		self.radius = 1
		
	def __str__(self):
		return ('The circle is located at {} and has a radius of {}'.format(self.center, self.radius))