grammar Grammar;

// Parser rules
program : statement* mainFunction statement* ;

mainFunction : 'int' 'main' '(' ')' body ;

body : '{' statement* '}' ;

iterationStatement
    : WHILE '(' expression ')' statement
    | FOR '(' forCondition ')' statement
    ;

forCondition
    : forFirst forSecond forThird
    ;

forFirst
    : variableDeclaration
    | assignmentStatement
    | expressionStatement
    | TERMINAL
    ;

forSecond
    : expressionStatement
    | TERMINAL
    ;

forThird
    : expression?
    ;

breakStatement
    : BREAK TERMINAL
    ;

continueStatement
    : CONTINUE TERMINAL
    ;

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
    | iterationStatement
    | breakStatement
    | continueStatement
    | ';'
    ;

typedefStatement
    : 'typedef' type ID ';';

expressionStatement
    : expression ';'
    ;

expression
    : logicalExpression
    | printCall
    ;

printCall
    : 'printf' '(' PRINTFREPLACER ',' logicalExpression ')'
    ;

assignmentStatement
    : expression assignmentOperator expression ';'
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
    : const? (baseType | ID) addressQualifier*
    ;

baseType
    : 'int'
    | 'float'
    | 'char'
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
BREAK : 'break' ;
CONTINUE : 'continue' ;
WHILE  : 'while' ;
FOR    : 'for' ;
TERMINAL: ';';
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
PRINTFREPLACER: '"%s"' | '"%d"' | '"%x"' | '"%f"' | '"%c"' ;
WS     : [ \t\r\n]+ -> skip ;
SINGLE_LINE_COMMENT: '//' .*? ('\n' | EOF);
MULTI_LINE_COMMENT : '/*' .*? '*/' ;
