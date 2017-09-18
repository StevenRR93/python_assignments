def dictionary_basic(diction):
    print ("My name is " + diction["name"])
    print ("My age is " + diction["age"])
    print ("My country of birth is " + diction["country"])
    print ("My favorite language is " + diction["language"])

personal_dic = {
    "name" : "Anna", "age" : "101", "country" : "United States", "language" : "python"
}
dictionary_basic(personal_dic)
