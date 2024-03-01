# Generated from MyGrammar.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,49,212,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,1,0,1,0,1,1,1,1,1,1,
        1,1,1,1,1,1,1,2,1,2,5,2,61,8,2,10,2,12,2,64,9,2,1,2,1,2,1,3,1,3,
        1,3,1,3,1,4,1,4,1,4,3,4,75,8,4,1,5,1,5,1,5,1,6,1,6,3,6,82,8,6,1,
        7,1,7,1,8,1,8,1,9,1,9,1,9,1,9,1,9,3,9,93,8,9,1,10,1,10,1,10,1,10,
        1,10,1,10,5,10,101,8,10,10,10,12,10,104,9,10,1,11,1,11,1,11,1,11,
        1,11,1,11,5,11,112,8,11,10,11,12,11,115,9,11,1,12,1,12,1,12,1,12,
        1,12,1,12,5,12,123,8,12,10,12,12,12,126,9,12,1,13,1,13,1,13,1,13,
        1,13,1,13,5,13,134,8,13,10,13,12,13,137,9,13,1,14,1,14,1,14,1,14,
        1,14,1,14,5,14,145,8,14,10,14,12,14,148,9,14,1,15,1,15,1,15,1,15,
        1,15,1,15,5,15,156,8,15,10,15,12,15,159,9,15,1,16,1,16,1,16,1,16,
        3,16,165,8,16,3,16,167,8,16,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,
        17,3,17,177,8,17,1,18,3,18,180,8,18,1,18,1,18,5,18,184,8,18,10,18,
        12,18,187,9,18,1,19,1,19,1,20,1,20,1,21,1,21,1,22,1,22,1,22,5,22,
        198,8,22,10,22,12,22,201,9,22,3,22,203,8,22,1,23,1,23,1,23,3,23,
        208,8,23,1,24,1,24,1,24,0,6,20,22,24,26,28,30,25,0,2,4,6,8,10,12,
        14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,0,10,1,0,40,
        41,1,0,34,39,1,0,29,30,1,0,31,33,1,0,45,47,1,0,43,44,4,0,8,9,29,
        31,42,42,45,45,1,0,8,9,2,0,1,1,10,11,1,0,14,24,208,0,50,1,0,0,0,
        2,52,1,0,0,0,4,58,1,0,0,0,6,67,1,0,0,0,8,74,1,0,0,0,10,76,1,0,0,
        0,12,81,1,0,0,0,14,83,1,0,0,0,16,85,1,0,0,0,18,92,1,0,0,0,20,94,
        1,0,0,0,22,105,1,0,0,0,24,116,1,0,0,0,26,127,1,0,0,0,28,138,1,0,
        0,0,30,149,1,0,0,0,32,166,1,0,0,0,34,176,1,0,0,0,36,179,1,0,0,0,
        38,188,1,0,0,0,40,190,1,0,0,0,42,192,1,0,0,0,44,202,1,0,0,0,46,204,
        1,0,0,0,48,209,1,0,0,0,50,51,3,2,1,0,51,1,1,0,0,0,52,53,5,1,0,0,
        53,54,5,2,0,0,54,55,5,3,0,0,55,56,5,4,0,0,56,57,3,4,2,0,57,3,1,0,
        0,0,58,62,5,5,0,0,59,61,3,8,4,0,60,59,1,0,0,0,61,64,1,0,0,0,62,60,
        1,0,0,0,62,63,1,0,0,0,63,65,1,0,0,0,64,62,1,0,0,0,65,66,5,6,0,0,
        66,5,1,0,0,0,67,68,3,36,18,0,68,69,3,44,22,0,69,70,5,7,0,0,70,7,
        1,0,0,0,71,75,3,10,5,0,72,75,3,4,2,0,73,75,3,6,3,0,74,71,1,0,0,0,
        74,72,1,0,0,0,74,73,1,0,0,0,75,9,1,0,0,0,76,77,3,12,6,0,77,78,5,
        7,0,0,78,11,1,0,0,0,79,82,3,14,7,0,80,82,3,16,8,0,81,79,1,0,0,0,
        81,80,1,0,0,0,82,13,1,0,0,0,83,84,3,18,9,0,84,15,1,0,0,0,85,86,3,
        20,10,0,86,17,1,0,0,0,87,88,3,32,16,0,88,89,3,48,24,0,89,90,3,12,
        6,0,90,93,1,0,0,0,91,93,3,20,10,0,92,87,1,0,0,0,92,91,1,0,0,0,93,
        19,1,0,0,0,94,95,6,10,-1,0,95,96,3,22,11,0,96,102,1,0,0,0,97,98,
        10,2,0,0,98,99,7,0,0,0,99,101,3,22,11,0,100,97,1,0,0,0,101,104,1,
        0,0,0,102,100,1,0,0,0,102,103,1,0,0,0,103,21,1,0,0,0,104,102,1,0,
        0,0,105,106,6,11,-1,0,106,107,3,24,12,0,107,113,1,0,0,0,108,109,
        10,2,0,0,109,110,7,1,0,0,110,112,3,24,12,0,111,108,1,0,0,0,112,115,
        1,0,0,0,113,111,1,0,0,0,113,114,1,0,0,0,114,23,1,0,0,0,115,113,1,
        0,0,0,116,117,6,12,-1,0,117,118,3,26,13,0,118,124,1,0,0,0,119,120,
        10,2,0,0,120,121,7,2,0,0,121,123,3,26,13,0,122,119,1,0,0,0,123,126,
        1,0,0,0,124,122,1,0,0,0,124,125,1,0,0,0,125,25,1,0,0,0,126,124,1,
        0,0,0,127,128,6,13,-1,0,128,129,3,28,14,0,129,135,1,0,0,0,130,131,
        10,2,0,0,131,132,7,3,0,0,132,134,3,28,14,0,133,130,1,0,0,0,134,137,
        1,0,0,0,135,133,1,0,0,0,135,136,1,0,0,0,136,27,1,0,0,0,137,135,1,
        0,0,0,138,139,6,14,-1,0,139,140,3,30,15,0,140,146,1,0,0,0,141,142,
        10,2,0,0,142,143,7,4,0,0,143,145,3,30,15,0,144,141,1,0,0,0,145,148,
        1,0,0,0,146,144,1,0,0,0,146,147,1,0,0,0,147,29,1,0,0,0,148,146,1,
        0,0,0,149,150,6,15,-1,0,150,151,3,32,16,0,151,157,1,0,0,0,152,153,
        10,2,0,0,153,154,7,5,0,0,154,156,3,32,16,0,155,152,1,0,0,0,156,159,
        1,0,0,0,157,155,1,0,0,0,157,158,1,0,0,0,158,31,1,0,0,0,159,157,1,
        0,0,0,160,161,7,6,0,0,161,167,3,32,16,0,162,164,3,34,17,0,163,165,
        7,7,0,0,164,163,1,0,0,0,164,165,1,0,0,0,165,167,1,0,0,0,166,160,
        1,0,0,0,166,162,1,0,0,0,167,33,1,0,0,0,168,177,5,25,0,0,169,177,
        5,26,0,0,170,171,5,3,0,0,171,172,3,12,6,0,172,173,5,4,0,0,173,177,
        1,0,0,0,174,177,5,27,0,0,175,177,5,28,0,0,176,168,1,0,0,0,176,169,
        1,0,0,0,176,170,1,0,0,0,176,174,1,0,0,0,176,175,1,0,0,0,177,35,1,
        0,0,0,178,180,3,40,20,0,179,178,1,0,0,0,179,180,1,0,0,0,180,181,
        1,0,0,0,181,185,3,38,19,0,182,184,3,42,21,0,183,182,1,0,0,0,184,
        187,1,0,0,0,185,183,1,0,0,0,185,186,1,0,0,0,186,37,1,0,0,0,187,185,
        1,0,0,0,188,189,7,8,0,0,189,39,1,0,0,0,190,191,5,12,0,0,191,41,1,
        0,0,0,192,193,5,31,0,0,193,43,1,0,0,0,194,199,3,46,23,0,195,196,
        5,13,0,0,196,198,3,46,23,0,197,195,1,0,0,0,198,201,1,0,0,0,199,197,
        1,0,0,0,199,200,1,0,0,0,200,203,1,0,0,0,201,199,1,0,0,0,202,194,
        1,0,0,0,202,203,1,0,0,0,203,45,1,0,0,0,204,207,5,27,0,0,205,206,
        5,14,0,0,206,208,3,12,6,0,207,205,1,0,0,0,207,208,1,0,0,0,208,47,
        1,0,0,0,209,210,7,9,0,0,210,49,1,0,0,0,18,62,74,81,92,102,113,124,
        135,146,157,164,166,176,179,185,199,202,207
    ]

