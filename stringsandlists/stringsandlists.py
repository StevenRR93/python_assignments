words = "It's thanksgiving day. It's my birthday,too!"
print(str(words.find("day")))
words = words.replace("day", "month", 1)
print(words)
x = [2,54,-2,7,12,98]
print(max(x))
print(min(x))
x = ["hello",2,54,-2,7,12,98,"world"]
print(x[0])
print(x[len(x)-1])
y = [x[0], x[len(x)-1]]
print(y)
x = [19,2,54,-2,7,12,98,32,10,-3,6]
x.sort()
a = []
b = []
i = 0
for val in x:
    if i < len(x)/2:
        a.append(val)
    elif i == len(x)/2:
        b.append(0)
    if i >= len(x)/2:
        b.append(val)
    i += 1
b[0] = a
print(str(b))
    