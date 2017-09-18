def filterbytype(value):
    if isinstance(value, int):
        if (value < 100):
           print("Thats a small number! ")
        else:
            print("That's a big number.")
    elif isinstance(value, str):
        if (len(value) < 50):
            print("Short sentence.")
        else:
            print("Long sentence.")
    elif isinstance(value, list):
        if (len(value) < 10 ):
            print("Small list.")
        else:
            print("Big list!")

sI = 45
mI = 100
bI = 455
eI = 0
spI = -23
sS = "Rubber baby buggy bumpers"
mS = "Experience is simply the name we give our mistakes"
bS = "Tell me and I forget. Teach me and I remember. Involve me and I learn."
eS = ""
aL = [1,7,4,21]
mL = [3,5,7,34,3,2,113,65,8,89]
lL = [4,34,22,68,9,13,3,5,7,9,2,12,45,923]
eL = []
spL = ['name','address','phone number','social security number']
filterbytype(sI)
filterbytype(mI)
filterbytype(bI)
filterbytype(eI)
filterbytype(spI)
filterbytype(sS)
filterbytype(mS)
filterbytype(bS)
filterbytype(eS)
filterbytype(aL)
filterbytype(mL)
filterbytype(lL)
filterbytype(eL)
filterbytype(spL)