class Person:
    def __init__(self, name, age, gender, address):
        self.name = name
        self.age = age
        self.gender = gender
        self.address = address
        
    def profession(self, company):
        
        return (f"Hello, my name is {self.name} and my age is {self.age} and i work in {company}")
    
    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}, Address: {self.address}"
    
    
miles = Person('Enock', 25, 'Male', 36)

print(miles.profession('XYZ Corp'))

print(miles)

