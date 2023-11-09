# DEFINITION
# Objected Oriented Programming is a way of thinking about and 
# organizing code for maximum reusability.

# ADVANTAGES OF OOP
# The point of OOP is to reuse the same code while giving 
# flexibility to create each object with their own features.

# It helps to focus on what the classes do rather than how they 
# do it. It makes code easier to understand.

# With this type of programming, a program comprises objects that
# can interact with the user, other objects, or other programs. 
# This makes programs more efficient and easier to understand.

# STAGES INVOLVED IN OOP
# Class definition;like function definition
#    This stage is where you write the blueprint to be used when called

# Instantiation
    # It is the process of creating an object from the class definition. 
    # After an object is instantiated, it is known as an instance
    
# Creating a class  
# using class keyword with a property of closet
class furniture():
    chairs = 5

# creating an object/instance
(number_of_chairs) = furniture()
print(number_of_chairs)
# output <__main__.furniture object at 0x00000271C028CB10> 
# this is the object Id
print(hash(number_of_chairs))
# the hash returns an interger value for every object '170281725101'
print(number_of_chairs.closets)
# returns the value of closets output=5