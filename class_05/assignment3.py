#numerical no.01: finding age 
#solution:
current_year = 2024
your_birth_year = int(input ("Enter your birth year: "))
your_age = current_year - your_birth_year
print("Your age is " , your_age)
print('_______________ \n')



#numerical no.01 :using datetime function
#solution:
from datetime import datetime
current_year = datetime.now().year
your_birth_year = int(input ("Enter your birth year: "))
print(f"your age is { current_year - your_birth_year }")
print('_______________ \n')




#numerical no.02: area of rectangle: 
#solution:
lenght = int(input("Enter the Lenght of rectangle: "))
width = int(input("Enter the width of rectangle: "))
area = lenght * width
print("The area of your rectangle is " , area)

print('_______________ \n')



#numerical no.03 :area of circle ; pie*r^2
#solution:
radius = float(input("Enter the radius of circle: "))
area_of_circle = (radius**2) * 3.1417
print("The area of circle is " , area_of_circle)
print('_______________ \n')



#numerical no.04: area of cube ; to find the area of cube use 6a^2
#solution:
surface_area = float(input("Enter the surface area of cube: "))
cube_area = 6 *(surface_area ** 2)
print("The area of your cube is ", cube_area)
print('_______________ \n')



#numerical no 05: conversion of temperature:
#solution:
user_temp = str(input("What type of conversion you're going to do? \n Choose 01 or 02  \n 01) Celsius to Fahrenheit \n 02) Fahrenheit to celsius? \n Your answer: "))
temp = float(input("Enter temperature in numbers: "))
celsius = 0  
farenhite = 0
if user_temp == "01":
    farehite = (9/5)*temp +32 #conversion of Celsius temp into Fahrenheit
    print(temp , "ﾟC in Fahrenheit = " , farehite ,"( ﾟF")
else :
    celsius = (5/9)*(temp - 32) #conversion of Fahrenheit to Celsius
    print(temp ,"ﾟF in Celsius = " , celsius , "ﾟC")

print('_______________ \n')



#numerical no 06: conversion of time 
#solution:
user_time = int(input("What type of conversion you are going to do? \n Choose one option at a time : \n 01)Hours to minutes \n 02)Hours to seconds  \n 03) Seconds to miuntes \n 04)Seconds to hours \n 05)Minutes to hours \n 06)Minutes to seconds \n  Your answer(without zero): "))
time = int(input("Enter time in numbers: "))
seconds = 0
minutes = 0
hour = 0
 #converting time
if user_time == 1:
    hour = int(time*60)
    print(time,"hours = " , hour, "minutes")   
elif user_time == 2:
    hour = int(time*3600)
    print(time,"hours =" , hour,"seconds")  
elif user_time == 3:
    seconds = int(time/60)
    print(time,"seconds  = ",seconds,"minutes")
elif user_time == 4:
    seconds = int(time/3600)
    print(time,"seconds = ",seconds, "hours")
elif user_time == 5:
    minutes = int(time/60)
    print(time,"minutes = ",minutes,"hours")
elif user_time == 6:
    minutes= int(time*60)
    print(time,"minutes  = ",minutes,"seconds")
else :
    print("See you next time")
print('_______________ \n')




#numerical no 06 : time conversion_method 02
#solution:
user_time = int(input("Which conversion do you want to perform? \n_________________ \n Choose any one option \n 1)seconds \n 2)minutes \n 3)hour \n Enter your answer in numbers: "))
time = int(input("Enter time : "))
if user_time == 1:
 minutes = time/60
 hours = time/3600
 print(user_time ,"in minutes = ",minutes)
 print(user_time,"in hours =",hours)

elif user_time == 2:
 seconds  = time*60
 hours = time/60
 print(user_time,"in seconds = ",seconds)
 print(user_time,"in hours = ",hours)

else :
 seconds = time*3600
 minutes =time *60
 print(time ,"in seconds = ",seconds)
 print(time,"in minutes ",minutes)

print('_______________ \n')




#numerical no 07 : % calculation
#solution:
number = int(input("Enter the gained marks: "))
total_num = int(input("Enter total marks: "))
percentage = int((number/total_num)*100)
print(number , " = " , percentage,"%")
print('_______________ \n')




#numerical no 08:  Calculating BMI
#solution:
weight =float(input("Enter your weight in KG's : "))
height =float(input("Enter your height in meters: "))
BMI = weight / (height**2)
if BMI < 18.5:
    print("You are under-weight \nTake healty diet :)")
elif 18.5 <= BMI <= 24.9:
    print("Your weight is Normal. \nKeep up the good work 👍🏼")
elif 25 <= BMI <=29.9 :
    print("You are over-weight. \nHit the Gym 💪🏼")
else :
    print("You are Obese! \nTake care of yourself before it's too late")

print('_______________ \n')




#numerical no 09 :calculating volume of cylinder
#solution:
print("To find the volume of cylinder : V = 3.1415*(radius^2)*height")
print("----------- \n ")
radius = float(input("Enter th of radius of cylinder: "))
height = float(input("Enter the height of cylinder: "))
volume = int(3.1415 *(radius**2)*height)
print("The volume of cylinder is ", volume , "cubic meter")

print('_______________ \n')