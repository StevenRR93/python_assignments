def typelist(listdt):
    bint = False
    bbool = False
    bcomplex = False
    bfloat = False
    bstr = False
    blist = False
    bother = False
    isnum = False
    isstr = False
    mixed = 0
    num = 0
    let = ""
    numtypes = 0
    for val in listdt:
        if isinstance(val, int):
            bint = True
            num += val
        elif isinstance(val, bool):
            bbool = True
        elif isinstance(val, float):
            bfloat = True
            num += val
        elif isinstance(val, complex):
            bcomplex = True
            num += val
        elif isinstance(val, str):
            bstr = True
            let += val + " "
        elif isinstance(val, list):
            blist = True
        else:
            bother = True
    typename = ""
    string = ""
    ssum = 0
        
    if (bint):
        typename = "integer"
        isnum = True
        mixed += 1
    if (bbool):
        typename = "bool"
        mixed += 1
    if (bfloat):
        typename = "float"
        isnum = True
        mixed += 1
    if (bcomplex):
        typename = "complex"
        isnum = True
        mixed += 1
    if (bstr):
        typename = "string"
        isstr = True
        mixed += 1
    if (blist):
        typename = "list"
        mixed += 1
    if (bother):
        typename = "other"
        mixed += 1
    if (mixed > 1):
        typename = "mixed"
    
    print("The list you entered is of "+ typename +" type")
    if (isnum):
        print("Sum: " + str(num))
    if (isstr):
        print("String: " + str(let))
#input
l = ['magical unicorns',19,'hello',98.98,'world']
#output
#"The list you entered is of mixed type"
#"String: magical unicorns hello world"
#"Sum: 117.98"
typelist(l)
# input
l = [2,3,1,7,4,12]
#output
#"The list you entered is of integer type"
#"Sum: 29"
typelist(l)
# input
l = ['magical','unicorns']
#output
#"The list you entered is of string type"
#"String: magical unicorns"
typelist(l)