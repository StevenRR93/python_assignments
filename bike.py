# declare a class and give it name User
class bike(object):

    # the __init__ method is called every time a new object is created
    def __init__(self, price, maxspeed):
        # set some instance variables. just like any variable we can call these anything
        self.price = price
        self.maxspeed = maxspeed
        self.miles = 0
    # this is a method we created to help a user login
    def displayinfo(self):
        print ("Price is: " + str(self.price)+ ". Max speed is: " + str(self.maxspeed) + ". Miles ridden is: " + str(self.miles) + ".")
        return self

    def ride(self):
        print("Riding...")
        self.miles += 10
        return self
        
    def reverse(self):
        print("Reversing...")
        self.miles -= 5
        return self
#now create an instance of the class
ride1 = bike(300, 10)
ride1.ride()
ride1.ride()
ride1.ride()
ride1.reverse()
ride1.displayinfo()
ride2 = bike(400, 15)
ride2.ride()
ride2.ride()
ride2.reverse()
ride2.reverse()
ride2.displayinfo()
ride3 = bike(500, 20)
ride3.reverse()
ride3.reverse()
ride3.reverse()
ride3.displayinfo()