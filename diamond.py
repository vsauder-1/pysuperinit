"""Demonstrate the order that __init__ is called in for multiple inheritance diamond"""


class IoBase:
    def __init__(self, dev):
        print('IO init')
        self.dev = dev

class Input(IoBase):
    def __init__(self, dev, buffered):
        print('Input init')
        super().__init__(dev)
        self.buffered = buffered

class Output(IoBase):
    def __init__(self, dev, stderr):
        print('Output init')
        super().__init__(dev)
        self.stderr = stderr

class IO(Input, Output):
    def __init__(self, dev, buffered, stderr):
        print('IO init')
        # replacing this line:
        # super().__init__(dev, stderr)
        # with these 2 does not change the behavior
        Input.__init__(self, dev, buffered)
        Output.__init__(self, dev, stderr)
        self.log = None

# fails with:  __init__() missing 1 required positional argument: 'stderr'
# Input.IoBase.__init__ is calling Output.__init__ via super().__init__
io = IO('/dev/tty', True, True)
