class Person:
    def __init__(self, name, last_name):
        self.person_name = name
        print(last_name)


bob = Person('vlad', 'cipariu')
print(bob.person_name)