class MyGrammarParser ( Parser ):

    grammarFileName = "MyGrammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'int'", "'main'", "'('", "')'", "'{'", 
                     "'}'", "';'", "'++'", "'--'", "'float'", "'char'", 
                     "'const'", "','", "'='", "'+='", "'-='", "'*='", "'/='", 
                     "'%='", "'<<='", "'>>='", "'&='", "'^='", "'|='", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'+'", "'-'", 
                     "'*'", "'/'", "'%'", "'>'", "'<'", "'=='", "'>='", 
                     "'<='", "'!='", "'&&'", "'||'", "'!'", "'<<'", "'>>'", 
                     "'&'", "'|'", "'^'", "'~'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "NUMBER", "FLOAT", "ID", "CHAR", "PLUS", 
                      "MINUS", "MUL", "DIV", "MOD", "GT", "LT", "EQ", "GE", 
                      "LE", "NE", "AND", "OR", "NOT", "LSHIFT", "RSHIFT", 
                      "BITAND", "BITOR", "BITXOR", "BITNOT", "WS" ]

    RULE_program = 0
    RULE_mainFunction = 1
    RULE_compoundStatement = 2
    RULE_declaration = 3
    RULE_statement = 4
    RULE_expressionStatement = 5
    RULE_expression = 6
    RULE_mutableExpression = 7
    RULE_immutableExpression = 8
    RULE_assignmentExpression = 9
    RULE_logicalExpression = 10
    RULE_comparisonExpression = 11
    RULE_additiveExpression = 12
    RULE_multiplicativeExpression = 13
    RULE_bitwiseExpression = 14
    RULE_shiftExpression = 15
    RULE_unaryExpression = 16
    RULE_primary = 17
    RULE_type = 18
    RULE_baseType = 19
    RULE_typeQualifier = 20
    RULE_pointerQualifier = 21
    RULE_variableList = 22
    RULE_variable = 23
    RULE_assignmentOperator = 24

    ruleNames =  [ "program", "mainFunction", "compoundStatement", "declaration", 
                   "statement", "expressionStatement", "expression", "mutableExpression", 
                   "immutableExpression", "assignmentExpression", "logicalExpression", 
                   "comparisonExpression", "additiveExpression", "multiplicativeExpression", 
                   "bitwiseExpression", "shiftExpression", "unaryExpression", 
                   "primary", "type", "baseType", "typeQualifier", "pointerQualifier", 
                   "variableList", "variable", "assignmentOperator" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    NUMBER=25
    FLOAT=26
    ID=27
    CHAR=28
    PLUS=29
    MINUS=30
    MUL=31
    DIV=32
    MOD=33
    GT=34
    LT=35
    EQ=36
    GE=37
    LE=38
    NE=39
    AND=40
    OR=41
    NOT=42
    LSHIFT=43
    RSHIFT=44
    BITAND=45
    BITOR=46
    BITXOR=47
    BITNOT=48
    WS=49

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def mainFunction(self):
            return self.getTypedRuleContext(MyGrammarParser.MainFunctionContext,0)


        def getRuleIndex(self):
            return MyGrammarParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = MyGrammarParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 50
            self.mainFunction()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MainFunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def compoundStatement(self):
            return self.getTypedRuleContext(MyGrammarParser.CompoundStatementContext,0)


        def getRuleIndex(self):
            return MyGrammarParser.RULE_mainFunction

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMainFunction" ):
                listener.enterMainFunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMainFunction" ):
                listener.exitMainFunction(self)




    def mainFunction(self):

        localctx = MyGrammarParser.MainFunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_mainFunction)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52
            self.match(MyGrammarParser.T__0)
            self.state = 53
            self.match(MyGrammarParser.T__1)
            self.state = 54
            self.match(MyGrammarParser.T__2)
            self.state = 55
            self.match(MyGrammarParser.T__3)
            self.state = 56
            self.compoundStatement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CompoundStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyGrammarParser.StatementContext)
            else:
                return self.getTypedRuleContext(MyGrammarParser.StatementContext,i)


        def getRuleIndex(self):
            return MyGrammarParser.RULE_compoundStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCompoundStatement" ):
                listener.enterCompoundStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCompoundStatement" ):
                listener.exitCompoundStatement(self)




    def compoundStatement(self):

        localctx = MyGrammarParser.CompoundStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_compoundStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58
            self.match(MyGrammarParser.T__4)
            self.state = 62
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 39586680020778) != 0):
                self.state = 59
                self.statement()
                self.state = 64
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 65
            self.match(MyGrammarParser.T__5)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(MyGrammarParser.TypeContext,0)


        def variableList(self):
            return self.getTypedRuleContext(MyGrammarParser.VariableListContext,0)


        def getRuleIndex(self):
            return MyGrammarParser.RULE_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaration" ):
                listener.enterDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaration" ):
                listener.exitDeclaration(self)




    def declaration(self):

        localctx = MyGrammarParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 67
            self.type_()
            self.state = 68
            self.variableList()
            self.state = 69
            self.match(MyGrammarParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expressionStatement(self):
            return self.getTypedRuleContext(MyGrammarParser.ExpressionStatementContext,0)


        def compoundStatement(self):
            return self.getTypedRuleContext(MyGrammarParser.CompoundStatementContext,0)


        def declaration(self):
            return self.getTypedRuleContext(MyGrammarParser.DeclarationContext,0)


        def getRuleIndex(self):
            return MyGrammarParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




    def statement(self):

        localctx = MyGrammarParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_statement)
        try:
            self.state = 74
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3, 8, 9, 25, 26, 27, 28, 29, 30, 31, 42, 45]:
                self.enterOuterAlt(localctx, 1)
                self.state = 71
                self.expressionStatement()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 2)
                self.state = 72
                self.compoundStatement()
                pass
            elif token in [1, 10, 11, 12]:
                self.enterOuterAlt(localctx, 3)
                self.state = 73
                self.declaration()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(MyGrammarParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MyGrammarParser.RULE_expressionStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressionStatement" ):
                listener.enterExpressionStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressionStatement" ):
                listener.exitExpressionStatement(self)




    def expressionStatement(self):

        localctx = MyGrammarParser.ExpressionStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_expressionStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 76
            self.expression()
            self.state = 77
            self.match(MyGrammarParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def mutableExpression(self):
            return self.getTypedRuleContext(MyGrammarParser.MutableExpressionContext,0)


        def immutableExpression(self):
            return self.getTypedRuleContext(MyGrammarParser.ImmutableExpressionContext,0)


        def getRuleIndex(self):
            return MyGrammarParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)




    def expression(self):

        localctx = MyGrammarParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_expression)
        try:
            self.state = 81
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 79
                self.mutableExpression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 80
                self.immutableExpression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MutableExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignmentExpression(self):
            return self.getTypedRuleContext(MyGrammarParser.AssignmentExpressionContext,0)


        def getRuleIndex(self):
            return MyGrammarParser.RULE_mutableExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMutableExpression" ):
                listener.enterMutableExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMutableExpression" ):
                listener.exitMutableExpression(self)




    def mutableExpression(self):

        localctx = MyGrammarParser.MutableExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_mutableExpression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83
            self.assignmentExpression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ImmutableExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def logicalExpression(self):
            return self.getTypedRuleContext(MyGrammarParser.LogicalExpressionContext,0)


        def getRuleIndex(self):
            return MyGrammarParser.RULE_immutableExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterImmutableExpression" ):
                listener.enterImmutableExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitImmutableExpression" ):
                listener.exitImmutableExpression(self)




    def immutableExpression(self):

        localctx = MyGrammarParser.ImmutableExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_immutableExpression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 85
            self.logicalExpression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unaryExpression(self):
            return self.getTypedRuleContext(MyGrammarParser.UnaryExpressionContext,0)


        def assignmentOperator(self):
            return self.getTypedRuleContext(MyGrammarParser.AssignmentOperatorContext,0)


        def expression(self):
            return self.getTypedRuleContext(MyGrammarParser.ExpressionContext,0)


        def logicalExpression(self):
            return self.getTypedRuleContext(MyGrammarParser.LogicalExpressionContext,0)


        def getRuleIndex(self):
            return MyGrammarParser.RULE_assignmentExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignmentExpression" ):
                listener.enterAssignmentExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignmentExpression" ):
                listener.exitAssignmentExpression(self)




    def assignmentExpression(self):

        localctx = MyGrammarParser.AssignmentExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_assignmentExpression)
        try:
            self.state = 92
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 87
                self.unaryExpression()
                self.state = 88
                self.assignmentOperator()
                self.state = 89
                self.expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 91
                self.logicalExpression(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LogicalExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def comparisonExpression(self):
            return self.getTypedRuleContext(MyGrammarParser.ComparisonExpressionContext,0)


        def logicalExpression(self):
            return self.getTypedRuleContext(MyGrammarParser.LogicalExpressionContext,0)


        def AND(self):
            return self.getToken(MyGrammarParser.AND, 0)

        def OR(self):
            return self.getToken(MyGrammarParser.OR, 0)

        def getRuleIndex(self):
            return MyGrammarParser.RULE_logicalExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogicalExpression" ):
                listener.enterLogicalExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogicalExpression" ):
                listener.exitLogicalExpression(self)



    def logicalExpression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MyGrammarParser.LogicalExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 20
        self.enterRecursionRule(localctx, 20, self.RULE_logicalExpression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 95
            self.comparisonExpression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 102
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MyGrammarParser.LogicalExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_logicalExpression)
                    self.state = 97
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 98
                    _la = self._input.LA(1)
                    if not(_la==40 or _la==41):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 99
                    self.comparisonExpression(0) 
                self.state = 104
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ComparisonExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def additiveExpression(self):
            return self.getTypedRuleContext(MyGrammarParser.AdditiveExpressionContext,0)


        def comparisonExpression(self):
            return self.getTypedRuleContext(MyGrammarParser.ComparisonExpressionContext,0)


        def GT(self):
            return self.getToken(MyGrammarParser.GT, 0)

        def LT(self):
            return self.getToken(MyGrammarParser.LT, 0)

        def EQ(self):
            return self.getToken(MyGrammarParser.EQ, 0)

        def GE(self):
            return self.getToken(MyGrammarParser.GE, 0)

        def LE(self):
            return self.getToken(MyGrammarParser.LE, 0)

        def NE(self):
            return self.getToken(MyGrammarParser.NE, 0)

        def getRuleIndex(self):
            return MyGrammarParser.RULE_comparisonExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparisonExpression" ):
                listener.enterComparisonExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparisonExpression" ):
                listener.exitComparisonExpression(self)



    def comparisonExpression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MyGrammarParser.ComparisonExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 22
        self.enterRecursionRule(localctx, 22, self.RULE_comparisonExpression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 106
            self.additiveExpression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 113
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MyGrammarParser.ComparisonExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_comparisonExpression)
                    self.state = 108
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 109
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1082331758592) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 110
                    self.additiveExpression(0) 
                self.state = 115
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class AdditiveExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def multiplicativeExpression(self):
            return self.getTypedRuleContext(MyGrammarParser.MultiplicativeExpressionContext,0)


        def additiveExpression(self):
            return self.getTypedRuleContext(MyGrammarParser.AdditiveExpressionContext,0)


        def PLUS(self):
            return self.getToken(MyGrammarParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(MyGrammarParser.MINUS, 0)

        def getRuleIndex(self):
            return MyGrammarParser.RULE_additiveExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAdditiveExpression" ):
                listener.enterAdditiveExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAdditiveExpression" ):
                listener.exitAdditiveExpression(self)



    def additiveExpression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MyGrammarParser.AdditiveExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 24
        self.enterRecursionRule(localctx, 24, self.RULE_additiveExpression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 117
            self.multiplicativeExpression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 124
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MyGrammarParser.AdditiveExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_additiveExpression)
                    self.state = 119
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 120
                    _la = self._input.LA(1)
                    if not(_la==29 or _la==30):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 121
                    self.multiplicativeExpression(0) 
                self.state = 126
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class MultiplicativeExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def bitwiseExpression(self):
            return self.getTypedRuleContext(MyGrammarParser.BitwiseExpressionContext,0)


        def multiplicativeExpression(self):
            return self.getTypedRuleContext(MyGrammarParser.MultiplicativeExpressionContext,0)


        def MUL(self):
            return self.getToken(MyGrammarParser.MUL, 0)

        def DIV(self):
            return self.getToken(MyGrammarParser.DIV, 0)

        def MOD(self):
            return self.getToken(MyGrammarParser.MOD, 0)

        def getRuleIndex(self):
            return MyGrammarParser.RULE_multiplicativeExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultiplicativeExpression" ):
                listener.enterMultiplicativeExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultiplicativeExpression" ):
                listener.exitMultiplicativeExpression(self)



    def multiplicativeExpression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MyGrammarParser.MultiplicativeExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 26
        self.enterRecursionRule(localctx, 26, self.RULE_multiplicativeExpression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 128
            self.bitwiseExpression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 135
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MyGrammarParser.MultiplicativeExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_multiplicativeExpression)
                    self.state = 130
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 131
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 15032385536) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 132
                    self.bitwiseExpression(0) 
                self.state = 137
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class BitwiseExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def shiftExpression(self):
            return self.getTypedRuleContext(MyGrammarParser.ShiftExpressionContext,0)


        def bitwiseExpression(self):
            return self.getTypedRuleContext(MyGrammarParser.BitwiseExpressionContext,0)


        def BITAND(self):
            return self.getToken(MyGrammarParser.BITAND, 0)

        def BITOR(self):
            return self.getToken(MyGrammarParser.BITOR, 0)

        def BITXOR(self):
            return self.getToken(MyGrammarParser.BITXOR, 0)

        def getRuleIndex(self):
            return MyGrammarParser.RULE_bitwiseExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBitwiseExpression" ):
                listener.enterBitwiseExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBitwiseExpression" ):
                listener.exitBitwiseExpression(self)



    def bitwiseExpression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MyGrammarParser.BitwiseExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 28
        self.enterRecursionRule(localctx, 28, self.RULE_bitwiseExpression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 139
            self.shiftExpression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 146
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MyGrammarParser.BitwiseExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_bitwiseExpression)
                    self.state = 141
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 142
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 246290604621824) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 143
                    self.shiftExpression(0) 
                self.state = 148
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ShiftExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unaryExpression(self):
            return self.getTypedRuleContext(MyGrammarParser.UnaryExpressionContext,0)


        def shiftExpression(self):
            return self.getTypedRuleContext(MyGrammarParser.ShiftExpressionContext,0)


        def LSHIFT(self):
            return self.getToken(MyGrammarParser.LSHIFT, 0)

        def RSHIFT(self):
            return self.getToken(MyGrammarParser.RSHIFT, 0)

        def getRuleIndex(self):
            return MyGrammarParser.RULE_shiftExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterShiftExpression" ):
                listener.enterShiftExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitShiftExpression" ):
                listener.exitShiftExpression(self)



    def shiftExpression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MyGrammarParser.ShiftExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 30
        self.enterRecursionRule(localctx, 30, self.RULE_shiftExpression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 150
            self.unaryExpression()
            self._ctx.stop = self._input.LT(-1)
            self.state = 157
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MyGrammarParser.ShiftExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_shiftExpression)
                    self.state = 152
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 153
                    _la = self._input.LA(1)
                    if not(_la==43 or _la==44):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 154
                    self.unaryExpression() 
                self.state = 159
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class UnaryExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unaryExpression(self):
            return self.getTypedRuleContext(MyGrammarParser.UnaryExpressionContext,0)


        def PLUS(self):
            return self.getToken(MyGrammarParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(MyGrammarParser.MINUS, 0)

        def NOT(self):
            return self.getToken(MyGrammarParser.NOT, 0)

        def MUL(self):
            return self.getToken(MyGrammarParser.MUL, 0)

        def BITAND(self):
            return self.getToken(MyGrammarParser.BITAND, 0)

        def primary(self):
            return self.getTypedRuleContext(MyGrammarParser.PrimaryContext,0)


        def getRuleIndex(self):
            return MyGrammarParser.RULE_unaryExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnaryExpression" ):
                listener.enterUnaryExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnaryExpression" ):
                listener.exitUnaryExpression(self)




    def unaryExpression(self):

        localctx = MyGrammarParser.UnaryExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_unaryExpression)
        self._la = 0 # Token type
        try:
            self.state = 166
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8, 9, 29, 30, 31, 42, 45]:
                self.enterOuterAlt(localctx, 1)
                self.state = 160
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 39586176697088) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 161
                self.unaryExpression()
                pass
            elif token in [3, 25, 26, 27, 28]:
                self.enterOuterAlt(localctx, 2)
                self.state = 162
                self.primary()
                self.state = 164
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
                if la_ == 1:
                    self.state = 163
                    _la = self._input.LA(1)
                    if not(_la==8 or _la==9):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()


                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrimaryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(MyGrammarParser.NUMBER, 0)

        def FLOAT(self):
            return self.getToken(MyGrammarParser.FLOAT, 0)

        def expression(self):
            return self.getTypedRuleContext(MyGrammarParser.ExpressionContext,0)


        def ID(self):
            return self.getToken(MyGrammarParser.ID, 0)

        def CHAR(self):
            return self.getToken(MyGrammarParser.CHAR, 0)

        def getRuleIndex(self):
            return MyGrammarParser.RULE_primary

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimary" ):
                listener.enterPrimary(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimary" ):
                listener.exitPrimary(self)




    def primary(self):

        localctx = MyGrammarParser.PrimaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_primary)
        try:
            self.state = 176
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [25]:
                self.enterOuterAlt(localctx, 1)
                self.state = 168
                self.match(MyGrammarParser.NUMBER)
                pass
            elif token in [26]:
                self.enterOuterAlt(localctx, 2)
                self.state = 169
                self.match(MyGrammarParser.FLOAT)
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 3)
                self.state = 170
                self.match(MyGrammarParser.T__2)
                self.state = 171
                self.expression()
                self.state = 172
                self.match(MyGrammarParser.T__3)
                pass
            elif token in [27]:
                self.enterOuterAlt(localctx, 4)
                self.state = 174
                self.match(MyGrammarParser.ID)
                pass
            elif token in [28]:
                self.enterOuterAlt(localctx, 5)
                self.state = 175
                self.match(MyGrammarParser.CHAR)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def baseType(self):
            return self.getTypedRuleContext(MyGrammarParser.BaseTypeContext,0)


        def typeQualifier(self):
            return self.getTypedRuleContext(MyGrammarParser.TypeQualifierContext,0)


        def pointerQualifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyGrammarParser.PointerQualifierContext)
            else:
                return self.getTypedRuleContext(MyGrammarParser.PointerQualifierContext,i)


        def getRuleIndex(self):
            return MyGrammarParser.RULE_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType" ):
                listener.enterType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType" ):
                listener.exitType(self)




    def type_(self):

        localctx = MyGrammarParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 179
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==12:
                self.state = 178
                self.typeQualifier()


            self.state = 181
            self.baseType()
            self.state = 185
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==31:
                self.state = 182
                self.pointerQualifier()
                self.state = 187
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BaseTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MyGrammarParser.RULE_baseType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBaseType" ):
                listener.enterBaseType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBaseType" ):
                listener.exitBaseType(self)




    def baseType(self):

        localctx = MyGrammarParser.BaseTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_baseType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 188
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 3074) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeQualifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MyGrammarParser.RULE_typeQualifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeQualifier" ):
                listener.enterTypeQualifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeQualifier" ):
                listener.exitTypeQualifier(self)




    def typeQualifier(self):

        localctx = MyGrammarParser.TypeQualifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_typeQualifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 190
            self.match(MyGrammarParser.T__11)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PointerQualifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MUL(self):
            return self.getToken(MyGrammarParser.MUL, 0)

        def getRuleIndex(self):
            return MyGrammarParser.RULE_pointerQualifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPointerQualifier" ):
                listener.enterPointerQualifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPointerQualifier" ):
                listener.exitPointerQualifier(self)




    def pointerQualifier(self):

        localctx = MyGrammarParser.PointerQualifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_pointerQualifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 192
            self.match(MyGrammarParser.MUL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyGrammarParser.VariableContext)
            else:
                return self.getTypedRuleContext(MyGrammarParser.VariableContext,i)


        def getRuleIndex(self):
            return MyGrammarParser.RULE_variableList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariableList" ):
                listener.enterVariableList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariableList" ):
                listener.exitVariableList(self)




    def variableList(self):

        localctx = MyGrammarParser.VariableListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_variableList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 202
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==27:
                self.state = 194
                self.variable()
                self.state = 199
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==13:
                    self.state = 195
                    self.match(MyGrammarParser.T__12)
                    self.state = 196
                    self.variable()
                    self.state = 201
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MyGrammarParser.ID, 0)

        def expression(self):
            return self.getTypedRuleContext(MyGrammarParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MyGrammarParser.RULE_variable

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariable" ):
                listener.enterVariable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariable" ):
                listener.exitVariable(self)




    def variable(self):

        localctx = MyGrammarParser.VariableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_variable)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 204
            self.match(MyGrammarParser.ID)
            self.state = 207
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==14:
                self.state = 205
                self.match(MyGrammarParser.T__13)
                self.state = 206
                self.expression()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentOperatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MyGrammarParser.RULE_assignmentOperator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignmentOperator" ):
                listener.enterAssignmentOperator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignmentOperator" ):
                listener.exitAssignmentOperator(self)




    def assignmentOperator(self):

        localctx = MyGrammarParser.AssignmentOperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_assignmentOperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 209
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 33538048) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[10] = self.logicalExpression_sempred
        self._predicates[11] = self.comparisonExpression_sempred
        self._predicates[12] = self.additiveExpression_sempred
        self._predicates[13] = self.multiplicativeExpression_sempred
        self._predicates[14] = self.bitwiseExpression_sempred
        self._predicates[15] = self.shiftExpression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def logicalExpression_sempred(self, localctx:LogicalExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def comparisonExpression_sempred(self, localctx:ComparisonExpressionContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def additiveExpression_sempred(self, localctx:AdditiveExpressionContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def multiplicativeExpression_sempred(self, localctx:MultiplicativeExpressionContext, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

    def bitwiseExpression_sempred(self, localctx:BitwiseExpressionContext, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         

    def shiftExpression_sempred(self, localctx:ShiftExpressionContext, predIndex:int):
            if predIndex == 5:
                return self.precpred(self._ctx, 2)
         




