def odd_even():
    for i in range(1, 2001):
        if (i%2 == 0):
            print("Number is " + str(i) +". This is an even number.")
        else:
            print("Number is " + str(i) +". This is an odd number.")
odd_even()

def multiply(mlist, num):
    it = 0
    for i in mlist:
        mlist[it] = i * num
        it += 1
    return mlist
a = [2,4,10,16]
b = multiply(a,5)
print(b)

def layered_multiples(arr):
    new_array = []
    for i in arr:
        temp_array = []
        for j in range(i):
            temp_array.append(1)
        new_array.append(temp_array)
    return new_array
x = layered_multiples(multiply([2,4,5],3))
print x