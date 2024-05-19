from collections import OrderedDict
from functools import cached_property


class Type:
    def __init__(self):
        pass

    @cached_property
    def width(self):
        """
        The size of the type in bytes
        :return:
        """
        raise NotImplementedError()


class Int(Type):
    def __init__(self):
        super().__init__()

    @cached_property
    def width(self):
        return 4


class Float(Type):
    def __init__(self):
        super().__init__()

    @cached_property
    def width(self):
        return 4


class Char(Type):
    def __init__(self):
        super().__init__()

    @cached_property
    def width(self):
        return 1


class Array(Type):
    def __init__(self, target: Type, length: int):
        super().__init__()
        self.target = target
        self.length = length

    @cached_property
    def width(self):
        return self.target.width * self.length


class Pointer(Type):
    def __init__(self, target: Type):
        super().__init__()
        self.target = target

    @cached_property
    def width(self):
        return 4


class Struct(Type):
    def __init__(self, fields: OrderedDict[str, Type]):
        super().__init__()
        self.fields = fields

    @cached_property
    def width(self):
        return sum([field.width for field in self.fields.values()])
