class call(object):
    
    def __init__(self, uid, name, number, time, reason):
        self.uid = uid
        self.name = name
        self.number = number
        self.time = time
        self.reason = reason

    def display(self, *num):
        print("ID: "+ str(self.uid))
        print("Name: "+ self.name)
        print("Number: "+ str(self.number))
        print("Time: "+ str(self.time))
        print("Reason: "+ self.reason)
    
    def getTime(self):
        return self.time

    def getNumber(self):
        return self.number

class callcenter(object):

    def __init__(self, calls, queuesize):
        self.calls = calls
        self.queuesize = queuesize

    def add(self, newcall):
        self.calls.append(newcall)
    
    def remove(self):
        if (self.queuesize > 0):
            self.calls.pop(0)
            self.queuesize-1

    def removephone(self, num):
        for i in range(0, self.queuesize-1):
            if (self.calls[i].getNumber() == num):
                self.calls.pop(i)
                self.queuesize-1

    def info(self):
        for i in self.calls:
            i.display()
    
    def sort(self):
        for i in range(0, self.queuesize-1):
            for j in range(0, self.queuesize-1):
                if (self.calls[j].getTime() > self.calls[j+1].getTime() ):
                    temp = self.calls[j]
                    self.calls[j]= self.calls[j+1]
                    self.calls[j+1] = temp

call1 = call( 1, "Some", 1234567890, 10, "Reason")
call2 = call( 2, "Guy", 1111111, 20, "Excuse")
call3 = call( 3, "Is", 2222222, 30, "Idea")
call4 = call( 4, "Calling", 3333333, 40, "Thought")
call5 = call( 5, "Here", 4444444, 50, "Placeholder")
call6 = call( 6, "Add", 9876543210, 25, "Addon")
cc =callcenter([call1, call2, call3, call4, call5], 5)
cc.info()
print("")
cc.add(call6)
cc.remove()
cc.info()
print("")
cc.sort()
cc.info()
print("")
cc.removephone(1111111)
cc.info()