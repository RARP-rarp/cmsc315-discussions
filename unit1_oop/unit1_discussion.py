"""
===========================================================
Unit 1 DISCUSSION: Python OOP, Namespaces, and Copying
===========================================================

INSTRUCTIONS:
In this assignment, you will build and explore object-oriented programming (OOP) concepts in Python.
You are provided with starter code containing TODO sections. Your task is to complete, modify, and
analyze the code to demonstrate understanding of inheritance, namespaces, and object copying.
"""


from copy import copy, deepcopy


# TODO 1:
# Create a parent class.
#
# Requirements:
# - Include at least one class variable.
# - Include at least two instance variables.
# - Include a constructor (__init__).
# - Include a method that returns or displays information about the object.
#
# Replace the pass statement with your implementation.

class ItemClass:
    state = "active"

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
    def tooltip(self):
        print(f"Currently {self.state}")

# TODO 2:
# Create a child class that inherits from the parent class.
#
# Requirements:
# - Use inheritance.
# - Add at least one new class variable.
# - Add at least two new instance variables.
# - Add at least one new method.
# - Override a method from the parent class.
#
# Replace the pass statement with your implementation.

class WeaponClass(ItemClass):
    description = "Weapon"

    def __init__(self, name, weight, attack_speed, damage):
        super().__init__(name, weight)
        self.attack_speed = attack_speed
        self.damage = damage
    def tooltip(self):
        print(f"AS {self.attack_speed} DAM {self.damage}")


# TODO 3:
# Create a function that demonstrates class namespaces and instance namespaces.
#
# Your function should:
# - Create at least two objects of the child class.
# - Access a class variable through the class itself.
# - Access the same class variable through an object.
# - Add a new attribute to only one object after it is created.
# - Display each object's namespace using __dict__.
# - Display information about the class namespace.

def demonstrate_namespaces(name1, weight1, attack_speed1, damage1, name2, weight2, attack_speed2, damage2):
    print("\n=== Namespace Demonstration ===")
    first_weapon = WeaponClass(name1, weight1, attack_speed1, damage1)
    second_weapon = WeaponClass(name2, weight2, attack_speed2, damage2)
    print(f"WeaponClass description: {WeaponClass.description}")
    print(f"first_weapon description: {first_weapon.description}")
    first_weapon.nickname = "Thunder"
    print("First Weapon: ", first_weapon.__dict__, "\nSecond Weapon: ", second_weapon.__dict__)
    print("Weapon Class namespace information: ", WeaponClass.__dict__)


# TODO 4:
# Create a function that demonstrates shallow copying and deep copying.
#
# Requirements:
# - Create an object that contains nested mutable data.
# - Create a shallow copy.
# - Create a deep copy.
# - Modify the original object's nested data.
# - Display the original object, shallow copy, and deep copy.
# - Use comments to explain the difference between shallow and deep copying.

def demonstrate_copying(given_list):
    original_list = given_list
    shallow_copied = copy(original_list)
    deep_copied = deepcopy(original_list)
    print("\n=== Copy Demonstration ===")
    print(f"Original list: {original_list}")
    print("Shallow copying")
    print("Deep copying\n")
    print("Modifying the deep copy, changing the first index to ten and second first index to zero")
    deep_copied[0] = "ten"
    deep_copied[2][0] = "zero"
    print(f"Original list: {original_list}")
    print(f"Deep copy: {deep_copied}")
    print("The original and the deep copy are independent of each other!\n")
    print("Modifying the shallow copy, changing the first index to nine and second first index to thirteen")
    # Shallow copy only makes a new instance for the outer layer of list, but a reference entry for the inner lists.
    shallow_copied[0] = "nine"
    shallow_copied[2][0] = "thirteen"
    print(f"Original list: {original_list}")
    print(f"Shallow copy: {shallow_copied}")
    print("Only the shallow copy is changed for the first index, but both second first indices have changed!")




# TODO 5:
# Complete the main function.
#
# Requirements:
# - Create at least one object from the parent class.
# - Create at least one object from the child class.
# - Demonstrate inheritance by calling methods.
# - Call your namespace demonstration function.
# - Call your copy demonstration function.

def main():
    print("=== Unit 1 OOP Assignment ===")

    print("\nCreate and test your parent object")
    Item1 = ItemClass("Backpack", 4)
    print(Item1.__dict__)
    print("\nCreate and test your child object")
    Left = WeaponClass("Dagger", 1, "three", "four")
    print(Left.__dict__)
    demonstrate_namespaces("Shotgun", 2, "five", "six", "Longsword", 3, "seven", "eight")
    demonstrate_copying(["one", "two", ["eleven", "twelve"]])


if __name__ == "__main__":
    main()