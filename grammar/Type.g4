grammar Type;
import Tokens;

type: Const? (BaseType | typedefName | enumType | structType) Multiply*;

typedefName: Identifier | BaseType;

enumType: Enum Identifier;

structType: Struct Identifier;