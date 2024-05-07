# Generated from Grammar.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .GrammarParser import GrammarParser
else:
    from GrammarParser import GrammarParser

# This class defines a complete listener for a parse tree produced by GrammarParser.
class GrammarListener(ParseTreeListener):

    # Enter a parse tree produced by GrammarParser#program.
    def enterProgram(self, ctx:GrammarParser.ProgramContext):
        pass

    # Exit a parse tree produced by GrammarParser#program.
    def exitProgram(self, ctx:GrammarParser.ProgramContext):
        pass


    # Enter a parse tree produced by GrammarParser#statement.
    def enterStatement(self, ctx:GrammarParser.StatementContext):
        pass

    # Exit a parse tree produced by GrammarParser#statement.
    def exitStatement(self, ctx:GrammarParser.StatementContext):
        pass


    # Enter a parse tree produced by GrammarParser#structDefinition.
    def enterStructDefinition(self, ctx:GrammarParser.StructDefinitionContext):
        pass

    # Exit a parse tree produced by GrammarParser#structDefinition.
    def exitStructDefinition(self, ctx:GrammarParser.StructDefinitionContext):
        pass


    # Enter a parse tree produced by GrammarParser#typedIdentifier.
    def enterTypedIdentifier(self, ctx:GrammarParser.TypedIdentifierContext):
        pass

    # Exit a parse tree produced by GrammarParser#typedIdentifier.
    def exitTypedIdentifier(self, ctx:GrammarParser.TypedIdentifierContext):
        pass


    # Enter a parse tree produced by GrammarParser#structList.
    def enterStructList(self, ctx:GrammarParser.StructListContext):
        pass

    # Exit a parse tree produced by GrammarParser#structList.
    def exitStructList(self, ctx:GrammarParser.StructListContext):
        pass


    # Enter a parse tree produced by GrammarParser#enumDeclaration.
    def enterEnumDeclaration(self, ctx:GrammarParser.EnumDeclarationContext):
        pass

    # Exit a parse tree produced by GrammarParser#enumDeclaration.
    def exitEnumDeclaration(self, ctx:GrammarParser.EnumDeclarationContext):
        pass


    # Enter a parse tree produced by GrammarParser#enumBody.
    def enterEnumBody(self, ctx:GrammarParser.EnumBodyContext):
        pass

    # Exit a parse tree produced by GrammarParser#enumBody.
    def exitEnumBody(self, ctx:GrammarParser.EnumBodyContext):
        pass


    # Enter a parse tree produced by GrammarParser#enumList.
    def enterEnumList(self, ctx:GrammarParser.EnumListContext):
        pass

    # Exit a parse tree produced by GrammarParser#enumList.
    def exitEnumList(self, ctx:GrammarParser.EnumListContext):
        pass


    # Enter a parse tree produced by GrammarParser#forwardDeclaration.
    def enterForwardDeclaration(self, ctx:GrammarParser.ForwardDeclarationContext):
        pass

    # Exit a parse tree produced by GrammarParser#forwardDeclaration.
    def exitForwardDeclaration(self, ctx:GrammarParser.ForwardDeclarationContext):
        pass


    # Enter a parse tree produced by GrammarParser#typeList.
    def enterTypeList(self, ctx:GrammarParser.TypeListContext):
        pass

    # Exit a parse tree produced by GrammarParser#typeList.
    def exitTypeList(self, ctx:GrammarParser.TypeListContext):
        pass


    # Enter a parse tree produced by GrammarParser#returnStatement.
    def enterReturnStatement(self, ctx:GrammarParser.ReturnStatementContext):
        pass

    # Exit a parse tree produced by GrammarParser#returnStatement.
    def exitReturnStatement(self, ctx:GrammarParser.ReturnStatementContext):
        pass


    # Enter a parse tree produced by GrammarParser#functionDeclaration.
    def enterFunctionDeclaration(self, ctx:GrammarParser.FunctionDeclarationContext):
        pass

    # Exit a parse tree produced by GrammarParser#functionDeclaration.
    def exitFunctionDeclaration(self, ctx:GrammarParser.FunctionDeclarationContext):
        pass


    # Enter a parse tree produced by GrammarParser#paramList.
    def enterParamList(self, ctx:GrammarParser.ParamListContext):
        pass

    # Exit a parse tree produced by GrammarParser#paramList.
    def exitParamList(self, ctx:GrammarParser.ParamListContext):
        pass


    # Enter a parse tree produced by GrammarParser#functionCall.
    def enterFunctionCall(self, ctx:GrammarParser.FunctionCallContext):
        pass

    # Exit a parse tree produced by GrammarParser#functionCall.
    def exitFunctionCall(self, ctx:GrammarParser.FunctionCallContext):
        pass


    # Enter a parse tree produced by GrammarParser#argumentList.
    def enterArgumentList(self, ctx:GrammarParser.ArgumentListContext):
        pass

    # Exit a parse tree produced by GrammarParser#argumentList.
    def exitArgumentList(self, ctx:GrammarParser.ArgumentListContext):
        pass


    # Enter a parse tree produced by GrammarParser#body.
    def enterBody(self, ctx:GrammarParser.BodyContext):
        pass

    # Exit a parse tree produced by GrammarParser#body.
    def exitBody(self, ctx:GrammarParser.BodyContext):
        pass


    # Enter a parse tree produced by GrammarParser#iterationStatement.
    def enterIterationStatement(self, ctx:GrammarParser.IterationStatementContext):
        pass

    # Exit a parse tree produced by GrammarParser#iterationStatement.
    def exitIterationStatement(self, ctx:GrammarParser.IterationStatementContext):
        pass


    # Enter a parse tree produced by GrammarParser#forCondition.
    def enterForCondition(self, ctx:GrammarParser.ForConditionContext):
        pass

    # Exit a parse tree produced by GrammarParser#forCondition.
    def exitForCondition(self, ctx:GrammarParser.ForConditionContext):
        pass


    # Enter a parse tree produced by GrammarParser#forFirst.
    def enterForFirst(self, ctx:GrammarParser.ForFirstContext):
        pass

    # Exit a parse tree produced by GrammarParser#forFirst.
    def exitForFirst(self, ctx:GrammarParser.ForFirstContext):
        pass


    # Enter a parse tree produced by GrammarParser#forSecond.
    def enterForSecond(self, ctx:GrammarParser.ForSecondContext):
        pass

    # Exit a parse tree produced by GrammarParser#forSecond.
    def exitForSecond(self, ctx:GrammarParser.ForSecondContext):
        pass


    # Enter a parse tree produced by GrammarParser#forThird.
    def enterForThird(self, ctx:GrammarParser.ForThirdContext):
        pass

    # Exit a parse tree produced by GrammarParser#forThird.
    def exitForThird(self, ctx:GrammarParser.ForThirdContext):
        pass


    # Enter a parse tree produced by GrammarParser#breakStatement.
    def enterBreakStatement(self, ctx:GrammarParser.BreakStatementContext):
        pass

    # Exit a parse tree produced by GrammarParser#breakStatement.
    def exitBreakStatement(self, ctx:GrammarParser.BreakStatementContext):
        pass


    # Enter a parse tree produced by GrammarParser#continueStatement.
    def enterContinueStatement(self, ctx:GrammarParser.ContinueStatementContext):
        pass

    # Exit a parse tree produced by GrammarParser#continueStatement.
    def exitContinueStatement(self, ctx:GrammarParser.ContinueStatementContext):
        pass


    # Enter a parse tree produced by GrammarParser#variableDeclaration.
    def enterVariableDeclaration(self, ctx:GrammarParser.VariableDeclarationContext):
        pass

    # Exit a parse tree produced by GrammarParser#variableDeclaration.
    def exitVariableDeclaration(self, ctx:GrammarParser.VariableDeclarationContext):
        pass


    # Enter a parse tree produced by GrammarParser#variableDeclarationQualifiers.
    def enterVariableDeclarationQualifiers(self, ctx:GrammarParser.VariableDeclarationQualifiersContext):
        pass

    # Exit a parse tree produced by GrammarParser#variableDeclarationQualifiers.
    def exitVariableDeclarationQualifiers(self, ctx:GrammarParser.VariableDeclarationQualifiersContext):
        pass


    # Enter a parse tree produced by GrammarParser#variableDeclarationQualifier.
    def enterVariableDeclarationQualifier(self, ctx:GrammarParser.VariableDeclarationQualifierContext):
        pass

    # Exit a parse tree produced by GrammarParser#variableDeclarationQualifier.
    def exitVariableDeclarationQualifier(self, ctx:GrammarParser.VariableDeclarationQualifierContext):
        pass


    # Enter a parse tree produced by GrammarParser#arraySpecifier.
    def enterArraySpecifier(self, ctx:GrammarParser.ArraySpecifierContext):
        pass

    # Exit a parse tree produced by GrammarParser#arraySpecifier.
    def exitArraySpecifier(self, ctx:GrammarParser.ArraySpecifierContext):
        pass


    # Enter a parse tree produced by GrammarParser#switchStatement.
    def enterSwitchStatement(self, ctx:GrammarParser.SwitchStatementContext):
        pass

    # Exit a parse tree produced by GrammarParser#switchStatement.
    def exitSwitchStatement(self, ctx:GrammarParser.SwitchStatementContext):
        pass


    # Enter a parse tree produced by GrammarParser#caseStatement.
    def enterCaseStatement(self, ctx:GrammarParser.CaseStatementContext):
        pass

    # Exit a parse tree produced by GrammarParser#caseStatement.
    def exitCaseStatement(self, ctx:GrammarParser.CaseStatementContext):
        pass


    # Enter a parse tree produced by GrammarParser#defaultCaseStatement.
    def enterDefaultCaseStatement(self, ctx:GrammarParser.DefaultCaseStatementContext):
        pass

    # Exit a parse tree produced by GrammarParser#defaultCaseStatement.
    def exitDefaultCaseStatement(self, ctx:GrammarParser.DefaultCaseStatementContext):
        pass


    # Enter a parse tree produced by GrammarParser#typedefStatement.
    def enterTypedefStatement(self, ctx:GrammarParser.TypedefStatementContext):
        pass

    # Exit a parse tree produced by GrammarParser#typedefStatement.
    def exitTypedefStatement(self, ctx:GrammarParser.TypedefStatementContext):
        pass


    # Enter a parse tree produced by GrammarParser#expressionStatement.
    def enterExpressionStatement(self, ctx:GrammarParser.ExpressionStatementContext):
        pass

    # Exit a parse tree produced by GrammarParser#expressionStatement.
    def exitExpressionStatement(self, ctx:GrammarParser.ExpressionStatementContext):
        pass


    # Enter a parse tree produced by GrammarParser#assignmentStatement.
    def enterAssignmentStatement(self, ctx:GrammarParser.AssignmentStatementContext):
        pass

    # Exit a parse tree produced by GrammarParser#assignmentStatement.
    def exitAssignmentStatement(self, ctx:GrammarParser.AssignmentStatementContext):
        pass


    # Enter a parse tree produced by GrammarParser#ifStatement.
    def enterIfStatement(self, ctx:GrammarParser.IfStatementContext):
        pass

    # Exit a parse tree produced by GrammarParser#ifStatement.
    def exitIfStatement(self, ctx:GrammarParser.IfStatementContext):
        pass


    # Enter a parse tree produced by GrammarParser#elseStatement.
    def enterElseStatement(self, ctx:GrammarParser.ElseStatementContext):
        pass

    # Exit a parse tree produced by GrammarParser#elseStatement.
    def exitElseStatement(self, ctx:GrammarParser.ElseStatementContext):
        pass


    # Enter a parse tree produced by GrammarParser#type.
    def enterType(self, ctx:GrammarParser.TypeContext):
        pass

    # Exit a parse tree produced by GrammarParser#type.
    def exitType(self, ctx:GrammarParser.TypeContext):
        pass


    # Enter a parse tree produced by GrammarParser#typedefType.
    def enterTypedefType(self, ctx:GrammarParser.TypedefTypeContext):
        pass

    # Exit a parse tree produced by GrammarParser#typedefType.
    def exitTypedefType(self, ctx:GrammarParser.TypedefTypeContext):
        pass


    # Enter a parse tree produced by GrammarParser#enumType.
    def enterEnumType(self, ctx:GrammarParser.EnumTypeContext):
        pass

    # Exit a parse tree produced by GrammarParser#enumType.
    def exitEnumType(self, ctx:GrammarParser.EnumTypeContext):
        pass


    # Enter a parse tree produced by GrammarParser#structType.
    def enterStructType(self, ctx:GrammarParser.StructTypeContext):
        pass

    # Exit a parse tree produced by GrammarParser#structType.
    def exitStructType(self, ctx:GrammarParser.StructTypeContext):
        pass


    # Enter a parse tree produced by GrammarParser#expression.
    def enterExpression(self, ctx:GrammarParser.ExpressionContext):
        pass

    # Exit a parse tree produced by GrammarParser#expression.
    def exitExpression(self, ctx:GrammarParser.ExpressionContext):
        pass


    # Enter a parse tree produced by GrammarParser#logicalOrExpression.
    def enterLogicalOrExpression(self, ctx:GrammarParser.LogicalOrExpressionContext):
        pass

    # Exit a parse tree produced by GrammarParser#logicalOrExpression.
    def exitLogicalOrExpression(self, ctx:GrammarParser.LogicalOrExpressionContext):
        pass


    # Enter a parse tree produced by GrammarParser#logicalAndExpression.
    def enterLogicalAndExpression(self, ctx:GrammarParser.LogicalAndExpressionContext):
        pass

    # Exit a parse tree produced by GrammarParser#logicalAndExpression.
    def exitLogicalAndExpression(self, ctx:GrammarParser.LogicalAndExpressionContext):
        pass


    # Enter a parse tree produced by GrammarParser#inclusiveOrExpression.
    def enterInclusiveOrExpression(self, ctx:GrammarParser.InclusiveOrExpressionContext):
        pass

    # Exit a parse tree produced by GrammarParser#inclusiveOrExpression.
    def exitInclusiveOrExpression(self, ctx:GrammarParser.InclusiveOrExpressionContext):
        pass


    # Enter a parse tree produced by GrammarParser#exclusiveOrExpression.
    def enterExclusiveOrExpression(self, ctx:GrammarParser.ExclusiveOrExpressionContext):
        pass

    # Exit a parse tree produced by GrammarParser#exclusiveOrExpression.
    def exitExclusiveOrExpression(self, ctx:GrammarParser.ExclusiveOrExpressionContext):
        pass


    # Enter a parse tree produced by GrammarParser#andExpression.
    def enterAndExpression(self, ctx:GrammarParser.AndExpressionContext):
        pass

    # Exit a parse tree produced by GrammarParser#andExpression.
    def exitAndExpression(self, ctx:GrammarParser.AndExpressionContext):
        pass


    # Enter a parse tree produced by GrammarParser#equalityExpression.
    def enterEqualityExpression(self, ctx:GrammarParser.EqualityExpressionContext):
        pass

    # Exit a parse tree produced by GrammarParser#equalityExpression.
    def exitEqualityExpression(self, ctx:GrammarParser.EqualityExpressionContext):
        pass


    # Enter a parse tree produced by GrammarParser#relationalExpression.
    def enterRelationalExpression(self, ctx:GrammarParser.RelationalExpressionContext):
        pass

    # Exit a parse tree produced by GrammarParser#relationalExpression.
    def exitRelationalExpression(self, ctx:GrammarParser.RelationalExpressionContext):
        pass


    # Enter a parse tree produced by GrammarParser#shiftExpression.
    def enterShiftExpression(self, ctx:GrammarParser.ShiftExpressionContext):
        pass

    # Exit a parse tree produced by GrammarParser#shiftExpression.
    def exitShiftExpression(self, ctx:GrammarParser.ShiftExpressionContext):
        pass


    # Enter a parse tree produced by GrammarParser#additiveExpression.
    def enterAdditiveExpression(self, ctx:GrammarParser.AdditiveExpressionContext):
        pass

    # Exit a parse tree produced by GrammarParser#additiveExpression.
    def exitAdditiveExpression(self, ctx:GrammarParser.AdditiveExpressionContext):
        pass


    # Enter a parse tree produced by GrammarParser#multiplicativeExpression.
    def enterMultiplicativeExpression(self, ctx:GrammarParser.MultiplicativeExpressionContext):
        pass

    # Exit a parse tree produced by GrammarParser#multiplicativeExpression.
    def exitMultiplicativeExpression(self, ctx:GrammarParser.MultiplicativeExpressionContext):
        pass


    # Enter a parse tree produced by GrammarParser#castExpression.
    def enterCastExpression(self, ctx:GrammarParser.CastExpressionContext):
        pass

    # Exit a parse tree produced by GrammarParser#castExpression.
    def exitCastExpression(self, ctx:GrammarParser.CastExpressionContext):
        pass


    # Enter a parse tree produced by GrammarParser#unaryExpression.
    def enterUnaryExpression(self, ctx:GrammarParser.UnaryExpressionContext):
        pass

    # Exit a parse tree produced by GrammarParser#unaryExpression.
    def exitUnaryExpression(self, ctx:GrammarParser.UnaryExpressionContext):
        pass


    # Enter a parse tree produced by GrammarParser#unaryOperator.
    def enterUnaryOperator(self, ctx:GrammarParser.UnaryOperatorContext):
        pass

    # Exit a parse tree produced by GrammarParser#unaryOperator.
    def exitUnaryOperator(self, ctx:GrammarParser.UnaryOperatorContext):
        pass


    # Enter a parse tree produced by GrammarParser#postfixExpression.
    def enterPostfixExpression(self, ctx:GrammarParser.PostfixExpressionContext):
        pass

    # Exit a parse tree produced by GrammarParser#postfixExpression.
    def exitPostfixExpression(self, ctx:GrammarParser.PostfixExpressionContext):
        pass


    # Enter a parse tree produced by GrammarParser#primaryExpression.
    def enterPrimaryExpression(self, ctx:GrammarParser.PrimaryExpressionContext):
        pass

    # Exit a parse tree produced by GrammarParser#primaryExpression.
    def exitPrimaryExpression(self, ctx:GrammarParser.PrimaryExpressionContext):
        pass


    # Enter a parse tree produced by GrammarParser#argumentExpressionList.
    def enterArgumentExpressionList(self, ctx:GrammarParser.ArgumentExpressionListContext):
        pass

    # Exit a parse tree produced by GrammarParser#argumentExpressionList.
    def exitArgumentExpressionList(self, ctx:GrammarParser.ArgumentExpressionListContext):
        pass


    # Enter a parse tree produced by GrammarParser#initializerList.
    def enterInitializerList(self, ctx:GrammarParser.InitializerListContext):
        pass

    # Exit a parse tree produced by GrammarParser#initializerList.
    def exitInitializerList(self, ctx:GrammarParser.InitializerListContext):
        pass


    # Enter a parse tree produced by GrammarParser#initializerListBody.
    def enterInitializerListBody(self, ctx:GrammarParser.InitializerListBodyContext):
        pass

    # Exit a parse tree produced by GrammarParser#initializerListBody.
    def exitInitializerListBody(self, ctx:GrammarParser.InitializerListBodyContext):
        pass



del GrammarParser