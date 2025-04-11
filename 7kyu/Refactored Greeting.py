class Person():
    def __init__(self, name):
        self.name = name
    
    def greet(self, name):
        return f"Hello {name}, my name is {self.name}"
    
    def name(self):
        return self.name

if __name__ == "__main__":
    jack = Person("Jack")
    jill = Person("Jill")

    print(jack.greet("Jill"))
    print(jack.greet("Mary"))

    print(jill.greet("Jack"))
    print(jill.name)