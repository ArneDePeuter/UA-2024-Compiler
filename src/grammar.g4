// Grammar.g4

grammar Grammar;

// Parser rules
expression : (expressionSequence ';')+ ;
expressionSequence : logicalExpression ;
atom : NUMBER | '(' expressionSequence ')' ;
logicalExpression : comparisonExpression ( ('&&' | '||') comparisonExpression )* ;
comparisonExpression : additiveExpression ( ('>' | '<' | '==' | '>=' | '<=' | '!=') additiveExpression )* ;
additiveExpression : multiplicativeExpression ( ('+' | '-') multiplicativeExpression )* ;
multiplicativeExpression : unaryExpression ( ('*' | '/' | '%') unaryExpression )* ;
unaryExpression : ('+' | '-' | '!') unaryExpression | primary ;
primary : NUMBER | '(' expressionSequence ')' ;

// Lexer rules
NUMBER : [0-9]+ ;
WS : [ \t\r\n]+ -> skip ;


