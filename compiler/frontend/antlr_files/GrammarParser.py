# Generated from Grammar.g4 by ANTLR 4.13.1
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
        4,1,50,227,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,1,0,1,0,1,
        1,1,1,1,1,1,1,1,1,1,1,1,2,1,2,5,2,63,8,2,10,2,12,2,66,9,2,1,2,1,
        2,1,3,1,3,1,3,1,3,1,4,1,4,1,4,5,4,77,8,4,10,4,12,4,80,9,4,3,4,82,
        8,4,1,5,1,5,1,5,3,5,87,8,5,1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,3,7,97,
        8,7,1,8,1,8,1,8,1,9,1,9,3,9,104,8,9,1,10,1,10,1,11,1,11,1,12,5,12,
        111,8,12,10,12,12,12,114,9,12,1,12,1,12,1,12,1,12,1,12,3,12,121,
        8,12,1,13,1,13,1,13,1,13,1,13,1,13,5,13,129,8,13,10,13,12,13,132,
        9,13,1,14,1,14,1,14,1,14,1,14,1,14,5,14,140,8,14,10,14,12,14,143,
        9,14,1,15,1,15,1,15,1,15,1,15,1,15,5,15,151,8,15,10,15,12,15,154,
        9,15,1,16,1,16,1,16,1,16,1,16,1,16,5,16,162,8,16,10,16,12,16,165,
        9,16,1,17,1,17,1,17,1,17,1,17,1,17,5,17,173,8,17,10,17,12,17,176,
        9,17,1,18,1,18,1,18,1,18,1,18,1,18,5,18,184,8,18,10,18,12,18,187,
        9,18,1,19,1,19,1,19,1,19,3,19,193,8,19,3,19,195,8,19,1,20,1,20,1,
        20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,3,20,207,8,20,1,21,3,21,210,
        8,21,1,21,1,21,5,21,214,8,21,10,21,12,21,217,9,21,1,22,1,22,1,23,
        1,23,1,24,1,24,1,25,1,25,1,25,0,6,26,28,30,32,34,36,26,0,2,4,6,8,
        10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,0,
        10,1,0,41,42,1,0,35,40,1,0,30,31,1,0,32,34,1,0,46,48,1,0,44,45,4,
        0,10,11,30,32,43,43,46,46,1,0,10,11,2,0,1,1,12,13,2,0,9,9,15,24,
        225,0,52,1,0,0,0,2,54,1,0,0,0,4,60,1,0,0,0,6,69,1,0,0,0,8,81,1,0,
        0,0,10,83,1,0,0,0,12,88,1,0,0,0,14,96,1,0,0,0,16,98,1,0,0,0,18,103,
        1,0,0,0,20,105,1,0,0,0,22,107,1,0,0,0,24,120,1,0,0,0,26,122,1,0,
        0,0,28,133,1,0,0,0,30,144,1,0,0,0,32,155,1,0,0,0,34,166,1,0,0,0,
        36,177,1,0,0,0,38,194,1,0,0,0,40,206,1,0,0,0,42,209,1,0,0,0,44,218,
        1,0,0,0,46,220,1,0,0,0,48,222,1,0,0,0,50,224,1,0,0,0,52,53,3,2,1,
        0,53,1,1,0,0,0,54,55,5,1,0,0,55,56,5,2,0,0,56,57,5,3,0,0,57,58,5,
        4,0,0,58,59,3,4,2,0,59,3,1,0,0,0,60,64,5,5,0,0,61,63,3,14,7,0,62,
        61,1,0,0,0,63,66,1,0,0,0,64,62,1,0,0,0,64,65,1,0,0,0,65,67,1,0,0,
        0,66,64,1,0,0,0,67,68,5,6,0,0,68,5,1,0,0,0,69,70,3,42,21,0,70,71,
        3,8,4,0,71,72,5,7,0,0,72,7,1,0,0,0,73,78,3,10,5,0,74,75,5,8,0,0,
        75,77,3,10,5,0,76,74,1,0,0,0,77,80,1,0,0,0,78,76,1,0,0,0,78,79,1,
        0,0,0,79,82,1,0,0,0,80,78,1,0,0,0,81,73,1,0,0,0,81,82,1,0,0,0,82,
        9,1,0,0,0,83,86,5,27,0,0,84,85,5,9,0,0,85,87,3,18,9,0,86,84,1,0,
        0,0,86,87,1,0,0,0,87,11,1,0,0,0,88,89,5,3,0,0,89,90,3,42,21,0,90,
        91,5,4,0,0,91,92,3,38,19,0,92,13,1,0,0,0,93,97,3,16,8,0,94,97,3,
        4,2,0,95,97,3,6,3,0,96,93,1,0,0,0,96,94,1,0,0,0,96,95,1,0,0,0,97,
        15,1,0,0,0,98,99,3,18,9,0,99,100,5,7,0,0,100,17,1,0,0,0,101,104,
        3,20,10,0,102,104,3,22,11,0,103,101,1,0,0,0,103,102,1,0,0,0,104,
        19,1,0,0,0,105,106,3,24,12,0,106,21,1,0,0,0,107,108,3,26,13,0,108,
        23,1,0,0,0,109,111,3,48,24,0,110,109,1,0,0,0,111,114,1,0,0,0,112,
        110,1,0,0,0,112,113,1,0,0,0,113,115,1,0,0,0,114,112,1,0,0,0,115,
        116,5,27,0,0,116,117,3,50,25,0,117,118,3,18,9,0,118,121,1,0,0,0,
        119,121,3,26,13,0,120,112,1,0,0,0,120,119,1,0,0,0,121,25,1,0,0,0,
        122,123,6,13,-1,0,123,124,3,28,14,0,124,130,1,0,0,0,125,126,10,2,
        0,0,126,127,7,0,0,0,127,129,3,28,14,0,128,125,1,0,0,0,129,132,1,
        0,0,0,130,128,1,0,0,0,130,131,1,0,0,0,131,27,1,0,0,0,132,130,1,0,
        0,0,133,134,6,14,-1,0,134,135,3,30,15,0,135,141,1,0,0,0,136,137,
        10,2,0,0,137,138,7,1,0,0,138,140,3,30,15,0,139,136,1,0,0,0,140,143,
        1,0,0,0,141,139,1,0,0,0,141,142,1,0,0,0,142,29,1,0,0,0,143,141,1,
        0,0,0,144,145,6,15,-1,0,145,146,3,32,16,0,146,152,1,0,0,0,147,148,
        10,2,0,0,148,149,7,2,0,0,149,151,3,32,16,0,150,147,1,0,0,0,151,154,
        1,0,0,0,152,150,1,0,0,0,152,153,1,0,0,0,153,31,1,0,0,0,154,152,1,
        0,0,0,155,156,6,16,-1,0,156,157,3,34,17,0,157,163,1,0,0,0,158,159,
        10,2,0,0,159,160,7,3,0,0,160,162,3,34,17,0,161,158,1,0,0,0,162,165,
        1,0,0,0,163,161,1,0,0,0,163,164,1,0,0,0,164,33,1,0,0,0,165,163,1,
        0,0,0,166,167,6,17,-1,0,167,168,3,36,18,0,168,174,1,0,0,0,169,170,
        10,2,0,0,170,171,7,4,0,0,171,173,3,36,18,0,172,169,1,0,0,0,173,176,
        1,0,0,0,174,172,1,0,0,0,174,175,1,0,0,0,175,35,1,0,0,0,176,174,1,
        0,0,0,177,178,6,18,-1,0,178,179,3,38,19,0,179,185,1,0,0,0,180,181,
        10,2,0,0,181,182,7,5,0,0,182,184,3,38,19,0,183,180,1,0,0,0,184,187,
        1,0,0,0,185,183,1,0,0,0,185,186,1,0,0,0,186,37,1,0,0,0,187,185,1,
        0,0,0,188,189,7,6,0,0,189,195,3,38,19,0,190,192,3,40,20,0,191,193,
        7,7,0,0,192,191,1,0,0,0,192,193,1,0,0,0,193,195,1,0,0,0,194,188,
        1,0,0,0,194,190,1,0,0,0,195,39,1,0,0,0,196,207,5,25,0,0,197,207,
        5,26,0,0,198,199,5,3,0,0,199,200,3,18,9,0,200,201,5,4,0,0,201,207,
        1,0,0,0,202,207,5,27,0,0,203,207,5,28,0,0,204,207,5,29,0,0,205,207,
        3,12,6,0,206,196,1,0,0,0,206,197,1,0,0,0,206,198,1,0,0,0,206,202,
        1,0,0,0,206,203,1,0,0,0,206,204,1,0,0,0,206,205,1,0,0,0,207,41,1,
        0,0,0,208,210,3,46,23,0,209,208,1,0,0,0,209,210,1,0,0,0,210,211,
        1,0,0,0,211,215,3,44,22,0,212,214,3,48,24,0,213,212,1,0,0,0,214,
        217,1,0,0,0,215,213,1,0,0,0,215,216,1,0,0,0,216,43,1,0,0,0,217,215,
        1,0,0,0,218,219,7,8,0,0,219,45,1,0,0,0,220,221,5,14,0,0,221,47,1,
        0,0,0,222,223,5,32,0,0,223,49,1,0,0,0,224,225,7,9,0,0,225,51,1,0,
        0,0,19,64,78,81,86,96,103,112,120,130,141,152,163,174,185,192,194,
        206,209,215
    ]

