def findingcharacters(word_list, char):
    new_list = []
    for i in word_list:
        for j in i:
            if (j == char):
                new_list.append(i)
    return new_list

# input
wl = ['hello','world','my','name','is','Anna']
c = 'o'
print(findingcharacters(wl, c))
# output
#new_list = ['hello','world']