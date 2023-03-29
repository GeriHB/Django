class Dog:

    def __init__(self, name, age, furColor):
        self.name = name
        self.age = age
        self.furColor = furColor

    def bark(self, st):
        print('BARK!' + st)


mydog = Dog('Fido', 13, 'Brown')
print(mydog.age)
mydog.bark('shcasc')
