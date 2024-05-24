def welcome_email(name,age):
    # return "welcome {} ,Your age is {}".format(name,age)
    # return "welcome {name} ,Your age is {age}".format(name=name,age=age)
    # return "welcome {name} ,Your age is {age}".format(age=age,name=name)
    return "welcome {n} ,Your age is {a} ok bye {}".format("Rajnish",a=age,n=name,)

print(welcome_email("Raj",21))