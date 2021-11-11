def getAll ():
    _name = input("\nEnter your name: ")
    _age = int(input("\nEnter your age: "))
    _add = input("\nEnter your address: ")
    return _name, _age, _add

def display (nameF, ageF, addF):
    print(f"\nHi, my name is {nameF}. I am {ageF} years old and I live in {addF}.\n")

name, age, add = getAll()
display(name, age, add)