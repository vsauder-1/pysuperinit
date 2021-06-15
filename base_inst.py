class A:
    CLASS_VAR = 'A'

    def __new__(cls, *args, **kwargs):
        print("Creating A instance")
        obj = super(A, cls).__new__(cls)
        obj.var = 'superA'
        return obj

    def __init__(self):
        print(f'As {self.CLASS_VAR=} var={getattr(self, "var", "a_unknown_var")}')
        self.var = 'a'

    def func(self):
        print(f'func(A): {self.CLASS_VAR=}')

    @classmethod
    def cfunc(cls):
        print(f'cfunc(A): {cls.CLASS_VAR=}')

    @staticmethod
    def sfunc():
        print('sfunc(A)')


class B(A):
    CLASS_VAR = 'B'

    def __new__(cls, *args, **kwargs):
        print("Creating B instance")
        obj = super(B, cls).__new__(cls)
        obj.var = 'superB'
        return obj

    def __init__(self):
        print(f'Bs {self.CLASS_VAR=} var={getattr(self, "var", "b_unknown_var")}')
        super().__init__()
        self.var = 'b'
        print(f'Bs {self.CLASS_VAR=} {self.var=}')

    def func(self):
        super().func()
        print(f'func(B): {self.CLASS_VAR=}')

    @classmethod
    def cfunc(cls):
        super().cfunc()
        print(f'cfunc(B): {cls.CLASS_VAR=}')

    @staticmethod
    def sfunc():
        # super().sfunc()
        print('sfunc(B)')


x = A()
x.func()
x.cfunc()
x.sfunc()
x = B()
x.func()
x.cfunc()
x.sfunc()
