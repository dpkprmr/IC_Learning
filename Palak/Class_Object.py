class person:
    def __init__(self, name, age, country):
        self.name= name
        self.age= age
        self.country= country
    def self_introduction(self):
        print("My name is " +  self.name)
        print("My age is " + self.age)
        print("Country I live in " + self.country)
p1= person("Palak", "27", "India")
p2= person("Eric", "30", "US")
p1.self_introduction()
p2.self_introduction()
# Without Calling Function
class person:
    def __init__(self, name, age, country):
        self.name= name
        self.age= age
        self.country= country
p1= person("Palak", '27', "India")
print(p1.name)
print(p1.age)
print(p1.country)
