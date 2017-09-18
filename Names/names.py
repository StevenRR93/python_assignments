def names(diction):
    for i in diction:
        print(i['first_name'] + " " + i['last_name'])
    print("")
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
names(students)

def name_format(diction):
    for i in diction:
        print(i)
        count = 1
        for j in diction[i]:
            print(str(count) +" - "+j['first_name'] +" "+ j['last_name'] + " - " + str(len(j['first_name'] +j['last_name'])))
            count += 1
users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
}
name_format(users)
