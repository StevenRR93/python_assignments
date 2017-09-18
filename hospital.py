class Patient(object):
    
    def __init__(self, uid, name, allergies):
        self.uid = uid
        self.name = name
        self.allergies = allergies
        self.bed = None

    def display(self, *num):
        print("ID: "+ str(self.uid))
        print("Name: "+ self.name)
        print("Allergies: "+ self.allergies)
        print("Bed: "+ str(self.bed))
    
    def setBed(self, bedno):
        self.bed = bedno

    def getBed(self):
        return self.bed

    def getName(self):
        return self.name

class Hospital(object):

    def __init__(self, patients, name, capacity):
        self.patients = patients
        self.name = name
        self.capacity = capacity
        for i in range(len(patients)):
            patients[i].setBed(i+1)

    def admit(self, newpatient):
        if (len(self.patients) >= self.capacity):
            print("Hospital is full")
        else:
            if (len(self.patients)== 0):
                self.patients.setBed(1)
            else:
                bednum = 0
                for i in range(len(self.patients)):
                    for j in range(len(self.patients)):
                        if (bednum + 1 == self.patients[j].getBed()):
                            bednum += 1
                self.patients.append(newpatient)
                if (bednum == len(self.patients)-1):  
                    self.patients[len(self.patients)-1].setBed(bednum+1)
                else:
                    self.patients[len(self.patients)-1].setBed(bednum)
                    print("c3"+ str(bednum))

            self.patients.append(newpatient)
            print("Admitted successfully")
    
    def discharge(self, n):
        check = True
        if (len(self.patients) > 0):
            for i in range(len(self.patients)):
                if (self.patients[i].getName() == n):
                    self.patients[i].setBed(None)
                    self.patients.pop(i)
                    print("Patient removed successfully")
                    check = False
                    break
        if (check):    
            print("Patient not found: "+ self.patients[i].getName())

patient1 = Patient(1, "John", "None")
patient2 = Patient(2, "Smith", "Peanuts")
patient3 = Patient(3, "Jane", "None")
patient4 = Patient(4, "Doe", "Bees")
patient5 = Patient(5, "Dude", "Working")
h = Hospital([patient1,patient2, patient3, patient4, patient5], "Hospital" , 6)
patient6 = Patient(6, "Addon", "Math")
h.admit(patient6)
patient1.display()
patient2.display()
patient3.display()
patient4.display()
patient5.display()
patient6.display()
h.discharge("Addon")
patient6.display()