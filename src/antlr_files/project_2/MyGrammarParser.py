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
        4,1,50,221,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,1,0,1,0,1,
        1,1,1,1,1,1,1,1,1,1,1,1,2,1,2,5,2,63,8,2,10,2,12,2,66,9,2,1,2,1,
        2,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,3,5,82,8,5,1,6,
        1,6,1,6,1,7,1,7,3,7,89,8,7,1,8,1,8,1,9,1,9,1,10,1,10,1,10,1,10,1,
        10,3,10,100,8,10,1,11,1,11,1,11,1,11,1,11,1,11,5,11,108,8,11,10,
        11,12,11,111,9,11,1,12,1,12,1,12,1,12,1,12,1,12,5,12,119,8,12,10,
        12,12,12,122,9,12,1,13,1,13,1,13,1,13,1,13,1,13,5,13,130,8,13,10,
        13,12,13,133,9,13,1,14,1,14,1,14,1,14,1,14,1,14,5,14,141,8,14,10,
        14,12,14,144,9,14,1,15,1,15,1,15,1,15,1,15,1,15,5,15,152,8,15,10,
        15,12,15,155,9,15,1,16,1,16,1,16,1,16,1,16,1,16,5,16,163,8,16,10,
        16,12,16,166,9,16,1,17,1,17,1,17,1,17,3,17,172,8,17,3,17,174,8,17,
        1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,3,18,186,8,18,
        1,19,3,19,189,8,19,1,19,1,19,5,19,193,8,19,10,19,12,19,196,9,19,
        1,20,1,20,1,21,1,21,1,22,1,22,1,23,1,23,1,23,5,23,207,8,23,10,23,
        12,23,210,9,23,3,23,212,8,23,1,24,1,24,1,24,3,24,217,8,24,1,25,1,
        25,1,25,0,6,22,24,26,28,30,32,26,0,2,4,6,8,10,12,14,16,18,20,22,
        24,26,28,30,32,34,36,38,40,42,44,46,48,50,0,10,1,0,41,42,1,0,35,
        40,1,0,30,31,1,0,32,34,1,0,46,48,1,0,44,45,4,0,8,9,30,32,43,43,46,
        46,1,0,8,9,2,0,1,1,10,11,1,0,14,24,218,0,52,1,0,0,0,2,54,1,0,0,0,
        4,60,1,0,0,0,6,69,1,0,0,0,8,73,1,0,0,0,10,81,1,0,0,0,12,83,1,0,0,
        0,14,88,1,0,0,0,16,90,1,0,0,0,18,92,1,0,0,0,20,99,1,0,0,0,22,101,
        1,0,0,0,24,112,1,0,0,0,26,123,1,0,0,0,28,134,1,0,0,0,30,145,1,0,
        0,0,32,156,1,0,0,0,34,173,1,0,0,0,36,185,1,0,0,0,38,188,1,0,0,0,
        40,197,1,0,0,0,42,199,1,0,0,0,44,201,1,0,0,0,46,211,1,0,0,0,48,213,
        1,0,0,0,50,218,1,0,0,0,52,53,3,2,1,0,53,1,1,0,0,0,54,55,5,1,0,0,
        55,56,5,2,0,0,56,57,5,3,0,0,57,58,5,4,0,0,58,59,3,4,2,0,59,3,1,0,
        0,0,60,64,5,5,0,0,61,63,3,10,5,0,62,61,1,0,0,0,63,66,1,0,0,0,64,
        62,1,0,0,0,64,65,1,0,0,0,65,67,1,0,0,0,66,64,1,0,0,0,67,68,5,6,0,
        0,68,5,1,0,0,0,69,70,3,38,19,0,70,71,3,46,23,0,71,72,5,7,0,0,72,
        7,1,0,0,0,73,74,5,3,0,0,74,75,3,38,19,0,75,76,5,4,0,0,76,77,3,34,
        17,0,77,9,1,0,0,0,78,82,3,12,6,0,79,82,3,4,2,0,80,82,3,6,3,0,81,
        78,1,0,0,0,81,79,1,0,0,0,81,80,1,0,0,0,82,11,1,0,0,0,83,84,3,14,
        7,0,84,85,5,7,0,0,85,13,1,0,0,0,86,89,3,16,8,0,87,89,3,18,9,0,88,
        86,1,0,0,0,88,87,1,0,0,0,89,15,1,0,0,0,90,91,3,20,10,0,91,17,1,0,
        0,0,92,93,3,22,11,0,93,19,1,0,0,0,94,95,3,34,17,0,95,96,3,50,25,
        0,96,97,3,14,7,0,97,100,1,0,0,0,98,100,3,22,11,0,99,94,1,0,0,0,99,
        98,1,0,0,0,100,21,1,0,0,0,101,102,6,11,-1,0,102,103,3,24,12,0,103,
        109,1,0,0,0,104,105,10,2,0,0,105,106,7,0,0,0,106,108,3,24,12,0,107,
        104,1,0,0,0,108,111,1,0,0,0,109,107,1,0,0,0,109,110,1,0,0,0,110,
        23,1,0,0,0,111,109,1,0,0,0,112,113,6,12,-1,0,113,114,3,26,13,0,114,
        120,1,0,0,0,115,116,10,2,0,0,116,117,7,1,0,0,117,119,3,26,13,0,118,
        115,1,0,0,0,119,122,1,0,0,0,120,118,1,0,0,0,120,121,1,0,0,0,121,
        25,1,0,0,0,122,120,1,0,0,0,123,124,6,13,-1,0,124,125,3,28,14,0,125,
        131,1,0,0,0,126,127,10,2,0,0,127,128,7,2,0,0,128,130,3,28,14,0,129,
        126,1,0,0,0,130,133,1,0,0,0,131,129,1,0,0,0,131,132,1,0,0,0,132,
        27,1,0,0,0,133,131,1,0,0,0,134,135,6,14,-1,0,135,136,3,30,15,0,136,
        142,1,0,0,0,137,138,10,2,0,0,138,139,7,3,0,0,139,141,3,30,15,0,140,
        137,1,0,0,0,141,144,1,0,0,0,142,140,1,0,0,0,142,143,1,0,0,0,143,
        29,1,0,0,0,144,142,1,0,0,0,145,146,6,15,-1,0,146,147,3,32,16,0,147,
        153,1,0,0,0,148,149,10,2,0,0,149,150,7,4,0,0,150,152,3,32,16,0,151,
        148,1,0,0,0,152,155,1,0,0,0,153,151,1,0,0,0,153,154,1,0,0,0,154,
        31,1,0,0,0,155,153,1,0,0,0,156,157,6,16,-1,0,157,158,3,34,17,0,158,
        164,1,0,0,0,159,160,10,2,0,0,160,161,7,5,0,0,161,163,3,34,17,0,162,
        159,1,0,0,0,163,166,1,0,0,0,164,162,1,0,0,0,164,165,1,0,0,0,165,
        33,1,0,0,0,166,164,1,0,0,0,167,168,7,6,0,0,168,174,3,34,17,0,169,
        171,3,36,18,0,170,172,7,7,0,0,171,170,1,0,0,0,171,172,1,0,0,0,172,
        174,1,0,0,0,173,167,1,0,0,0,173,169,1,0,0,0,174,35,1,0,0,0,175,186,
        5,25,0,0,176,186,5,26,0,0,177,178,5,3,0,0,178,179,3,14,7,0,179,180,
        5,4,0,0,180,186,1,0,0,0,181,186,5,27,0,0,182,186,5,28,0,0,183,186,
        5,29,0,0,184,186,3,8,4,0,185,175,1,0,0,0,185,176,1,0,0,0,185,177,
        1,0,0,0,185,181,1,0,0,0,185,182,1,0,0,0,185,183,1,0,0,0,185,184,
        1,0,0,0,186,37,1,0,0,0,187,189,3,42,21,0,188,187,1,0,0,0,188,189,
        1,0,0,0,189,190,1,0,0,0,190,194,3,40,20,0,191,193,3,44,22,0,192,
        191,1,0,0,0,193,196,1,0,0,0,194,192,1,0,0,0,194,195,1,0,0,0,195,
        39,1,0,0,0,196,194,1,0,0,0,197,198,7,8,0,0,198,41,1,0,0,0,199,200,
        5,12,0,0,200,43,1,0,0,0,201,202,5,32,0,0,202,45,1,0,0,0,203,208,
        3,48,24,0,204,205,5,13,0,0,205,207,3,48,24,0,206,204,1,0,0,0,207,
        210,1,0,0,0,208,206,1,0,0,0,208,209,1,0,0,0,209,212,1,0,0,0,210,
        208,1,0,0,0,211,203,1,0,0,0,211,212,1,0,0,0,212,47,1,0,0,0,213,216,
        5,27,0,0,214,215,5,14,0,0,215,217,3,14,7,0,216,214,1,0,0,0,216,217,
        1,0,0,0,217,49,1,0,0,0,218,219,7,9,0,0,219,51,1,0,0,0,18,64,81,88,
        99,109,120,131,142,153,164,171,173,185,188,194,208,211,216
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
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'+'", "'-'", "'*'", "'/'", "'%'", "'>'", "'<'", "'=='", 
                     "'>='", "'<='", "'!='", "'&&'", "'||'", "'!'", "'<<'", 
                     "'>>'", "'&'", "'|'", "'^'", "'~'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "NUMBER", "FLOAT", "ID", "CHAR", "CHAR_ESC", 
                      "PLUS", "MINUS", "MUL", "DIV", "MOD", "GT", "LT", 
                      "EQ", "GE", "LE", "NE", "AND", "OR", "NOT", "LSHIFT", 
                      "RSHIFT", "BITAND", "BITOR", "BITXOR", "BITNOT", "WS" ]

    RULE_program = 0
    RULE_mainFunction = 1
    RULE_compoundStatement = 2
    RULE_declaration = 3
    RULE_castExpression = 4
    RULE_statement = 5
    RULE_expressionStatement = 6
    RULE_expression = 7
    RULE_mutableExpression = 8
    RULE_immutableExpression = 9
    RULE_assignmentExpression = 10
    RULE_logicalExpression = 11
    RULE_comparisonExpression = 12
    RULE_additiveExpression = 13
    RULE_multiplicativeExpression = 14
    RULE_bitwiseExpression = 15
    RULE_shiftExpression = 16
    RULE_unaryExpression = 17
    RULE_primary = 18
    RULE_type = 19
    RULE_baseType = 20
    RULE_typeQualifier = 21
    RULE_pointerQualifier = 22
    RULE_variableList = 23
    RULE_variable = 24
    RULE_assignmentOperator = 25

    ruleNames =  [ "program", "mainFunction", "compoundStatement", "declaration", 
                   "castExpression", "statement", "expressionStatement", 
                   "expression", "mutableExpression", "immutableExpression", 
                   "assignmentExpression", "logicalExpression", "comparisonExpression", 
                   "additiveExpression", "multiplicativeExpression", "bitwiseExpression", 
                   "shiftExpression", "unaryExpression", "primary", "type", 
                   "baseType", "typeQualifier", "pointerQualifier", "variableList", 
                   "variable", "assignmentOperator" ]

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
    CHAR_ESC=29
    PLUS=30
    MINUS=31
    MUL=32
    DIV=33
    MOD=34
    GT=35
    LT=36
    EQ=37
    GE=38
    LE=39
    NE=40
    AND=41
    OR=42
    NOT=43
    LSHIFT=44
    RSHIFT=45
    BITAND=46
    BITOR=47
    BITXOR=48
    BITNOT=49
    WS=50

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = MyGrammarParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMainFunction" ):
                return visitor.visitMainFunction(self)
            else:
                return visitor.visitChildren(self)




    def mainFunction(self):

        localctx = MyGrammarParser.MainFunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_mainFunction)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 54
            self.match(MyGrammarParser.T__0)
            self.state = 55
            self.match(MyGrammarParser.T__1)
            self.state = 56
            self.match(MyGrammarParser.T__2)
            self.state = 57
            self.match(MyGrammarParser.T__3)
            self.state = 58
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCompoundStatement" ):
                return visitor.visitCompoundStatement(self)
            else:
                return visitor.visitChildren(self)




    def compoundStatement(self):

        localctx = MyGrammarParser.CompoundStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_compoundStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 60
            self.match(MyGrammarParser.T__4)
            self.state = 64
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 79173393588010) != 0):
                self.state = 61
                self.statement()
                self.state = 66
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 67
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaration" ):
                return visitor.visitDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def declaration(self):

        localctx = MyGrammarParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 69
            self.type_()
            self.state = 70
            self.variableList()
            self.state = 71
            self.match(MyGrammarParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CastExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(MyGrammarParser.TypeContext,0)


        def unaryExpression(self):
            return self.getTypedRuleContext(MyGrammarParser.UnaryExpressionContext,0)


        def getRuleIndex(self):
            return MyGrammarParser.RULE_castExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCastExpression" ):
                listener.enterCastExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCastExpression" ):
                listener.exitCastExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCastExpression" ):
                return visitor.visitCastExpression(self)
            else:
                return visitor.visitChildren(self)




    def castExpression(self):

        localctx = MyGrammarParser.CastExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_castExpression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 73
            self.match(MyGrammarParser.T__2)
            self.state = 74
            self.type_()
            self.state = 75
            self.match(MyGrammarParser.T__3)
            self.state = 76
            self.unaryExpression()
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = MyGrammarParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_statement)
        try:
            self.state = 81
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3, 8, 9, 25, 26, 27, 28, 29, 30, 31, 32, 43, 46]:
                self.enterOuterAlt(localctx, 1)
                self.state = 78
                self.expressionStatement()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 2)
                self.state = 79
                self.compoundStatement()
                pass
            elif token in [1, 10, 11, 12]:
                self.enterOuterAlt(localctx, 3)
                self.state = 80
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressionStatement" ):
                return visitor.visitExpressionStatement(self)
            else:
                return visitor.visitChildren(self)




    def expressionStatement(self):

        localctx = MyGrammarParser.ExpressionStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_expressionStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83
            self.expression()
            self.state = 84
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = MyGrammarParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_expression)
        try:
            self.state = 88
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 86
                self.mutableExpression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 87
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMutableExpression" ):
                return visitor.visitMutableExpression(self)
            else:
                return visitor.visitChildren(self)




    def mutableExpression(self):

        localctx = MyGrammarParser.MutableExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_mutableExpression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 90
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImmutableExpression" ):
                return visitor.visitImmutableExpression(self)
            else:
                return visitor.visitChildren(self)




    def immutableExpression(self):

        localctx = MyGrammarParser.ImmutableExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_immutableExpression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 92
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignmentExpression" ):
                return visitor.visitAssignmentExpression(self)
            else:
                return visitor.visitChildren(self)




    def assignmentExpression(self):

        localctx = MyGrammarParser.AssignmentExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_assignmentExpression)
        try:
            self.state = 99
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 94
                self.unaryExpression()
                self.state = 95
                self.assignmentOperator()
                self.state = 96
                self.expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 98
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicalExpression" ):
                return visitor.visitLogicalExpression(self)
            else:
                return visitor.visitChildren(self)



    def logicalExpression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MyGrammarParser.LogicalExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 22
        self.enterRecursionRule(localctx, 22, self.RULE_logicalExpression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 102
            self.comparisonExpression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 109
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MyGrammarParser.LogicalExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_logicalExpression)
                    self.state = 104
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 105
                    _la = self._input.LA(1)
                    if not(_la==41 or _la==42):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 106
                    self.comparisonExpression(0) 
                self.state = 111
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComparisonExpression" ):
                return visitor.visitComparisonExpression(self)
            else:
                return visitor.visitChildren(self)



    def comparisonExpression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MyGrammarParser.ComparisonExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 24
        self.enterRecursionRule(localctx, 24, self.RULE_comparisonExpression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 113
            self.additiveExpression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 120
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MyGrammarParser.ComparisonExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_comparisonExpression)
                    self.state = 115
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 116
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 2164663517184) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 117
                    self.additiveExpression(0) 
                self.state = 122
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdditiveExpression" ):
                return visitor.visitAdditiveExpression(self)
            else:
                return visitor.visitChildren(self)



    def additiveExpression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MyGrammarParser.AdditiveExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 26
        self.enterRecursionRule(localctx, 26, self.RULE_additiveExpression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 124
            self.multiplicativeExpression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 131
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MyGrammarParser.AdditiveExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_additiveExpression)
                    self.state = 126
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 127
                    _la = self._input.LA(1)
                    if not(_la==30 or _la==31):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 128
                    self.multiplicativeExpression(0) 
                self.state = 133
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiplicativeExpression" ):
                return visitor.visitMultiplicativeExpression(self)
            else:
                return visitor.visitChildren(self)



    def multiplicativeExpression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MyGrammarParser.MultiplicativeExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 28
        self.enterRecursionRule(localctx, 28, self.RULE_multiplicativeExpression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 135
            self.bitwiseExpression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 142
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MyGrammarParser.MultiplicativeExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_multiplicativeExpression)
                    self.state = 137
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 138
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 30064771072) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 139
                    self.bitwiseExpression(0) 
                self.state = 144
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBitwiseExpression" ):
                return visitor.visitBitwiseExpression(self)
            else:
                return visitor.visitChildren(self)



    def bitwiseExpression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MyGrammarParser.BitwiseExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 30
        self.enterRecursionRule(localctx, 30, self.RULE_bitwiseExpression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 146
            self.shiftExpression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 153
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MyGrammarParser.BitwiseExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_bitwiseExpression)
                    self.state = 148
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 149
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 492581209243648) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 150
                    self.shiftExpression(0) 
                self.state = 155
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitShiftExpression" ):
                return visitor.visitShiftExpression(self)
            else:
                return visitor.visitChildren(self)



    def shiftExpression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MyGrammarParser.ShiftExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 32
        self.enterRecursionRule(localctx, 32, self.RULE_shiftExpression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 157
            self.unaryExpression()
            self._ctx.stop = self._input.LT(-1)
            self.state = 164
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MyGrammarParser.ShiftExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_shiftExpression)
                    self.state = 159
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 160
                    _la = self._input.LA(1)
                    if not(_la==44 or _la==45):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 161
                    self.unaryExpression() 
                self.state = 166
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnaryExpression" ):
                return visitor.visitUnaryExpression(self)
            else:
                return visitor.visitChildren(self)




    def unaryExpression(self):

        localctx = MyGrammarParser.UnaryExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_unaryExpression)
        self._la = 0 # Token type
        try:
            self.state = 173
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8, 9, 30, 31, 32, 43, 46]:
                self.enterOuterAlt(localctx, 1)
                self.state = 167
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 79172353393408) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 168
                self.unaryExpression()
                pass
            elif token in [3, 25, 26, 27, 28, 29]:
                self.enterOuterAlt(localctx, 2)
                self.state = 169
                self.primary()
                self.state = 171
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
                if la_ == 1:
                    self.state = 170
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

        def CHAR_ESC(self):
            return self.getToken(MyGrammarParser.CHAR_ESC, 0)

        def castExpression(self):
            return self.getTypedRuleContext(MyGrammarParser.CastExpressionContext,0)


        def getRuleIndex(self):
            return MyGrammarParser.RULE_primary

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimary" ):
                listener.enterPrimary(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimary" ):
                listener.exitPrimary(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimary" ):
                return visitor.visitPrimary(self)
            else:
                return visitor.visitChildren(self)




    def primary(self):

        localctx = MyGrammarParser.PrimaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_primary)
        try:
            self.state = 185
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 175
                self.match(MyGrammarParser.NUMBER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 176
                self.match(MyGrammarParser.FLOAT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 177
                self.match(MyGrammarParser.T__2)
                self.state = 178
                self.expression()
                self.state = 179
                self.match(MyGrammarParser.T__3)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 181
                self.match(MyGrammarParser.ID)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 182
                self.match(MyGrammarParser.CHAR)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 183
                self.match(MyGrammarParser.CHAR_ESC)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 184
                self.castExpression()
                pass


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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType" ):
                return visitor.visitType(self)
            else:
                return visitor.visitChildren(self)




    def type_(self):

        localctx = MyGrammarParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 188
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==12:
                self.state = 187
                self.typeQualifier()


            self.state = 190
            self.baseType()
            self.state = 194
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==32:
                self.state = 191
                self.pointerQualifier()
                self.state = 196
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBaseType" ):
                return visitor.visitBaseType(self)
            else:
                return visitor.visitChildren(self)




    def baseType(self):

        localctx = MyGrammarParser.BaseTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_baseType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 197
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeQualifier" ):
                return visitor.visitTypeQualifier(self)
            else:
                return visitor.visitChildren(self)




    def typeQualifier(self):

        localctx = MyGrammarParser.TypeQualifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_typeQualifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 199
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPointerQualifier" ):
                return visitor.visitPointerQualifier(self)
            else:
                return visitor.visitChildren(self)




    def pointerQualifier(self):

        localctx = MyGrammarParser.PointerQualifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_pointerQualifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 201
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariableList" ):
                return visitor.visitVariableList(self)
            else:
                return visitor.visitChildren(self)




    def variableList(self):

        localctx = MyGrammarParser.VariableListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_variableList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 211
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==27:
                self.state = 203
                self.variable()
                self.state = 208
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==13:
                    self.state = 204
                    self.match(MyGrammarParser.T__12)
                    self.state = 205
                    self.variable()
                    self.state = 210
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable" ):
                return visitor.visitVariable(self)
            else:
                return visitor.visitChildren(self)




    def variable(self):

        localctx = MyGrammarParser.VariableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_variable)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 213
            self.match(MyGrammarParser.ID)
            self.state = 216
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==14:
                self.state = 214
                self.match(MyGrammarParser.T__13)
                self.state = 215
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignmentOperator" ):
                return visitor.visitAssignmentOperator(self)
            else:
                return visitor.visitChildren(self)




    def assignmentOperator(self):

        localctx = MyGrammarParser.AssignmentOperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_assignmentOperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 218
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
        self._predicates[11] = self.logicalExpression_sempred
        self._predicates[12] = self.comparisonExpression_sempred
        self._predicates[13] = self.additiveExpression_sempred
        self._predicates[14] = self.multiplicativeExpression_sempred
        self._predicates[15] = self.bitwiseExpression_sempred
        self._predicates[16] = self.shiftExpression_sempred
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
         




