class Details:
    def setData(self,id,name,gender):
        self.id = id
        self.name = name
        self.gender = gender
        print("Id:",self.id)
        print("Name:",self.name)
        print("Gender",self.gender)

class Employee(Details):
    def setEmployee(self,id,name,gender,comp,dept):
        self.setData(id,name,gender)
        self.company = comp
        self.department = dept
        print("Company:",self.company)
        print("Department:",self.department)

class Doctor(Details):
    def setEmployee(self,id,name,gender,hospital,dept):
        self.setData(id,name,gender)
        self.hospital = hospital
        self.department = dept
        print("Hospital:",self.hospital)
        print("Department:",self.department)

obj1 = Doctor()
obj1.setEmployee(1,"Shrey","Male","ABC","Eyes")

obj2 = Employee()
obj1.setEmployee(2,'asdas','adasd','adasd','wdada')
