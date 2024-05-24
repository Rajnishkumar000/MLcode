class car:
    pass
car1=car()
car2=car()

car1.window=4
car1.door=6
car2.window=8
car2.door=2
print(car1.window)
print(car1.door)
print(car2.window)
print(car2.door)
print(dir(car))
print(dir(car1))

# To fix no of attribute we can use __init__ main. Here we can assign any no of variables like window door engine

class vehicle:
    def __init__(self,car,bike,enginetype):                   #Acts as constructor
        self.car=car
        self.bike=bike
        self.enginetype=enginetype
        #here 2 attribute is created

    def self_driving(self):# if i give here parameter self then i ll be able to access the 2 argument
        return "This is {} car".format(self.enginetype)

v1=vehicle("Audi A8","Pulser 200 RS","Petrol") #here v1 is pointing to self.It throws an error saying init missing 2 positional argument if we do not pass any args
print(v1.car)
print(v1.bike)
v1.cycle="Avon"
print(v1.cycle)
print(v1.self_driving())
