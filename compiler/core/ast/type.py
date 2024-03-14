
class Type:
    ...


class IntegerType(Type):
    ...


class FloatType(Type):
    ...


class CharType(Type):
    ...


class ConstType(Type):
    def __init__(self, of: Type):
        self.of = of


class AddressType(Type):
    def __init__(self, of: Type):
        self.of = of


class DereferenceType(Type):
    def __init__(self, of: Type):
        self.of = of

