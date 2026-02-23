class Parent:
    def __init__(self, name):
        self.name = name
        self.attribut = None  # À la place de ligne 6-7

    # def set_attribut(self, attribut):
  #      self.attribut = attribut

    def greet(self):
        print(f"Hello, I am {self.name}.")

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def greet(self):
        parent_greeting = super().greet()
        return f"{parent_greeting} I am {self.age} years old."