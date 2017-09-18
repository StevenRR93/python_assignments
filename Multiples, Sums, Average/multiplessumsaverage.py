def odds():
    for val in range(1, 1000, 2):
        print(val)
#odds()
def fives():
    for val in range(5, 1000001, 5):
        print(val)
#fives()
a = [1, 2, 5, 10, 255, 3]
def sumavg(list):
    asum = 0
    for val in list:
        asum += val
    print("Sum:")
    print(str(asum))
    print("Average:")
    print(str(asum/len(a)))
sumavg(a)

