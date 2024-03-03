grammar MyGrammar;

// Parser rules
program : mainFunction ;

mainFunction : 'int' 'main' '(' ')' compoundStatement ;

compoundStatement : '{' statement* '}' ;

declaration
    : type variableList ';'
    ;

castExpression
    : '(' type ')' unaryExpression
    ;

statement
    : expressionStatement
    | compoundStatement
    | declaration
    ;

expressionStatement
    : expression ';'
    ;

expression
    : mutableExpression
    | immutableExpression
    ;

mutableExpression
    : assignmentExpression
    ;

immutableExpression
    : logicalExpression
    ;

assignmentExpression
    : unaryExpression assignmentOperator expression
    | logicalExpression
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
    : ('+' | '-' | '!' | '*' | '&' | '++' | '--') unaryExpression  // Existing prefix operators
    | primary ('++' | '--')?                                      // Adding optional postfix operators
    ;


primary
    : NUMBER
    | FLOAT
    | '(' expression ')'
    | ID    // Allow variable names as primary expressions.
    | CHAR
    | CHAR_ESC
    | castExpression
    ;

type
    : typeQualifier? baseType pointerQualifier*  // Adjusted rule
    ;

baseType
    : 'int'
    | 'float'
    | 'char'
    ;

typeQualifier
    : 'const'
    ;

pointerQualifier
    : '*'
    ;


variableList
    : (variable (',' variable)*)?
    ;

variable
    : ID ('=' expression)?
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
