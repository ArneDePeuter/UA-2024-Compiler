// Arithmetic.g4

grammar Arithmetic;

// Parser Rules
expression : additiveExpression ;

additiveExpression
    : multiplicativeExpression ( ('+' | '-') multiplicativeExpression )*
    ;

multiplicativeExpression
    : atom ( ('*' | '/') atom )*
    ;

atom
    : NUMBER
    | '(' expression ')'
    ;

// Lexer Rules
NUMBER : [0-9]+ ;

WS : [ \t\r\n]+ -> skip ;
