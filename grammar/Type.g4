grammar Type;
import Tokens;

type: Const? (BaseType | typedefType | enumType | structType) Multiply*;

typedefType: Identifier;

enumType: Enum Identifier;

structType: Struct Identifier;