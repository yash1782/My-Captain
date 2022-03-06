# AREA OF THE CIRCLE
rad=float(input("Input the radius of the circle: "))
# print(rad)
# print(type(rad))

Area=3.14*rad*rad
print("The area of the circle with radius {} is: ".format(rad),Area)


#FIND THE EXTENSION OF FILE 


import pathlib
  
# function to return the file extension
file_extension = pathlib.Path('Area_Of_Circle.py').suffix
print("File Extension: ", file_extension)  