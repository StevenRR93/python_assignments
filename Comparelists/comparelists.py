def comparelists(li1, li2):
    if (len(li1) != len(li2)):
        return False
    else:
        j = 0
        for i in li1:
            if i != li2[j]:
                return False
            j += 1
    return True


list_one = [1,2,5,6,2]
list_two = [1,2,5,6,2]
print(comparelists(list_one, list_two))
list_one = [1,2,5,6,5]
list_two = [1,2,5,6,5,3]
print(comparelists(list_one, list_two))
list_one = [1,2,5,6,5,16]
list_two = [1,2,5,6,5]
print(comparelists(list_one, list_two))
list_one = ['celery','carrots','bread','milk']
list_two = ['celery','carrots','bread','cream']
print(comparelists(list_one, list_two))
        
