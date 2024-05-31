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
        return 4


class Array(Type):
    def __init__(self, target: Type, length: int, dimensions: list[int]):
        super().__init__()
        self.target = target
        self.length = length
        self.dimensions = dimensions

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
    def __init__(self, name: str, fields: list[tuple[str, Type]]):
        super().__init__()
        self.name = name
        self.fields = fields

    @cached_property
    def width(self):
        return sum([field[1].width for field in self.fields])

    def get_member_offset(self, field_name: str):
        offset = 0
        for field in self.fields:
            if field[0] == field_name:
                return offset
            offset += field[1].width
        raise ValueError(f"Field {field_name} not found in struct {self.name}")

    def get_member_type(self, field_name: str):
        for field in self.fields:
            if field[0] == field_name:
                return field[1]
        raise ValueError(f"Field {field_name} not found in struct {self.name}")

class Any(Type):
    def __init__(self):
        super().__init__()

    @cached_property
    def width(self):
        raise RuntimeError("Any type does not have a width")
