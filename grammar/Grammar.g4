grammar Grammar;

// Parser rules
program : statement* mainFunction statement* ;

mainFunction : 'int' 'main' '(' ')' body ;

body : '{' statement* '}' ;

variableDeclaration
    : type variableDeclarationQualifiers ';'
    ;

variableDeclarationQualifiers
    : (variableDeclarationQualifier (',' variableDeclarationQualifier)*)?
    ;

variableDeclarationQualifier
    : ID ('=' expression)?
    ;

castExpression
    : '(' type ')' unaryExpression
    ;

statement
    : expressionStatement
    | body
    | variableDeclaration
    | assignmentStatement
    | comment
    | typedefStatement
    ;

typedefStatement
    : 'typedef' baseType ID ';';

expressionStatement
    : expression ';'
    ;

expression
    : logicalExpression
    | printCall
    ;

printCall
    : 'printf' '(' ('"%s"' | '"%d"' | '"%x"' | '"%f"' | '"%c"' ) ',' logicalExpression ')'
    ;

assignmentStatement
    : addressQualifier* ID assignmentOperator expression ';'
    ;

logicalExpression
    : logicalExpression ('&&' | '||') comparisonExpression
    | comparisonExpression
    ;

comparisonExpression
    : comparisonExpression ( '>' | '<' | '==' | '>=' | '<=' | '!=' ) additiveExpression
    | additiveExpression
    ;

additiveExpression
    : additiveExpression ('+' | '-') multiplicativeExpression
    | multiplicativeExpression
    ;

multiplicativeExpression
    : multiplicativeExpression ('*' | '/' | '%') bitwiseExpression
    | bitwiseExpression
    ;

bitwiseExpression
    : bitwiseExpression ('&' | '|' | '^') shiftExpression
    | shiftExpression
    ;

shiftExpression
    : shiftExpression ('<<' | '>>') unaryExpression
    | unaryExpression
    ;

unaryExpression
    : ('+' | '-' | '!' | '*' | '&' | '++' | '--') unaryExpression
    | primary ('++' | '--')?
    ;


primary
    : NUMBER
    | FLOAT
    | '(' expression ')'
    | ID
    | CHAR
    | CHAR_ESC
    | castExpression
    ;

type
    : const? baseType addressQualifier*
    ;

baseType
    : 'int'
    | 'float'
    | 'char'
    | ID
    ;

const
    : 'const'
    ;

addressQualifier
    : '*'
    ;


assignmentOperator
    : '='
    | '+='
    | '-='
    | '*='
    | '/='
    | '%='
    | '<<='
    | '>>='
    | '&='
    | '^='
    | '|='
    ;

comment
    : SINGLE_LINE_COMMENT
    | MULTI_LINE_COMMENT
    ;


// Lexer rules
NUMBER : '0' | [1-9][0-9]* ;
FLOAT : [0-9]+ '.' [0-9]* | '.' [0-9]+;
ID     : [a-zA-Z_][a-zA-Z_0-9]* ;
CHAR : '\'' [\u0000-\u00FF] '\'' ;
CHAR_ESC : '\'' ( '\\n' | '\\t' | '\\0' | . ) '\'' ;
PLUS   : '+';
MINUS  : '-';
MUL    : '*';
DIV    : '/';
MOD    : '%';
GT     : '>';
LT     : '<';
EQ     : '==';
GE     : '>=';
LE     : '<=';
NE     : '!=';
AND    : '&&';
OR     : '||';
NOT    : '!';
LSHIFT : '<<';
RSHIFT : '>>';
BITAND : '&';
BITOR  : '|';
BITXOR : '^';
BITNOT : '~';
WS     : [ \t\r\n]+ -> skip ;
SINGLE_LINE_COMMENT: '//' .*? ('\n' | EOF);
MULTI_LINE_COMMENT : '/*' .*? '*/' ;
