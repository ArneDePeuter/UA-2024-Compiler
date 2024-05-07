grammar Expression;
import Type, Tokens;

expression
    : logicalOrExpression
    ;

logicalOrExpression
    : logicalAndExpression ( OrLogical logicalAndExpression )*
    ;

logicalAndExpression
    : inclusiveOrExpression ( AndLogical inclusiveOrExpression )*
    ;

inclusiveOrExpression
    : exclusiveOrExpression ( OrBit exclusiveOrExpression )*
    ;

exclusiveOrExpression
    : andExpression ( XorBit andExpression )*
    ;

andExpression
    : equalityExpression ( AndBit equalityExpression )*
    ;

equalityExpression
    : relationalExpression ( ( Equal | NotEqual ) relationalExpression )*
    ;

relationalExpression
    : shiftExpression ( (
            LessThan
        |   LessThanEqual
        |   GreaterThan
        |   GreaterThanEqual
        ) shiftExpression )*
    ;

shiftExpression
    : additiveExpression ( (
            ShiftLeft
        |   ShiftRight
        ) additiveExpression )*
    ;

additiveExpression
    : multiplicativeExpression ( (
            Plus
        |   Minus
        ) multiplicativeExpression )*
    ;

multiplicativeExpression
    : castExpression ( (
            Multiply
        |   Divide
        |   Modulus
        ) castExpression )*
    ;

castExpression
    : OpenParan type CloseParan castExpression
    | unaryExpression
    ;

unaryExpression
    : postfixExpression
    | unaryOperator castExpression
    ;

unaryOperator
    : AddressOf
    | Dereference
    | Plus
    | Minus
    | NotBit
    | NotLogical
    | PlusPlus
    | MinusMinus
    ;

postfixExpression
    : primaryExpression (
        OpenBracket logicalOrExpression CloseBracket
        | OpenParan argumentExpressionList CloseParan
        | DotOp Identifier
        | ArrowOp Identifier
        | PlusPlus
        | MinusMinus
    )*
    ;

primaryExpression
    : Identifier
    | Constant
    | StringLiteral
    | OpenParan expression CloseParan
    | initializerList
    ;

argumentExpressionList
    : logicalOrExpression ( Comma logicalOrExpression )*
    ;

initializerList
    : OpenBrace initializerListBody CloseBrace
    ;

initializerListBody
    : expression ( Comma expression )*
    ;