import sys
def draw_stars(slist):
    for i in slist:
        for j in range(i):
            sys.stdout.write("*")
        sys.stdout.write('\n')
    sys.stdout.flush()
x = [4, 6, 1, 3, 5, 7, 25]
draw_stars(x)

def draw_things(tlist):
    for i in tlist:
        if(isinstance(i, str)):
            for j in range(len(i)):
                sys.stdout.write(i[0])
        else:
            for j in range(i):
                sys.stdout.write("*")
        sys.stdout.write('\n')
    sys.stdout.flush()
x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
draw_things(x)