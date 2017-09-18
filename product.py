class product(object):
    
    def __init__(self, price, name, weight, brand, cost):
        
        self.price = price
        self.name = name
        self.weight = weight
        self.brand = brand
        self.cost = cost
        self.status = "For Sale"

    def sell(self):
        self.status = "Sold"       
        return self

    def addtax(self, tax):
        total = self.cost
        total += self.cost * tax
        print("Price plus tax is: $" + str(total))
        return total
        
    def ret(self, defect, withbox):
        if (defect):
            self.status = "Defective"
            self.price = 0
        elif (withbox):
            self.status = "For Sale"
        else:
            self.status = "Used"
            self.cost = self.cost*.8
        return self
    
    def displayall(self):
        print ("Name: " + self.name)
        print ("Price: $" + str(self.price))
        print ("Weight: " + str(self.weight) +"lbs")
        print ("Brand: " + self.brand)
        print ("Cost: $"+ str(self.cost)) 
        print ("Status: " + str(self.status))      
        return self
        

product1 = product(100, "Tools", 10, "Craftsman", 100)
product1.displayall()
product1.addtax(.08)
product1.sell()
product2 = product(80, "Chair", 15, "Generic", 80)
product2.addtax(.07)
product2.sell()
product2.ret(True, False)
product2.displayall()
product3 = product(10000, "Watch", 1, "Rolex", 10000)
product3.addtax(.1)
product3.sell()
product3.displayall()
product3.ret(False, True)
product3.displayall()
product3.sell()


