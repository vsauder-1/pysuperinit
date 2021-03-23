"""Demonstrate simple inheritance for __init__ and method"""

class Animal:
    def __init__(self, mode):
        self._mode = mode

    def move(self, steps):
        print(f"{str(self)} {self._mode}ing {steps=}")

    def __str__(self):
        return 'Animal'

class Dog(Animal):
    def __init__(self, color):
        super().__init__('runn')
        self._color = color

    def move(self, steps):  # should match base definition
        super().move(steps)

    def __str__(self):
        return f'{self._color.capitalize()} dog'

Dog('brown').move(3)
