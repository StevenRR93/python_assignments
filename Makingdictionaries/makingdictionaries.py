def make_dict(arr1, arr2):
    new_dict = {}
    # your code here
    if (len(arr1) >= len(arr2)):
        for i in range(len(arr1)):
            new_dict[arr1[i]] = arr2[i]
    else:
        for i in range(len(arr2)):
            new_dict[arr2[i]] = arr1[i] 
    return new_dict

name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

print (make_dict(name, favorite_animal))