class GrammarParser ( Parser ):

    grammarFileName = "Grammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'int'", "'main'", "'('", "')'", "'{'", 
                     "'}'", "';'", "','", "'='", "'++'", "'--'", "'float'", 
                     "'char'", "'const'", "'+='", "'-='", "'*='", "'/='", 
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
    RULE_body = 2
    RULE_variableDeclaration = 3
    RULE_variableDeclarationQualifiers = 4
    RULE_variableDeclarationQualifier = 5
    RULE_castExpression = 6
    RULE_statement = 7
    RULE_expressionStatement = 8
    RULE_expression = 9
    RULE_mutableExpression = 10
    RULE_immutableExpression = 11
    RULE_assignmentExpression = 12
    RULE_logicalExpression = 13
    RULE_comparisonExpression = 14
    RULE_additiveExpression = 15
    RULE_multiplicativeExpression = 16
    RULE_bitwiseExpression = 17
    RULE_shiftExpression = 18
    RULE_unaryExpression = 19
    RULE_primary = 20
    RULE_type = 21
    RULE_baseType = 22
    RULE_const = 23
    RULE_addressQualifier = 24
    RULE_assignmentOperator = 25

    ruleNames =  [ "program", "mainFunction", "body", "variableDeclaration", 
                   "variableDeclarationQualifiers", "variableDeclarationQualifier", 
                   "castExpression", "statement", "expressionStatement", 
                   "expression", "mutableExpression", "immutableExpression", 
                   "assignmentExpression", "logicalExpression", "comparisonExpression", 
                   "additiveExpression", "multiplicativeExpression", "bitwiseExpression", 
                   "shiftExpression", "unaryExpression", "primary", "type", 
                   "baseType", "const", "addressQualifier", "assignmentOperator" ]

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
            return self.getTypedRuleContext(GrammarParser.MainFunctionContext,0)


        def getRuleIndex(self):
            return GrammarParser.RULE_program

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

        localctx = GrammarParser.ProgramContext(self, self._ctx, self.state)
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

        def body(self):
            return self.getTypedRuleContext(GrammarParser.BodyContext,0)


        def getRuleIndex(self):
            return GrammarParser.RULE_mainFunction

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

        localctx = GrammarParser.MainFunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_mainFunction)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 54
            self.match(GrammarParser.T__0)
            self.state = 55
            self.match(GrammarParser.T__1)
            self.state = 56
            self.match(GrammarParser.T__2)
            self.state = 57
            self.match(GrammarParser.T__3)
            self.state = 58
            self.body()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.StatementContext)
            else:
                return self.getTypedRuleContext(GrammarParser.StatementContext,i)


        def getRuleIndex(self):
            return GrammarParser.RULE_body

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBody" ):
                listener.enterBody(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBody" ):
                listener.exitBody(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBody" ):
                return visitor.visitBody(self)
            else:
                return visitor.visitChildren(self)




    def body(self):

        localctx = GrammarParser.BodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 60
            self.match(GrammarParser.T__4)
            self.state = 64
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 79173393611818) != 0):
                self.state = 61
                self.statement()
                self.state = 66
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 67
            self.match(GrammarParser.T__5)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(GrammarParser.TypeContext,0)


        def variableDeclarationQualifiers(self):
            return self.getTypedRuleContext(GrammarParser.VariableDeclarationQualifiersContext,0)


        def getRuleIndex(self):
            return GrammarParser.RULE_variableDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariableDeclaration" ):
                listener.enterVariableDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariableDeclaration" ):
                listener.exitVariableDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariableDeclaration" ):
                return visitor.visitVariableDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def variableDeclaration(self):

        localctx = GrammarParser.VariableDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_variableDeclaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 69
            self.type_()
            self.state = 70
            self.variableDeclarationQualifiers()
            self.state = 71
            self.match(GrammarParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableDeclarationQualifiersContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variableDeclarationQualifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.VariableDeclarationQualifierContext)
            else:
                return self.getTypedRuleContext(GrammarParser.VariableDeclarationQualifierContext,i)


        def getRuleIndex(self):
            return GrammarParser.RULE_variableDeclarationQualifiers

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariableDeclarationQualifiers" ):
                listener.enterVariableDeclarationQualifiers(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariableDeclarationQualifiers" ):
                listener.exitVariableDeclarationQualifiers(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariableDeclarationQualifiers" ):
                return visitor.visitVariableDeclarationQualifiers(self)
            else:
                return visitor.visitChildren(self)




    def variableDeclarationQualifiers(self):

        localctx = GrammarParser.VariableDeclarationQualifiersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_variableDeclarationQualifiers)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==27:
                self.state = 73
                self.variableDeclarationQualifier()
                self.state = 78
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==8:
                    self.state = 74
                    self.match(GrammarParser.T__7)
                    self.state = 75
                    self.variableDeclarationQualifier()
                    self.state = 80
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableDeclarationQualifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(GrammarParser.ID, 0)

        def expression(self):
            return self.getTypedRuleContext(GrammarParser.ExpressionContext,0)


        def getRuleIndex(self):
            return GrammarParser.RULE_variableDeclarationQualifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariableDeclarationQualifier" ):
                listener.enterVariableDeclarationQualifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariableDeclarationQualifier" ):
                listener.exitVariableDeclarationQualifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariableDeclarationQualifier" ):
                return visitor.visitVariableDeclarationQualifier(self)
            else:
                return visitor.visitChildren(self)




    def variableDeclarationQualifier(self):

        localctx = GrammarParser.VariableDeclarationQualifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_variableDeclarationQualifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83
            self.match(GrammarParser.ID)
            self.state = 86
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==9:
                self.state = 84
                self.match(GrammarParser.T__8)
                self.state = 85
                self.expression()


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
            return self.getTypedRuleContext(GrammarParser.TypeContext,0)


        def unaryExpression(self):
            return self.getTypedRuleContext(GrammarParser.UnaryExpressionContext,0)


        def getRuleIndex(self):
            return GrammarParser.RULE_castExpression

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

        localctx = GrammarParser.CastExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_castExpression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 88
            self.match(GrammarParser.T__2)
            self.state = 89
            self.type_()
            self.state = 90
            self.match(GrammarParser.T__3)
            self.state = 91
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
            return self.getTypedRuleContext(GrammarParser.ExpressionStatementContext,0)


        def body(self):
            return self.getTypedRuleContext(GrammarParser.BodyContext,0)


        def variableDeclaration(self):
            return self.getTypedRuleContext(GrammarParser.VariableDeclarationContext,0)


        def getRuleIndex(self):
            return GrammarParser.RULE_statement

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

        localctx = GrammarParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_statement)
        try:
            self.state = 96
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3, 10, 11, 25, 26, 27, 28, 29, 30, 31, 32, 43, 46]:
                self.enterOuterAlt(localctx, 1)
                self.state = 93
                self.expressionStatement()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 2)
                self.state = 94
                self.body()
                pass
            elif token in [1, 12, 13, 14]:
                self.enterOuterAlt(localctx, 3)
                self.state = 95
                self.variableDeclaration()
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
            return self.getTypedRuleContext(GrammarParser.ExpressionContext,0)


        def getRuleIndex(self):
            return GrammarParser.RULE_expressionStatement

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

        localctx = GrammarParser.ExpressionStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_expressionStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 98
            self.expression()
            self.state = 99
            self.match(GrammarParser.T__6)
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
            return self.getTypedRuleContext(GrammarParser.MutableExpressionContext,0)


        def immutableExpression(self):
            return self.getTypedRuleContext(GrammarParser.ImmutableExpressionContext,0)


        def getRuleIndex(self):
            return GrammarParser.RULE_expression

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

        localctx = GrammarParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_expression)
        try:
            self.state = 103
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 101
                self.mutableExpression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 102
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
            return self.getTypedRuleContext(GrammarParser.AssignmentExpressionContext,0)


        def getRuleIndex(self):
            return GrammarParser.RULE_mutableExpression

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

        localctx = GrammarParser.MutableExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_mutableExpression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 105
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
            return self.getTypedRuleContext(GrammarParser.LogicalExpressionContext,0)


        def getRuleIndex(self):
            return GrammarParser.RULE_immutableExpression

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

        localctx = GrammarParser.ImmutableExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_immutableExpression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 107
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

        def ID(self):
            return self.getToken(GrammarParser.ID, 0)

        def assignmentOperator(self):
            return self.getTypedRuleContext(GrammarParser.AssignmentOperatorContext,0)


        def expression(self):
            return self.getTypedRuleContext(GrammarParser.ExpressionContext,0)


        def addressQualifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.AddressQualifierContext)
            else:
                return self.getTypedRuleContext(GrammarParser.AddressQualifierContext,i)


        def logicalExpression(self):
            return self.getTypedRuleContext(GrammarParser.LogicalExpressionContext,0)


        def getRuleIndex(self):
            return GrammarParser.RULE_assignmentExpression

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

        localctx = GrammarParser.AssignmentExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_assignmentExpression)
        self._la = 0 # Token type
        try:
            self.state = 120
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 112
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==32:
                    self.state = 109
                    self.addressQualifier()
                    self.state = 114
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 115
                self.match(GrammarParser.ID)
                self.state = 116
                self.assignmentOperator()
                self.state = 117
                self.expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 119
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
            return self.getTypedRuleContext(GrammarParser.ComparisonExpressionContext,0)


        def logicalExpression(self):
            return self.getTypedRuleContext(GrammarParser.LogicalExpressionContext,0)


        def AND(self):
            return self.getToken(GrammarParser.AND, 0)

        def OR(self):
            return self.getToken(GrammarParser.OR, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_logicalExpression

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
        localctx = GrammarParser.LogicalExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 26
        self.enterRecursionRule(localctx, 26, self.RULE_logicalExpression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 123
            self.comparisonExpression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 130
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = GrammarParser.LogicalExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_logicalExpression)
                    self.state = 125
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 126
                    _la = self._input.LA(1)
                    if not(_la==41 or _la==42):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 127
                    self.comparisonExpression(0) 
                self.state = 132
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

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
            return self.getTypedRuleContext(GrammarParser.AdditiveExpressionContext,0)


        def comparisonExpression(self):
            return self.getTypedRuleContext(GrammarParser.ComparisonExpressionContext,0)


        def GT(self):
            return self.getToken(GrammarParser.GT, 0)

        def LT(self):
            return self.getToken(GrammarParser.LT, 0)

        def EQ(self):
            return self.getToken(GrammarParser.EQ, 0)

        def GE(self):
            return self.getToken(GrammarParser.GE, 0)

        def LE(self):
            return self.getToken(GrammarParser.LE, 0)

        def NE(self):
            return self.getToken(GrammarParser.NE, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_comparisonExpression

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
        localctx = GrammarParser.ComparisonExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 28
        self.enterRecursionRule(localctx, 28, self.RULE_comparisonExpression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 134
            self.additiveExpression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 141
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = GrammarParser.ComparisonExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_comparisonExpression)
                    self.state = 136
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 137
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 2164663517184) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 138
                    self.additiveExpression(0) 
                self.state = 143
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

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
            return self.getTypedRuleContext(GrammarParser.MultiplicativeExpressionContext,0)


        def additiveExpression(self):
            return self.getTypedRuleContext(GrammarParser.AdditiveExpressionContext,0)


        def PLUS(self):
            return self.getToken(GrammarParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(GrammarParser.MINUS, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_additiveExpression

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
        localctx = GrammarParser.AdditiveExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 30
        self.enterRecursionRule(localctx, 30, self.RULE_additiveExpression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 145
            self.multiplicativeExpression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 152
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = GrammarParser.AdditiveExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_additiveExpression)
                    self.state = 147
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 148
                    _la = self._input.LA(1)
                    if not(_la==30 or _la==31):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 149
                    self.multiplicativeExpression(0) 
                self.state = 154
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

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
            return self.getTypedRuleContext(GrammarParser.BitwiseExpressionContext,0)


        def multiplicativeExpression(self):
            return self.getTypedRuleContext(GrammarParser.MultiplicativeExpressionContext,0)


        def MUL(self):
            return self.getToken(GrammarParser.MUL, 0)

        def DIV(self):
            return self.getToken(GrammarParser.DIV, 0)

        def MOD(self):
            return self.getToken(GrammarParser.MOD, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_multiplicativeExpression

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
        localctx = GrammarParser.MultiplicativeExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 32
        self.enterRecursionRule(localctx, 32, self.RULE_multiplicativeExpression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 156
            self.bitwiseExpression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 163
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = GrammarParser.MultiplicativeExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_multiplicativeExpression)
                    self.state = 158
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 159
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 30064771072) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 160
                    self.bitwiseExpression(0) 
                self.state = 165
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

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
            return self.getTypedRuleContext(GrammarParser.ShiftExpressionContext,0)


        def bitwiseExpression(self):
            return self.getTypedRuleContext(GrammarParser.BitwiseExpressionContext,0)


        def BITAND(self):
            return self.getToken(GrammarParser.BITAND, 0)

        def BITOR(self):
            return self.getToken(GrammarParser.BITOR, 0)

        def BITXOR(self):
            return self.getToken(GrammarParser.BITXOR, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_bitwiseExpression

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
        localctx = GrammarParser.BitwiseExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 34
        self.enterRecursionRule(localctx, 34, self.RULE_bitwiseExpression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 167
            self.shiftExpression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 174
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = GrammarParser.BitwiseExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_bitwiseExpression)
                    self.state = 169
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 170
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 492581209243648) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 171
                    self.shiftExpression(0) 
                self.state = 176
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

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
            return self.getTypedRuleContext(GrammarParser.UnaryExpressionContext,0)


        def shiftExpression(self):
            return self.getTypedRuleContext(GrammarParser.ShiftExpressionContext,0)


        def LSHIFT(self):
            return self.getToken(GrammarParser.LSHIFT, 0)

        def RSHIFT(self):
            return self.getToken(GrammarParser.RSHIFT, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_shiftExpression

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
        localctx = GrammarParser.ShiftExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 36
        self.enterRecursionRule(localctx, 36, self.RULE_shiftExpression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 178
            self.unaryExpression()
            self._ctx.stop = self._input.LT(-1)
            self.state = 185
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = GrammarParser.ShiftExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_shiftExpression)
                    self.state = 180
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 181
                    _la = self._input.LA(1)
                    if not(_la==44 or _la==45):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 182
                    self.unaryExpression() 
                self.state = 187
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

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
            return self.getTypedRuleContext(GrammarParser.UnaryExpressionContext,0)


        def PLUS(self):
            return self.getToken(GrammarParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(GrammarParser.MINUS, 0)

        def NOT(self):
            return self.getToken(GrammarParser.NOT, 0)

        def MUL(self):
            return self.getToken(GrammarParser.MUL, 0)

        def BITAND(self):
            return self.getToken(GrammarParser.BITAND, 0)

        def primary(self):
            return self.getTypedRuleContext(GrammarParser.PrimaryContext,0)


        def getRuleIndex(self):
            return GrammarParser.RULE_unaryExpression

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

        localctx = GrammarParser.UnaryExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_unaryExpression)
        self._la = 0 # Token type
        try:
            self.state = 194
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10, 11, 30, 31, 32, 43, 46]:
                self.enterOuterAlt(localctx, 1)
                self.state = 188
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 79172353395712) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 189
                self.unaryExpression()
                pass
            elif token in [3, 25, 26, 27, 28, 29]:
                self.enterOuterAlt(localctx, 2)
                self.state = 190
                self.primary()
                self.state = 192
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
                if la_ == 1:
                    self.state = 191
                    _la = self._input.LA(1)
                    if not(_la==10 or _la==11):
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
            return self.getToken(GrammarParser.NUMBER, 0)

        def FLOAT(self):
            return self.getToken(GrammarParser.FLOAT, 0)

        def expression(self):
            return self.getTypedRuleContext(GrammarParser.ExpressionContext,0)


        def ID(self):
            return self.getToken(GrammarParser.ID, 0)

        def CHAR(self):
            return self.getToken(GrammarParser.CHAR, 0)

        def CHAR_ESC(self):
            return self.getToken(GrammarParser.CHAR_ESC, 0)

        def castExpression(self):
            return self.getTypedRuleContext(GrammarParser.CastExpressionContext,0)


        def getRuleIndex(self):
            return GrammarParser.RULE_primary

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

        localctx = GrammarParser.PrimaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_primary)
        try:
            self.state = 206
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 196
                self.match(GrammarParser.NUMBER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 197
                self.match(GrammarParser.FLOAT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 198
                self.match(GrammarParser.T__2)
                self.state = 199
                self.expression()
                self.state = 200
                self.match(GrammarParser.T__3)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 202
                self.match(GrammarParser.ID)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 203
                self.match(GrammarParser.CHAR)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 204
                self.match(GrammarParser.CHAR_ESC)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 205
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
            return self.getTypedRuleContext(GrammarParser.BaseTypeContext,0)


        def const(self):
            return self.getTypedRuleContext(GrammarParser.ConstContext,0)


        def addressQualifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.AddressQualifierContext)
            else:
                return self.getTypedRuleContext(GrammarParser.AddressQualifierContext,i)


        def getRuleIndex(self):
            return GrammarParser.RULE_type

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

        localctx = GrammarParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 209
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==14:
                self.state = 208
                self.const()


            self.state = 211
            self.baseType()
            self.state = 215
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==32:
                self.state = 212
                self.addressQualifier()
                self.state = 217
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
            return GrammarParser.RULE_baseType

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

        localctx = GrammarParser.BaseTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_baseType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 218
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 12290) != 0)):
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


    class ConstContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return GrammarParser.RULE_const

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConst" ):
                listener.enterConst(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConst" ):
                listener.exitConst(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConst" ):
                return visitor.visitConst(self)
            else:
                return visitor.visitChildren(self)




    def const(self):

        localctx = GrammarParser.ConstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_const)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 220
            self.match(GrammarParser.T__13)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AddressQualifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MUL(self):
            return self.getToken(GrammarParser.MUL, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_addressQualifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddressQualifier" ):
                listener.enterAddressQualifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddressQualifier" ):
                listener.exitAddressQualifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddressQualifier" ):
                return visitor.visitAddressQualifier(self)
            else:
                return visitor.visitChildren(self)




    def addressQualifier(self):

        localctx = GrammarParser.AddressQualifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_addressQualifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 222
            self.match(GrammarParser.MUL)
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
            return GrammarParser.RULE_assignmentOperator

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

        localctx = GrammarParser.AssignmentOperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_assignmentOperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 224
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 33522176) != 0)):
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
        self._predicates[13] = self.logicalExpression_sempred
        self._predicates[14] = self.comparisonExpression_sempred
        self._predicates[15] = self.additiveExpression_sempred
        self._predicates[16] = self.multiplicativeExpression_sempred
        self._predicates[17] = self.bitwiseExpression_sempred
        self._predicates[18] = self.shiftExpression_sempred
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
         




