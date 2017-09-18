class MathDojo(object):
    
    def __init__(self):
        self.number = 0

    def add(self, *num):
        for i in range(len(num)):
            if (isinstance(num[i], list)):
                for j in range(len(num[i])):
                    self.number += num[i][j]
            elif(isinstance(num[i], tuple) ):
                self.number += num[i].value()
            else:  
                self.number += num[i]
        return self

    def subtract(self, *num):
        for i in range(len(num)):
            if (isinstance(num[i], list)):
                for j in range(len(num[i])):
                    self.number -= num[i][j]
            elif(isinstance(num[i], tuple) ):
                self.number -= num[i].value()
            else:  
                self.number -= num[i]
        return self

    def result(self):
        return self.number
 
md = MathDojo() 
print(md.add(2).add(2,5).subtract(3,2).result())
md1 = MathDojo()
print(md1.add([1], 3,4).add([3,5,7,8], [2,4.3,1.25]).subtract(2, [2,3], [1.1,2.3]).result())