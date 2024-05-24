# all variable are public
# if we put underscore before a variable it will be protected
# if we put double underscore before a variable it will be private
#
# but protected variable can be overriden and accessed .in case of protected overriden should be done only from subclass
# but private variable can be overriden and accessed in same class only

class vehicle:
    def __init__(self,car,bike,enginetype):                   #Acts as constructor
        self._car=car
        self.bike=bike
        self.enginetype=enginetype
        #here 2 attribute is created

    def self_driving(self):# if i give here parameter self then i ll be able to access the 2 argument
        return "This is {} car".format(self.enginetype)

v1=vehicle("Audi A8","Pulser 200 RS","Petrol") #here v1 is pointing to self.It throws an error saying init missing 2 positional argument if we do not pass any args
print(v1._car)
print(v1.bike)
v1.cycle="Avon"
print(v1.cycle)
print(v1.self_driving())
print(dir(v1))