

try:
    a=b
except:
    print("This code is wrong")
finally:
    print("finally")
print("This is outside")


try:
    a=int(input("Enter the no 1 "))
    b=int(input("Enter the no 2 "))
    c=a/b
except NameError as ex1:
    print("There is name error")
except Exception as ex:
    print(ex)
else:
    print("no error")
finally:
    print("It will execute always")