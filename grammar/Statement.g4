grammar Statement;
import Type, Expression, Tokens;

statement
    : body
    | forwardDeclaration
    | functionDeclaration
    | variableDeclaration
    | enumDeclaration
    | assignmentStatement
    | typedefStatement
    | ifStatement
    | iterationStatement
    | breakStatement
    | continueStatement
    | switchStatement
    | returnStatement
    | expressionStatement
    | structDefinition
    | Delimiter
    | Comment
    ;


structDefinition: Struct Identifier OpenBrace structList? CloseBrace Delimiter ;

typedIdentifier : type Identifier arraySpecifier?;

structList: typedIdentifier Delimiter (typedIdentifier Delimiter)* ;

enumDeclaration
    : Enum Identifier? OpenBrace enumBody CloseBrace
    ;

enumBody
    : enumList? (Comment? Comma enumList)* Comment? Comma?
    ;

enumList
    : Identifier (Equals expression)? (Comma Comment? Identifier (Equals expression)?)* Comma? Comment?
    ;

forwardDeclaration : typedIdentifier OpenParan typeList? CloseParan Delimiter ;

typeList : type Identifier? arraySpecifier? (Comma type Identifier? arraySpecifier?)* ;

returnStatement : Return expression? Delimiter ;

functionDeclaration : type Identifier OpenParan paramList? CloseParan body ;

paramList : typedIdentifier (Comma typedIdentifier)* ;

argumentList : expression (Comma expression)* ;

body : OpenBrace statement* CloseBrace ;

iterationStatement
    : While OpenParan expression CloseParan statement
    | For OpenParan forCondition CloseParan statement
    ;

forCondition
    : forFirst forSecond forThird
    ;

forFirst
    : variableDeclaration
    | assignmentStatement
    | expressionStatement
    | Delimiter
    ;

forSecond
    : expressionStatement
    | Delimiter
    ;

forThird
    : expression?
    ;

breakStatement
    : Break Delimiter
    ;

continueStatement
    : Continue Delimiter
    ;

variableDeclaration
    : type variableDeclarationQualifiers (Comma variableDeclarationQualifier)* Delimiter
    ;

variableDeclarationQualifiers
    : variableDeclarationQualifier (Comma variableDeclarationQualifier)*
    ;

variableDeclarationQualifier
    : Identifier arraySpecifier? (Equals expression)?
    ;

arraySpecifier
    : OpenBracket expression? CloseBracket ( OpenBracket expression? CloseBracket )*
    ;

switchStatement
    : Switch OpenParan expression CloseParan OpenBrace caseStatement* defaultCaseStatement? CloseBrace
    ;

caseStatement
    : Case expression Colon statement*
    ;

defaultCaseStatement
    : Default Colon statement*
    ;

typedefStatement
    : Typedef type Identifier Delimiter;

expressionStatement
    : expression Delimiter
    ;

assignmentStatement
    : expression Equals expression Delimiter
    ;

ifStatement
    : If OpenParan expression CloseParan body (elseStatement)?
    ;

elseStatement
    : Else (body | ifStatement)
    ;
