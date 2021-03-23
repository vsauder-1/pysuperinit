"""Demonstrate the order that __init__ is called in for multiple inheritance - mixins"""
from abc import ABC, abstractmethod


class DBase(ABC):
    def __init__(self):
        # super().__init__()  # this may call the mixin but we don't have mode to send
        print('Base - do nothing')
        self.data = dict()

    def get_data(self):
        return self.data

    def set_data(self, updates):
        self.data.update(updates)

    @abstractmethod
    def save(self, quik=False):
        """Push to a file somewhere"""

class LoggerMixin:
    def __init__(self, mode):
        print('Mixin - no base. mode=', mode)
        # super().__init__()  # << this does not make much sense as it does not have a base (other than object)
        self.mode = mode

    def set_data(self, updates):
        print(f'Doing update [{self.mode}]:', updates)
        super().set_data(updates)  # Pycharm does not like this: there is no clear resolution to this method

    def newlog(self):
        print('Starting new log')

class HttpDbase(DBase):
    def __init__(self, server):
        super().__init__()
        print('HTTP server:', server)
        self.server = server

    def save(self, quik=False):
        # push to a HTTP server
        super().save(quik)
        print('Sending to HTTP server:', self.server)

# this will correctly override set_data, but the init won't work because the server name goes to the mixin as 'mode'
class LoggerDbase(LoggerMixin, HttpDbase):
    pass

# this will init correctly, but it will not override set_data
class LoggerDbase(HttpDbase, LoggerMixin):
    pass

class LoggerDbase(LoggerMixin, HttpDbase):
    def __init__(self, server, mode='extended'):
        LoggerMixin.__init__(self, mode)
        HttpDbase.__init__(self, server)


db = LoggerDbase('http://someserver.local')
print('Data:', db.get_data())
db.set_data(dict(fruit=dict(name='apples', size='1bushel')))
print('Data:', db.get_data())
db.save()

# this works if the mixin does not have an __init__ method
class LoggerMixin:
    def set_data(self, updates):
        print(f'Doing update:', updates)
        super().set_data(updates)  # Pycharm does not like this: there is no clear resolution to this method

class LoggerDbase(LoggerMixin, HttpDbase):
    pass

db = LoggerDbase('http://someserver.local')
db.set_data(dict(fruit=dict(name='apples', size='1bushel')))
db.save()

# this works if the mixin does not touch the __init__ args
class LoggerMixin:
    def __init__(self, *args, **kwargs):
        mode = kwargs.pop('mode', 'abbrev')
        print('Mixin - no base. mode=', mode)
        super().__init__(*args, **kwargs)  # << this does not make much sense as it does not have a base (other than object)
        self.mode = mode

    def set_data(self, updates):
        print(f'Doing update [{self.mode}]:', updates)
        super().set_data(updates)  # Pycharm does not like this: there is no clear resolution to this method

class LoggerDbase(LoggerMixin, HttpDbase):
    pass

db = LoggerDbase('http://someserver.local')
db.set_data(dict(fruit=dict(name='apples', size='1bushel')))
db.save()
