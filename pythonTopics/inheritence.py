class car:
    def __init__(self,windows,doors,enginetype):
        self.windows=windows
        self.doors=doors
        self.enginetype=enginetype

    def drive(self):
        print('The person drives the car')

car1=car(3,4,"diesel")
car1.drive()


class audi(car):
    def __init__(self,windows,doors,enginetype,enableai):
        super().__init__(windows,doors,enginetype )
        # super(audi, self).__init__()
        self.enableai=enableai

    def selfdriven(self):
        print("Audi supports self driving")

audiQ7=audi(3,3,"diesel",True)
print(dir(audiQ7))
