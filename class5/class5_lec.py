#assigning name to a variable:
user_name = "Amna ikram" #snake case : all letter are written in lower case separated with  underscore
User_Name ="Amna Ikram" #Pascal case: first letters are capital
username = "Amna Ikram" #small case : all letters are small 
USERNAME = "Amna Ikram" #capital case : all letters are capital

#topics:
# data types: Integer, string ,float , boolean
# Rules of naming a variable 
# Arithematic operator : + - / * 
# Concatention operator : +
# unordinary  operator : floor (//) , exponent(**) , modulus(%)
# Comments 


from datetime import datetime
current_year = datetime.now().year
your_birth_year = int(input ("Enter your birth year: "))
print(f"your age is { current_year - your_birth_year }")


