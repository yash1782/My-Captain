# AREA OF THE CIRCLE
from msilib.schema import File


rad=float(input("Input the radius of the circle: "))
# print(rad)
# print(type(rad))

Area=3.14*rad*rad
print("The area of the circle with radius {} is: ".format(rad),Area)


#FIND THE EXTENSION OF FILE 

File_Name = input("Enter File Name :(Format:- filename.py) : ")
File_Name=File_Name.split(".")[1]
if File_Name=="py":
    print("The extension of the file is : Python")  