grammar Grammar;

// Parser rules
program : (statement)* ;

statement
    : body
    | forwardDeclaration
    | functionDeclaration
    | variableDeclaration
    | enumDeclaration
    | assignmentStatement
    | comment
    | typedefStatement
    | ifStatement
    | iterationStatement
    | breakStatement
    | continueStatement
    | switchStatement
    | returnStatement
    | expressionStatement
    | ';'
    ;

typedIdentifier : type ID arraySpecifier?;

enumDeclaration
    : 'enum' ID? '{' enumBody '}'
    ;

enumBody
    : enumList? (comment? ',' enumList)* comment? ','?
    ;

enumList
    : ID ('=' expression)? (',' comment? ID ('=' expression)?)* ','? comment?
    ;

forwardDeclaration : typedIdentifier '(' typeList? ')' TERMINAL ;

typeList : type ID? arraySpecifier? (',' type ID? arraySpecifier?)* ;

returnStatement : RETURN expression? TERMINAL ;

functionDeclaration : type ID '(' paramList? ')' body ;

paramList : typedIdentifier (',' typedIdentifier)* ;

functionCall : ID '(' argumentList? ')' ;

argumentList : expression (',' expression)* ;

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

printfCall
    : 'printf' '(' STRING_LITERAL (',' argumentList)? ')'
    ;

continueStatement
    : CONTINUE TERMINAL
    ;

variableDeclaration
    : type variableDeclarationQualifiers (',' variableDeclarationQualifier)* TERMINAL
    ;

enumType
    : 'enum' ID
    ;

variableDeclarationQualifiers
    : variableDeclarationQualifier (',' variableDeclarationQualifier)*
    ;

variableDeclarationQualifier
    : ID arraySpecifier? ('=' expression)?
    ;

arraySpecifier
    : '[' expression? ']' ( '[' expression? ']' )*
    ;

arrayInitializer
    : '{' (arrayInitializer | expression) (',' (arrayInitializer | expression))* '}'
    | '{' '}'
    ;

castExpression
    : '(' type ')' unaryExpression
    ;

switchStatement
    : SWITCH '(' expression ')' '{' caseStatement* defaultCaseStatement? '}'
    ;

caseStatement
    : CASE expression ':' statement*
    ;

defaultCaseStatement
    : DEFAULT ':' statement*
    ;

typedefStatement
    : 'typedef' type ID ';';

expressionStatement
    : expression ';'
    ;

expression
    : logicalExpression
    ;

assignmentStatement
    : expression assignmentOperator expression ';'
    ;

ifStatement
    : IF '(' expression ')' body (elseStatement)?
    ;

elseStatement
    : ELSE (body | ifStatement)
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
    | printfCall
    | '(' expression ')'
    | ID arraySpecifier?
    | CHAR
    | CHAR_ESC
    | STRING_LITERAL
    | arrayInitializer
    | castExpression
    | functionCall
    ;

type
    : const? (baseType | ID | enumType) addressQualifier*
    ;

baseType
    : 'int'
    | 'float'
    | 'char'
    | 'void'
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
SWITCH : 'switch' ;
CASE   : 'case' ;
DEFAULT: 'default' ;
IF     : 'if' ;
ELSE   : 'else' ;
BREAK : 'break' ;
RETURN : 'return' ;
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
STRING_LITERAL
    : '"' ( EscapeSequence | FormatSpecifier | ~('\\' | '"' | '%') )* '"'
    ;

fragment EscapeSequence
    : '\\' ( '"'    // Double quote
           | '\\'   // Backslash
           | 'n'    // Newline
           | 't'    // Tab
           | 'r'    // Carriage return
           | 'b'    // Backspace
           | 'f'    // Formfeed
           | 'u' HexDigit HexDigit HexDigit HexDigit  // Unicode
           | 'x' HexDigit HexDigit  // Hex code
           | OctalEscape  // Octal escape
           )
    ;

fragment FormatSpecifier
    : '%' [+-0#]* [0-9]* ('.' [0-9]+)? [diufFeEgGxXoscpaAn%]
    ;

fragment OctalEscape
    : [0-3] [0-7] [0-7]  // 3-digit octal
    | [0-7] [0-7]?       // 1 or 2-digit octal
    ;

fragment HexDigit
    : [0-9a-fA-F]  // Hexadecimal digit
    ;


WS     : [ \t\r\n]+ -> skip ;
SINGLE_LINE_COMMENT: '//' .*? ('\n' | EOF);
MULTI_LINE_COMMENT : '/*' .*? '*/' ;