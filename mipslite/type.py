from collections import OrderedDict


class Type:
    def __init__(self):
        pass

    @property
    def width(self):
        """
        The size of the type in bytes
        :return:
        """
        raise NotImplementedError()


class Int(Type):
    def __init__(self):
        super().__init__()

    @property
    def width(self):
        return 4


class Float(Type):
    def __init__(self):
        super().__init__()

    @property
    def width(self):
        return 4


class Char(Type):
    def __init__(self):
        super().__init__()

    @property
    def width(self):
        return 1


class Array(Type):
    def __init__(self, target: Type, length: int):
        super().__init__()
        self.target = target
        self.length = length

    @property
    def width(self):
        return self.target.width * self.length


class Pointer(Type):
    def __init__(self, target: Type):
        super().__init__()
        self.target = target

    @property
    def width(self):
        return 4


class Struct(Type):
    def __init__(self, fields: OrderedDict[str, Type]):
        super().__init__()
        self.fields = fields

    @property
    def width(self):
        return sum([field.width for field in self.fields.values()])
