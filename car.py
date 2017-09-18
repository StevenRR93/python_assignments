class car(object):
    
    def __init__(self, price, speed, fuel, milage):
        
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.milage = milage
        if (price > 10000):
            self.tax = .15
        else:
            self.tax = .12

    def displayall(self):
        print ("Price: $" + str(self.price))
        print ("Speed: " + str(self.price) + "mph")
        print ("Fuel: " + str(self.speed))
        print ("Milage: " + str(self.milage) + " mpg")
        print ("Tax:" + str(self.tax) +"%")        
        return self

car1 = car(2000, 35, "Full", 15)
car1.displayall()
car2 = car(2000, 15, "Kind of Full", 105)
car2.displayall()
car3 = car(2000, 35, "Full", 95)
car3.displayall()
car4 = car(2000, 35, "Full", 25)
car4.displayall()
car5 = car(2000000, 35, "Empty", 15)
car5.displayall()