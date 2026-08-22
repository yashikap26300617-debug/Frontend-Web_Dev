#to convert temperature 

# x=float(input("enter temperature:" ))
# unit=input()
# if unit == "c":
#     f=(x*9/5)+32
#     print(f) 
# elif unit == "F":
#     C=(x-32)*5/9
#     print(C)


#def convert_temperature(x,unit):
 #   return convert_temperature


# if unit=="c":
#    f=(x*9/5)+32
# print(f)

# elif unit =="F":
# C=(x-32)*5/9
# print(C) 


# x=float(input("enter temperature:"))
# unit=input()
# x=convert_temperature(x,unit)

def convert_temperature(temp, unit):
    if unit == "C":
        return (temp * 9 / 5) + 32
    elif unit == "F":
        return (temp - 32) * 5 / 9


x = float(input("Enter temperature: "))
unit = input()

x = convert_temperature(x, unit)

print(x)