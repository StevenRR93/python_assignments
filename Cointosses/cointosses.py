import random
def coin_toss():
    coin = round(random.random())
    if (coin == 1):
        return "head"
    else:
        return "tail"

def tosses_sim():
    print("Starting the program")
    anum = 0
    hcount = 0
    tcount = 0
    for i in range(5001):
        if (coin_toss() == "head"):
            print ("Attempt #"+ str(anum)+ ": Throwing a coin... It's a head! ... Got "+ str(hcount) + " head(s) so far and "+ str(tcount) +" tail(s) so far")
            hcount += 1
        else:
            print ("Attempt #"+ str(anum)+ ": Throwing a coin... It's a tail! ... Got "+ str(hcount) + " head(s) so far and "+ str(tcount) +" tail(s) so far")
            tcount += 1
        anum += 1
    print("Ending the program, thank you!")
tosses_sim()