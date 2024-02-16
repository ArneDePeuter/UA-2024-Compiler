grammar grammar;

// Parser rules
program : (expression ';')+ ;

expression : logicalExpression ;

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
    : multiplicativeExpression ('*' | '/' | '%') unaryExpression
    | unaryExpression
    ;

unaryExpression
    : ('+' | '-' | '!') unaryExpression
    | bitwiseExpression
    ;

bitwiseExpression
    : bitwiseExpression ('&' | '|' | '^') shiftExpression
    | shiftExpression
    ;

shiftExpression
    : shiftExpression ('<<' | '>>') primary
    | primary
    ;

primary
    : NUMBER
    | '(' expression ')'
    ;

// Lexer rules
NUMBER : [0-9]+ ;
PLUS : '+';
MINUS : '-';
MUL : '*';
DIV : '/';
MOD : '%';
GT : '>';
LT : '<';
EQ : '==';
GE : '>=';
LE : '<=';
NE : '!=';
AND : '&&';
OR : '||';
NOT : '!';
LSHIFT : '<<';
RSHIFT : '>>';
BITAND : '&';
BITOR : '|';
BITXOR : '^';
BITNOT : '~';

WS : [ \t\r\n]+ -> skip ;
