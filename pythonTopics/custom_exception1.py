
class dobException(Exception):
    pass
year=int(input("enter the year of birth  "))
age =2023-year
try:
    if age>20 and age<=30:
        print("Age is valid")
    else:
        raise dobException

except dobException:
    print("The Year is not valid ")