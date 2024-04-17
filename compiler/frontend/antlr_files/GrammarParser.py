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
        4,1,57,267,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,1,0,5,0,60,8,0,10,0,12,0,63,9,0,1,0,1,0,5,0,
        67,8,0,10,0,12,0,70,9,0,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,2,5,2,80,8,
        2,10,2,12,2,83,9,2,1,2,1,2,1,3,1,3,1,3,1,3,1,4,1,4,1,4,5,4,94,8,
        4,10,4,12,4,97,9,4,3,4,99,8,4,1,5,1,5,1,5,3,5,104,8,5,1,6,1,6,1,
        6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,3,7,119,8,7,1,8,1,8,1,
        8,1,8,1,8,1,9,1,9,1,9,1,10,1,10,3,10,131,8,10,1,11,1,11,1,11,1,11,
        1,11,1,11,1,11,1,12,1,12,1,12,1,12,1,12,1,13,1,13,1,13,1,13,1,13,
        1,13,3,13,151,8,13,1,14,1,14,1,14,3,14,156,8,14,1,15,1,15,1,15,1,
        15,1,15,1,15,5,15,164,8,15,10,15,12,15,167,9,15,1,16,1,16,1,16,1,
        16,1,16,1,16,5,16,175,8,16,10,16,12,16,178,9,16,1,17,1,17,1,17,1,
        17,1,17,1,17,5,17,186,8,17,10,17,12,17,189,9,17,1,18,1,18,1,18,1,
        18,1,18,1,18,5,18,197,8,18,10,18,12,18,200,9,18,1,19,1,19,1,19,1,
        19,1,19,1,19,5,19,208,8,19,10,19,12,19,211,9,19,1,20,1,20,1,20,1,
        20,1,20,1,20,5,20,219,8,20,10,20,12,20,222,9,20,1,21,1,21,1,21,1,
        21,3,21,228,8,21,3,21,230,8,21,1,22,1,22,1,22,1,22,1,22,1,22,1,22,
        1,22,1,22,1,22,3,22,242,8,22,1,23,3,23,245,8,23,1,23,1,23,5,23,249,
        8,23,10,23,12,23,252,9,23,1,23,3,23,255,8,23,1,24,1,24,1,25,1,25,
        1,26,1,26,1,27,1,27,1,28,1,28,1,28,0,6,30,32,34,36,38,40,29,0,2,
        4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,
        50,52,54,56,0,11,1,0,45,46,1,0,39,44,1,0,34,35,1,0,36,38,1,0,50,
        52,1,0,48,49,4,0,14,15,34,36,47,47,50,50,1,0,14,15,2,0,1,1,16,17,
        2,0,9,9,19,28,1,0,56,57,270,0,61,1,0,0,0,2,71,1,0,0,0,4,77,1,0,0,
        0,6,86,1,0,0,0,8,98,1,0,0,0,10,100,1,0,0,0,12,105,1,0,0,0,14,118,
        1,0,0,0,16,120,1,0,0,0,18,125,1,0,0,0,20,130,1,0,0,0,22,132,1,0,
        0,0,24,139,1,0,0,0,26,144,1,0,0,0,28,152,1,0,0,0,30,157,1,0,0,0,
        32,168,1,0,0,0,34,179,1,0,0,0,36,190,1,0,0,0,38,201,1,0,0,0,40,212,
        1,0,0,0,42,229,1,0,0,0,44,241,1,0,0,0,46,254,1,0,0,0,48,256,1,0,
        0,0,50,258,1,0,0,0,52,260,1,0,0,0,54,262,1,0,0,0,56,264,1,0,0,0,
        58,60,3,14,7,0,59,58,1,0,0,0,60,63,1,0,0,0,61,59,1,0,0,0,61,62,1,
        0,0,0,62,64,1,0,0,0,63,61,1,0,0,0,64,68,3,2,1,0,65,67,3,14,7,0,66,
        65,1,0,0,0,67,70,1,0,0,0,68,66,1,0,0,0,68,69,1,0,0,0,69,1,1,0,0,
        0,70,68,1,0,0,0,71,72,5,1,0,0,72,73,5,2,0,0,73,74,5,3,0,0,74,75,
        5,4,0,0,75,76,3,4,2,0,76,3,1,0,0,0,77,81,5,5,0,0,78,80,3,14,7,0,
        79,78,1,0,0,0,80,83,1,0,0,0,81,79,1,0,0,0,81,82,1,0,0,0,82,84,1,
        0,0,0,83,81,1,0,0,0,84,85,5,6,0,0,85,5,1,0,0,0,86,87,3,46,23,0,87,
        88,3,8,4,0,88,89,5,7,0,0,89,7,1,0,0,0,90,95,3,10,5,0,91,92,5,8,0,
        0,92,94,3,10,5,0,93,91,1,0,0,0,94,97,1,0,0,0,95,93,1,0,0,0,95,96,
        1,0,0,0,96,99,1,0,0,0,97,95,1,0,0,0,98,90,1,0,0,0,98,99,1,0,0,0,
        99,9,1,0,0,0,100,103,5,31,0,0,101,102,5,9,0,0,102,104,3,20,10,0,
        103,101,1,0,0,0,103,104,1,0,0,0,104,11,1,0,0,0,105,106,5,3,0,0,106,
        107,3,46,23,0,107,108,5,4,0,0,108,109,3,42,21,0,109,13,1,0,0,0,110,
        119,3,18,9,0,111,119,3,4,2,0,112,119,3,6,3,0,113,119,3,24,12,0,114,
        119,3,56,28,0,115,119,3,16,8,0,116,119,3,26,13,0,117,119,5,7,0,0,
        118,110,1,0,0,0,118,111,1,0,0,0,118,112,1,0,0,0,118,113,1,0,0,0,
        118,114,1,0,0,0,118,115,1,0,0,0,118,116,1,0,0,0,118,117,1,0,0,0,
        119,15,1,0,0,0,120,121,5,10,0,0,121,122,3,46,23,0,122,123,5,31,0,
        0,123,124,5,7,0,0,124,17,1,0,0,0,125,126,3,20,10,0,126,127,5,7,0,
        0,127,19,1,0,0,0,128,131,3,30,15,0,129,131,3,22,11,0,130,128,1,0,
        0,0,130,129,1,0,0,0,131,21,1,0,0,0,132,133,5,11,0,0,133,134,5,3,
        0,0,134,135,5,54,0,0,135,136,5,8,0,0,136,137,3,30,15,0,137,138,5,
        4,0,0,138,23,1,0,0,0,139,140,3,20,10,0,140,141,3,54,27,0,141,142,
        3,20,10,0,142,143,5,7,0,0,143,25,1,0,0,0,144,145,5,12,0,0,145,146,
        5,3,0,0,146,147,3,20,10,0,147,148,5,4,0,0,148,150,3,4,2,0,149,151,
        3,28,14,0,150,149,1,0,0,0,150,151,1,0,0,0,151,27,1,0,0,0,152,155,
        5,13,0,0,153,156,3,4,2,0,154,156,3,26,13,0,155,153,1,0,0,0,155,154,
        1,0,0,0,156,29,1,0,0,0,157,158,6,15,-1,0,158,159,3,32,16,0,159,165,
        1,0,0,0,160,161,10,2,0,0,161,162,7,0,0,0,162,164,3,32,16,0,163,160,
        1,0,0,0,164,167,1,0,0,0,165,163,1,0,0,0,165,166,1,0,0,0,166,31,1,
        0,0,0,167,165,1,0,0,0,168,169,6,16,-1,0,169,170,3,34,17,0,170,176,
        1,0,0,0,171,172,10,2,0,0,172,173,7,1,0,0,173,175,3,34,17,0,174,171,
        1,0,0,0,175,178,1,0,0,0,176,174,1,0,0,0,176,177,1,0,0,0,177,33,1,
        0,0,0,178,176,1,0,0,0,179,180,6,17,-1,0,180,181,3,36,18,0,181,187,
        1,0,0,0,182,183,10,2,0,0,183,184,7,2,0,0,184,186,3,36,18,0,185,182,
        1,0,0,0,186,189,1,0,0,0,187,185,1,0,0,0,187,188,1,0,0,0,188,35,1,
        0,0,0,189,187,1,0,0,0,190,191,6,18,-1,0,191,192,3,38,19,0,192,198,
        1,0,0,0,193,194,10,2,0,0,194,195,7,3,0,0,195,197,3,38,19,0,196,193,
        1,0,0,0,197,200,1,0,0,0,198,196,1,0,0,0,198,199,1,0,0,0,199,37,1,
        0,0,0,200,198,1,0,0,0,201,202,6,19,-1,0,202,203,3,40,20,0,203,209,
        1,0,0,0,204,205,10,2,0,0,205,206,7,4,0,0,206,208,3,40,20,0,207,204,
        1,0,0,0,208,211,1,0,0,0,209,207,1,0,0,0,209,210,1,0,0,0,210,39,1,
        0,0,0,211,209,1,0,0,0,212,213,6,20,-1,0,213,214,3,42,21,0,214,220,
        1,0,0,0,215,216,10,2,0,0,216,217,7,5,0,0,217,219,3,42,21,0,218,215,
        1,0,0,0,219,222,1,0,0,0,220,218,1,0,0,0,220,221,1,0,0,0,221,41,1,
        0,0,0,222,220,1,0,0,0,223,224,7,6,0,0,224,230,3,42,21,0,225,227,
        3,44,22,0,226,228,7,7,0,0,227,226,1,0,0,0,227,228,1,0,0,0,228,230,
        1,0,0,0,229,223,1,0,0,0,229,225,1,0,0,0,230,43,1,0,0,0,231,242,5,
        29,0,0,232,242,5,30,0,0,233,234,5,3,0,0,234,235,3,20,10,0,235,236,
        5,4,0,0,236,242,1,0,0,0,237,242,5,31,0,0,238,242,5,32,0,0,239,242,
        5,33,0,0,240,242,3,12,6,0,241,231,1,0,0,0,241,232,1,0,0,0,241,233,
        1,0,0,0,241,237,1,0,0,0,241,238,1,0,0,0,241,239,1,0,0,0,241,240,
        1,0,0,0,242,45,1,0,0,0,243,245,3,50,25,0,244,243,1,0,0,0,244,245,
        1,0,0,0,245,246,1,0,0,0,246,250,3,48,24,0,247,249,3,52,26,0,248,
        247,1,0,0,0,249,252,1,0,0,0,250,248,1,0,0,0,250,251,1,0,0,0,251,
        255,1,0,0,0,252,250,1,0,0,0,253,255,5,31,0,0,254,244,1,0,0,0,254,
        253,1,0,0,0,255,47,1,0,0,0,256,257,7,8,0,0,257,49,1,0,0,0,258,259,
        5,18,0,0,259,51,1,0,0,0,260,261,5,36,0,0,261,53,1,0,0,0,262,263,
        7,9,0,0,263,55,1,0,0,0,264,265,7,10,0,0,265,57,1,0,0,0,22,61,68,
        81,95,98,103,118,130,150,155,165,176,187,198,209,220,227,229,241,
        244,250,254
    ]

