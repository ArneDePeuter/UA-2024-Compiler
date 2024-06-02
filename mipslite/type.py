from collections import OrderedDict
from functools import cached_property


class Type:
    def __init__(self, width: int):
        self.width = width


class Int(Type):
    def __init__(self):
        super().__init__(4)

class Float(Type):
    def __init__(self):
        super().__init__(4)

class Char(Type):
    def __init__(self):
        super().__init__(4)


class Array(Type):
    def __init__(self, target: Type, length: int, dimensions: list[int]):
        self.target = target
        self.length = length
        self.dimensions = dimensions
        super().__init__(self.target.width * self.length)


class Pointer(Type):
    def __init__(self, target: Type):
        super().__init__(4)
        self.target = target


class Struct(Type):
    def __init__(self, name: str, fields: list[tuple[str, Type]]):
        self.name = name
        self.fields = fields
        super().__init__(sum([field[1].width for field in self.fields]))

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
        super().__init__(None)


class Void(Type):
    def __init__(self):
        super().__init__(None)
