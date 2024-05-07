grammar Type;
import Tokens;

type: Const? (BaseType | typedefType | enumType | structType) AddressOf*;

typedefType: Identifier;

enumType: Enum Identifier;

structType: Struct Identifier;