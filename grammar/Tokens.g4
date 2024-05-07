grammar Tokens;

// skip whitespace
Ws: [ \t\r\n]+ -> skip ;

// Symbols
OpenParan: '(';
CloseParan: ')';
OpenBrace: '{';
CloseBrace: '}';
OpenBracket: '[';
CloseBracket: ']';
Comma: ',';
Colon: ':';
Equals: '=';
Delimiter: ';';
DotOp: '.';
ArrowOp: '->';

// Keywords
Const: 'const';
BaseType
    : 'int'
    | 'float'
    | 'char'
    | 'void'
    ;
Struct: 'struct';
Typedef: 'typedef';
Enum: 'enum';
Switch: 'switch';
Case: 'case';
Default: 'default';
If: 'if';
Else: 'else';
Break: 'break';
Return: 'return';
Continue: 'continue';
While: 'while';
For: 'for';

// Values
Identifier
    : [a-zA-Z_][a-zA-Z_0-9]*
    ;
Constant
    : Int
    | Float
    | Char
    ;
Int
    : '0' | [1-9][0-9]*
    ;
Float
    : [0-9]+ '.' [0-9]* | '.' [0-9]+
    ;
Char
    : '\'' CharContent '\''
    ;
CharContent
    : ~['\\\r\n]
    | ( '\\n' | '\\t' | '\\0' )
    ;
StringLiteral
    : '"' CharContent+ '"'
    ;

// Operators
AndBit: '&';
OrBit: '|';
XorBit: '^';
NotBit: '~';
AndLogical: '&&';
OrLogical: '||';
NotLogical: '!';
ShiftLeft: '<<';
ShiftRight: '>>';
Plus: '+';
Minus: '-';
Multiply: '*';
Divide: '/';
Modulus: '%';
Equal: '==';
NotEqual: '!=';
LessThan: '<';
GreaterThan: '>';
LessThanEqual: '<=';
GreaterThanEqual: '>=';
PlusPlus: '++';
MinusMinus: '--';
AddressOf: AndBit;
Dereference: Multiply;

// Misc
Comment: SingleLineComment | MultiLineComment;
SingleLineComment: '//' .*? ('\n' | EOF);
MultiLineComment: '/*' .*? '*/';
