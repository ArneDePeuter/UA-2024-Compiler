
class Type:
    ...


class Integer(Type):
    ...


class Float(Type):
    ...


class Char(Type):
    ...


class Address(Type):
    base_type: Type


class Dereference(Type):
    base_type: Type