class GrammarParser ( Parser ):

    grammarFileName = "Grammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'int'", "'main'", "'('", "')'", "'{'", 
                     "'}'", "';'", "','", "'='", "'typedef'", "'printf'", 
                     "'if'", "'else'", "'++'", "'--'", "'float'", "'char'", 
                     "'const'", "'+='", "'-='", "'*='", "'/='", "'%='", 
                     "'<<='", "'>>='", "'&='", "'^='", "'|='", "<INVALID>", 
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
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "NUMBER", "FLOAT", "ID", "CHAR", "CHAR_ESC", 
                      "PLUS", "MINUS", "MUL", "DIV", "MOD", "GT", "LT", 
                      "EQ", "GE", "LE", "NE", "AND", "OR", "NOT", "LSHIFT", 
                      "RSHIFT", "BITAND", "BITOR", "BITXOR", "BITNOT", "PRINTFREPLACER", 
                      "WS", "SINGLE_LINE_COMMENT", "MULTI_LINE_COMMENT" ]

    RULE_program = 0
    RULE_mainFunction = 1
    RULE_body = 2
    RULE_variableDeclaration = 3
    RULE_variableDeclarationQualifiers = 4
    RULE_variableDeclarationQualifier = 5
    RULE_castExpression = 6
    RULE_statement = 7
    RULE_typedefStatement = 8
    RULE_expressionStatement = 9
    RULE_expression = 10
    RULE_printCall = 11
    RULE_assignmentStatement = 12
    RULE_ifStatement = 13
    RULE_elseStatement = 14
    RULE_logicalExpression = 15
    RULE_comparisonExpression = 16
    RULE_additiveExpression = 17
    RULE_multiplicativeExpression = 18
    RULE_bitwiseExpression = 19
    RULE_shiftExpression = 20
    RULE_unaryExpression = 21
    RULE_primary = 22
    RULE_type = 23
    RULE_baseType = 24
    RULE_const = 25
    RULE_addressQualifier = 26
    RULE_assignmentOperator = 27
    RULE_comment = 28

    ruleNames =  [ "program", "mainFunction", "body", "variableDeclaration", 
                   "variableDeclarationQualifiers", "variableDeclarationQualifier", 
                   "castExpression", "statement", "typedefStatement", "expressionStatement", 
                   "expression", "printCall", "assignmentStatement", "ifStatement", 
                   "elseStatement", "logicalExpression", "comparisonExpression", 
                   "additiveExpression", "multiplicativeExpression", "bitwiseExpression", 
                   "shiftExpression", "unaryExpression", "primary", "type", 
                   "baseType", "const", "addressQualifier", "assignmentOperator", 
                   "comment" ]

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
    T__24=25
    T__25=26
    T__26=27
    T__27=28
    NUMBER=29
    FLOAT=30
    ID=31
    CHAR=32
    CHAR_ESC=33
    PLUS=34
    MINUS=35
    MUL=36
    DIV=37
    MOD=38
    GT=39
    LT=40
    EQ=41
    GE=42
    LE=43
    NE=44
    AND=45
    OR=46
    NOT=47
    LSHIFT=48
    RSHIFT=49
    BITAND=50
    BITOR=51
    BITXOR=52
    BITNOT=53
    PRINTFREPLACER=54
    WS=55
    SINGLE_LINE_COMMENT=56
    MULTI_LINE_COMMENT=57

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


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.StatementContext)
            else:
                return self.getTypedRuleContext(GrammarParser.StatementContext,i)


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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 58
                    self.statement() 
                self.state = 63
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

            self.state = 64
            self.mainFunction()
            self.state = 68
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 217439556411579562) != 0):
                self.state = 65
                self.statement()
                self.state = 70
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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
            self.state = 71
            self.match(GrammarParser.T__0)
            self.state = 72
            self.match(GrammarParser.T__1)
            self.state = 73
            self.match(GrammarParser.T__2)
            self.state = 74
            self.match(GrammarParser.T__3)
            self.state = 75
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
            self.state = 77
            self.match(GrammarParser.T__4)
            self.state = 81
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 217439556411579562) != 0):
                self.state = 78
                self.statement()
                self.state = 83
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 84
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
            self.state = 86
            self.type_()
            self.state = 87
            self.variableDeclarationQualifiers()
            self.state = 88
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
            self.state = 98
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==31:
                self.state = 90
                self.variableDeclarationQualifier()
                self.state = 95
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==8:
                    self.state = 91
                    self.match(GrammarParser.T__7)
                    self.state = 92
                    self.variableDeclarationQualifier()
                    self.state = 97
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
            self.state = 100
            self.match(GrammarParser.ID)
            self.state = 103
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==9:
                self.state = 101
                self.match(GrammarParser.T__8)
                self.state = 102
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
            self.state = 105
            self.match(GrammarParser.T__2)
            self.state = 106
            self.type_()
            self.state = 107
            self.match(GrammarParser.T__3)
            self.state = 108
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


        def assignmentStatement(self):
            return self.getTypedRuleContext(GrammarParser.AssignmentStatementContext,0)


        def comment(self):
            return self.getTypedRuleContext(GrammarParser.CommentContext,0)


        def typedefStatement(self):
            return self.getTypedRuleContext(GrammarParser.TypedefStatementContext,0)


        def ifStatement(self):
            return self.getTypedRuleContext(GrammarParser.IfStatementContext,0)


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
            self.state = 118
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 110
                self.expressionStatement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 111
                self.body()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 112
                self.variableDeclaration()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 113
                self.assignmentStatement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 114
                self.comment()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 115
                self.typedefStatement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 116
                self.ifStatement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 117
                self.match(GrammarParser.T__6)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypedefStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(GrammarParser.TypeContext,0)


        def ID(self):
            return self.getToken(GrammarParser.ID, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_typedefStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypedefStatement" ):
                listener.enterTypedefStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypedefStatement" ):
                listener.exitTypedefStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypedefStatement" ):
                return visitor.visitTypedefStatement(self)
            else:
                return visitor.visitChildren(self)




    def typedefStatement(self):

        localctx = GrammarParser.TypedefStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_typedefStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 120
            self.match(GrammarParser.T__9)
            self.state = 121
            self.type_()
            self.state = 122
            self.match(GrammarParser.ID)
            self.state = 123
            self.match(GrammarParser.T__6)
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
        self.enterRule(localctx, 18, self.RULE_expressionStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 125
            self.expression()
            self.state = 126
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

        def logicalExpression(self):
            return self.getTypedRuleContext(GrammarParser.LogicalExpressionContext,0)


        def printCall(self):
            return self.getTypedRuleContext(GrammarParser.PrintCallContext,0)


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
        self.enterRule(localctx, 20, self.RULE_expression)
        try:
            self.state = 130
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3, 14, 15, 29, 30, 31, 32, 33, 34, 35, 36, 47, 50]:
                self.enterOuterAlt(localctx, 1)
                self.state = 128
                self.logicalExpression(0)
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 2)
                self.state = 129
                self.printCall()
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


    class PrintCallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRINTFREPLACER(self):
            return self.getToken(GrammarParser.PRINTFREPLACER, 0)

        def logicalExpression(self):
            return self.getTypedRuleContext(GrammarParser.LogicalExpressionContext,0)


        def getRuleIndex(self):
            return GrammarParser.RULE_printCall

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintCall" ):
                listener.enterPrintCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintCall" ):
                listener.exitPrintCall(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintCall" ):
                return visitor.visitPrintCall(self)
            else:
                return visitor.visitChildren(self)




    def printCall(self):

        localctx = GrammarParser.PrintCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_printCall)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 132
            self.match(GrammarParser.T__10)
            self.state = 133
            self.match(GrammarParser.T__2)
            self.state = 134
            self.match(GrammarParser.PRINTFREPLACER)
            self.state = 135
            self.match(GrammarParser.T__7)
            self.state = 136
            self.logicalExpression(0)
            self.state = 137
            self.match(GrammarParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(GrammarParser.ExpressionContext,i)


        def assignmentOperator(self):
            return self.getTypedRuleContext(GrammarParser.AssignmentOperatorContext,0)


        def getRuleIndex(self):
            return GrammarParser.RULE_assignmentStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignmentStatement" ):
                listener.enterAssignmentStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignmentStatement" ):
                listener.exitAssignmentStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignmentStatement" ):
                return visitor.visitAssignmentStatement(self)
            else:
                return visitor.visitChildren(self)




    def assignmentStatement(self):

        localctx = GrammarParser.AssignmentStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_assignmentStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 139
            self.expression()
            self.state = 140
            self.assignmentOperator()
            self.state = 141
            self.expression()
            self.state = 142
            self.match(GrammarParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(GrammarParser.ExpressionContext,0)


        def body(self):
            return self.getTypedRuleContext(GrammarParser.BodyContext,0)


        def elseStatement(self):
            return self.getTypedRuleContext(GrammarParser.ElseStatementContext,0)


        def getRuleIndex(self):
            return GrammarParser.RULE_ifStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfStatement" ):
                listener.enterIfStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfStatement" ):
                listener.exitIfStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStatement" ):
                return visitor.visitIfStatement(self)
            else:
                return visitor.visitChildren(self)




    def ifStatement(self):

        localctx = GrammarParser.IfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_ifStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 144
            self.match(GrammarParser.T__11)
            self.state = 145
            self.match(GrammarParser.T__2)
            self.state = 146
            self.expression()
            self.state = 147
            self.match(GrammarParser.T__3)
            self.state = 148
            self.body()
            self.state = 150
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==13:
                self.state = 149
                self.elseStatement()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElseStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def body(self):
            return self.getTypedRuleContext(GrammarParser.BodyContext,0)


        def ifStatement(self):
            return self.getTypedRuleContext(GrammarParser.IfStatementContext,0)


        def getRuleIndex(self):
            return GrammarParser.RULE_elseStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElseStatement" ):
                listener.enterElseStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElseStatement" ):
                listener.exitElseStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElseStatement" ):
                return visitor.visitElseStatement(self)
            else:
                return visitor.visitChildren(self)




    def elseStatement(self):

        localctx = GrammarParser.ElseStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_elseStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 152
            self.match(GrammarParser.T__12)
            self.state = 155
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [5]:
                self.state = 153
                self.body()
                pass
            elif token in [12]:
                self.state = 154
                self.ifStatement()
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
        _startState = 30
        self.enterRecursionRule(localctx, 30, self.RULE_logicalExpression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 158
            self.comparisonExpression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 165
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = GrammarParser.LogicalExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_logicalExpression)
                    self.state = 160
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 161
                    _la = self._input.LA(1)
                    if not(_la==45 or _la==46):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 162
                    self.comparisonExpression(0) 
                self.state = 167
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

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
        _startState = 32
        self.enterRecursionRule(localctx, 32, self.RULE_comparisonExpression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 169
            self.additiveExpression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 176
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = GrammarParser.ComparisonExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_comparisonExpression)
                    self.state = 171
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 172
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 34634616274944) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 173
                    self.additiveExpression(0) 
                self.state = 178
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

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
        _startState = 34
        self.enterRecursionRule(localctx, 34, self.RULE_additiveExpression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 180
            self.multiplicativeExpression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 187
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = GrammarParser.AdditiveExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_additiveExpression)
                    self.state = 182
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 183
                    _la = self._input.LA(1)
                    if not(_la==34 or _la==35):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 184
                    self.multiplicativeExpression(0) 
                self.state = 189
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

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
        _startState = 36
        self.enterRecursionRule(localctx, 36, self.RULE_multiplicativeExpression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 191
            self.bitwiseExpression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 198
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = GrammarParser.MultiplicativeExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_multiplicativeExpression)
                    self.state = 193
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 194
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 481036337152) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 195
                    self.bitwiseExpression(0) 
                self.state = 200
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

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
        _startState = 38
        self.enterRecursionRule(localctx, 38, self.RULE_bitwiseExpression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 202
            self.shiftExpression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 209
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = GrammarParser.BitwiseExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_bitwiseExpression)
                    self.state = 204
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 205
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 7881299347898368) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 206
                    self.shiftExpression(0) 
                self.state = 211
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

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
        _startState = 40
        self.enterRecursionRule(localctx, 40, self.RULE_shiftExpression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 213
            self.unaryExpression()
            self._ctx.stop = self._input.LT(-1)
            self.state = 220
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = GrammarParser.ShiftExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_shiftExpression)
                    self.state = 215
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 216
                    _la = self._input.LA(1)
                    if not(_la==48 or _la==49):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 217
                    self.unaryExpression() 
                self.state = 222
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

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
        self.enterRule(localctx, 42, self.RULE_unaryExpression)
        self._la = 0 # Token type
        try:
            self.state = 229
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [14, 15, 34, 35, 36, 47, 50]:
                self.enterOuterAlt(localctx, 1)
                self.state = 223
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1266757654331392) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 224
                self.unaryExpression()
                pass
            elif token in [3, 29, 30, 31, 32, 33]:
                self.enterOuterAlt(localctx, 2)
                self.state = 225
                self.primary()
                self.state = 227
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
                if la_ == 1:
                    self.state = 226
                    _la = self._input.LA(1)
                    if not(_la==14 or _la==15):
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
        self.enterRule(localctx, 44, self.RULE_primary)
        try:
            self.state = 241
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 231
                self.match(GrammarParser.NUMBER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 232
                self.match(GrammarParser.FLOAT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 233
                self.match(GrammarParser.T__2)
                self.state = 234
                self.expression()
                self.state = 235
                self.match(GrammarParser.T__3)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 237
                self.match(GrammarParser.ID)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 238
                self.match(GrammarParser.CHAR)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 239
                self.match(GrammarParser.CHAR_ESC)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 240
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


        def ID(self):
            return self.getToken(GrammarParser.ID, 0)

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
        self.enterRule(localctx, 46, self.RULE_type)
        self._la = 0 # Token type
        try:
            self.state = 254
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 16, 17, 18]:
                self.enterOuterAlt(localctx, 1)
                self.state = 244
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==18:
                    self.state = 243
                    self.const()


                self.state = 246
                self.baseType()
                self.state = 250
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==36:
                    self.state = 247
                    self.addressQualifier()
                    self.state = 252
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            elif token in [31]:
                self.enterOuterAlt(localctx, 2)
                self.state = 253
                self.match(GrammarParser.ID)
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
        self.enterRule(localctx, 48, self.RULE_baseType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 256
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 196610) != 0)):
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
        self.enterRule(localctx, 50, self.RULE_const)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 258
            self.match(GrammarParser.T__17)
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
        self.enterRule(localctx, 52, self.RULE_addressQualifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 260
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
        self.enterRule(localctx, 54, self.RULE_assignmentOperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 262
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 536347136) != 0)):
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


    class CommentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SINGLE_LINE_COMMENT(self):
            return self.getToken(GrammarParser.SINGLE_LINE_COMMENT, 0)

        def MULTI_LINE_COMMENT(self):
            return self.getToken(GrammarParser.MULTI_LINE_COMMENT, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_comment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComment" ):
                listener.enterComment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComment" ):
                listener.exitComment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComment" ):
                return visitor.visitComment(self)
            else:
                return visitor.visitChildren(self)




    def comment(self):

        localctx = GrammarParser.CommentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_comment)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 264
            _la = self._input.LA(1)
            if not(_la==56 or _la==57):
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
        self._predicates[15] = self.logicalExpression_sempred
        self._predicates[16] = self.comparisonExpression_sempred
        self._predicates[17] = self.additiveExpression_sempred
        self._predicates[18] = self.multiplicativeExpression_sempred
        self._predicates[19] = self.bitwiseExpression_sempred
        self._predicates[20] = self.shiftExpression_sempred
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
         




