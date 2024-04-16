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
        4,1,57,291,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,1,0,5,0,66,8,0,
        10,0,12,0,69,9,0,1,0,1,0,5,0,73,8,0,10,0,12,0,76,9,0,1,1,1,1,1,1,
        1,1,1,1,1,1,1,2,1,2,5,2,86,8,2,10,2,12,2,89,9,2,1,2,1,2,1,3,1,3,
        1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,105,8,3,1,4,1,4,1,4,
        1,4,1,5,1,5,1,5,1,5,3,5,115,8,5,1,6,1,6,3,6,119,8,6,1,7,3,7,122,
        8,7,1,8,1,8,1,8,1,8,1,9,1,9,1,9,5,9,131,8,9,10,9,12,9,134,9,9,3,
        9,136,8,9,1,10,1,10,1,10,3,10,141,8,10,1,11,1,11,1,11,1,11,1,11,
        1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,3,12,156,8,12,1,13,1,13,
        1,13,1,13,1,13,1,14,1,14,1,14,1,15,1,15,3,15,168,8,15,1,16,1,16,
        1,16,1,16,1,16,1,16,1,16,1,17,1,17,1,17,1,17,1,17,1,18,1,18,1,18,
        1,18,1,18,1,18,5,18,188,8,18,10,18,12,18,191,9,18,1,19,1,19,1,19,
        1,19,1,19,1,19,5,19,199,8,19,10,19,12,19,202,9,19,1,20,1,20,1,20,
        1,20,1,20,1,20,5,20,210,8,20,10,20,12,20,213,9,20,1,21,1,21,1,21,
        1,21,1,21,1,21,5,21,221,8,21,10,21,12,21,224,9,21,1,22,1,22,1,22,
        1,22,1,22,1,22,5,22,232,8,22,10,22,12,22,235,9,22,1,23,1,23,1,23,
        1,23,1,23,1,23,5,23,243,8,23,10,23,12,23,246,9,23,1,24,1,24,1,24,
        1,24,3,24,252,8,24,3,24,254,8,24,1,25,1,25,1,25,1,25,1,25,1,25,1,
        25,1,25,1,25,1,25,3,25,266,8,25,1,26,3,26,269,8,26,1,26,1,26,5,26,
        273,8,26,10,26,12,26,276,9,26,1,26,3,26,279,8,26,1,27,1,27,1,28,
        1,28,1,29,1,29,1,30,1,30,1,31,1,31,1,31,0,6,36,38,40,42,44,46,32,
        0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,
        46,48,50,52,54,56,58,60,62,0,11,1,0,45,46,1,0,39,44,1,0,34,35,1,
        0,36,38,1,0,50,52,1,0,48,49,4,0,11,12,34,36,47,47,50,50,1,0,11,12,
        2,0,1,1,13,14,2,0,8,8,16,25,1,0,56,57,295,0,67,1,0,0,0,2,77,1,0,
        0,0,4,83,1,0,0,0,6,104,1,0,0,0,8,106,1,0,0,0,10,114,1,0,0,0,12,118,
        1,0,0,0,14,121,1,0,0,0,16,123,1,0,0,0,18,135,1,0,0,0,20,137,1,0,
        0,0,22,142,1,0,0,0,24,155,1,0,0,0,26,157,1,0,0,0,28,162,1,0,0,0,
        30,167,1,0,0,0,32,169,1,0,0,0,34,176,1,0,0,0,36,181,1,0,0,0,38,192,
        1,0,0,0,40,203,1,0,0,0,42,214,1,0,0,0,44,225,1,0,0,0,46,236,1,0,
        0,0,48,253,1,0,0,0,50,265,1,0,0,0,52,278,1,0,0,0,54,280,1,0,0,0,
        56,282,1,0,0,0,58,284,1,0,0,0,60,286,1,0,0,0,62,288,1,0,0,0,64,66,
        3,24,12,0,65,64,1,0,0,0,66,69,1,0,0,0,67,65,1,0,0,0,67,68,1,0,0,
        0,68,70,1,0,0,0,69,67,1,0,0,0,70,74,3,2,1,0,71,73,3,24,12,0,72,71,
        1,0,0,0,73,76,1,0,0,0,74,72,1,0,0,0,74,75,1,0,0,0,75,1,1,0,0,0,76,
        74,1,0,0,0,77,78,5,1,0,0,78,79,5,2,0,0,79,80,5,3,0,0,80,81,5,4,0,
        0,81,82,3,4,2,0,82,3,1,0,0,0,83,87,5,5,0,0,84,86,3,24,12,0,85,84,
        1,0,0,0,86,89,1,0,0,0,87,85,1,0,0,0,87,88,1,0,0,0,88,90,1,0,0,0,
        89,87,1,0,0,0,90,91,5,6,0,0,91,5,1,0,0,0,92,93,5,26,0,0,93,94,5,
        3,0,0,94,95,3,30,15,0,95,96,5,4,0,0,96,97,3,24,12,0,97,105,1,0,0,
        0,98,99,5,27,0,0,99,100,5,3,0,0,100,101,3,8,4,0,101,102,5,4,0,0,
        102,103,3,24,12,0,103,105,1,0,0,0,104,92,1,0,0,0,104,98,1,0,0,0,
        105,7,1,0,0,0,106,107,3,10,5,0,107,108,3,12,6,0,108,109,3,14,7,0,
        109,9,1,0,0,0,110,115,3,16,8,0,111,115,3,34,17,0,112,115,3,28,14,
        0,113,115,5,28,0,0,114,110,1,0,0,0,114,111,1,0,0,0,114,112,1,0,0,
        0,114,113,1,0,0,0,115,11,1,0,0,0,116,119,3,28,14,0,117,119,5,28,
        0,0,118,116,1,0,0,0,118,117,1,0,0,0,119,13,1,0,0,0,120,122,3,30,
        15,0,121,120,1,0,0,0,121,122,1,0,0,0,122,15,1,0,0,0,123,124,3,52,
        26,0,124,125,3,18,9,0,125,126,5,28,0,0,126,17,1,0,0,0,127,132,3,
        20,10,0,128,129,5,7,0,0,129,131,3,20,10,0,130,128,1,0,0,0,131,134,
        1,0,0,0,132,130,1,0,0,0,132,133,1,0,0,0,133,136,1,0,0,0,134,132,
        1,0,0,0,135,127,1,0,0,0,135,136,1,0,0,0,136,19,1,0,0,0,137,140,5,
        31,0,0,138,139,5,8,0,0,139,141,3,30,15,0,140,138,1,0,0,0,140,141,
        1,0,0,0,141,21,1,0,0,0,142,143,5,3,0,0,143,144,3,52,26,0,144,145,
        5,4,0,0,145,146,3,48,24,0,146,23,1,0,0,0,147,156,3,28,14,0,148,156,
        3,4,2,0,149,156,3,16,8,0,150,156,3,34,17,0,151,156,3,62,31,0,152,
        156,3,26,13,0,153,156,3,6,3,0,154,156,5,28,0,0,155,147,1,0,0,0,155,
        148,1,0,0,0,155,149,1,0,0,0,155,150,1,0,0,0,155,151,1,0,0,0,155,
        152,1,0,0,0,155,153,1,0,0,0,155,154,1,0,0,0,156,25,1,0,0,0,157,158,
        5,9,0,0,158,159,3,52,26,0,159,160,5,31,0,0,160,161,5,28,0,0,161,
        27,1,0,0,0,162,163,3,30,15,0,163,164,5,28,0,0,164,29,1,0,0,0,165,
        168,3,36,18,0,166,168,3,32,16,0,167,165,1,0,0,0,167,166,1,0,0,0,
        168,31,1,0,0,0,169,170,5,10,0,0,170,171,5,3,0,0,171,172,5,54,0,0,
        172,173,5,7,0,0,173,174,3,36,18,0,174,175,5,4,0,0,175,33,1,0,0,0,
        176,177,3,30,15,0,177,178,3,60,30,0,178,179,3,30,15,0,179,180,5,
        28,0,0,180,35,1,0,0,0,181,182,6,18,-1,0,182,183,3,38,19,0,183,189,
        1,0,0,0,184,185,10,2,0,0,185,186,7,0,0,0,186,188,3,38,19,0,187,184,
        1,0,0,0,188,191,1,0,0,0,189,187,1,0,0,0,189,190,1,0,0,0,190,37,1,
        0,0,0,191,189,1,0,0,0,192,193,6,19,-1,0,193,194,3,40,20,0,194,200,
        1,0,0,0,195,196,10,2,0,0,196,197,7,1,0,0,197,199,3,40,20,0,198,195,
        1,0,0,0,199,202,1,0,0,0,200,198,1,0,0,0,200,201,1,0,0,0,201,39,1,
        0,0,0,202,200,1,0,0,0,203,204,6,20,-1,0,204,205,3,42,21,0,205,211,
        1,0,0,0,206,207,10,2,0,0,207,208,7,2,0,0,208,210,3,42,21,0,209,206,
        1,0,0,0,210,213,1,0,0,0,211,209,1,0,0,0,211,212,1,0,0,0,212,41,1,
        0,0,0,213,211,1,0,0,0,214,215,6,21,-1,0,215,216,3,44,22,0,216,222,
        1,0,0,0,217,218,10,2,0,0,218,219,7,3,0,0,219,221,3,44,22,0,220,217,
        1,0,0,0,221,224,1,0,0,0,222,220,1,0,0,0,222,223,1,0,0,0,223,43,1,
        0,0,0,224,222,1,0,0,0,225,226,6,22,-1,0,226,227,3,46,23,0,227,233,
        1,0,0,0,228,229,10,2,0,0,229,230,7,4,0,0,230,232,3,46,23,0,231,228,
        1,0,0,0,232,235,1,0,0,0,233,231,1,0,0,0,233,234,1,0,0,0,234,45,1,
        0,0,0,235,233,1,0,0,0,236,237,6,23,-1,0,237,238,3,48,24,0,238,244,
        1,0,0,0,239,240,10,2,0,0,240,241,7,5,0,0,241,243,3,48,24,0,242,239,
        1,0,0,0,243,246,1,0,0,0,244,242,1,0,0,0,244,245,1,0,0,0,245,47,1,
        0,0,0,246,244,1,0,0,0,247,248,7,6,0,0,248,254,3,48,24,0,249,251,
        3,50,25,0,250,252,7,7,0,0,251,250,1,0,0,0,251,252,1,0,0,0,252,254,
        1,0,0,0,253,247,1,0,0,0,253,249,1,0,0,0,254,49,1,0,0,0,255,266,5,
        29,0,0,256,266,5,30,0,0,257,258,5,3,0,0,258,259,3,30,15,0,259,260,
        5,4,0,0,260,266,1,0,0,0,261,266,5,31,0,0,262,266,5,32,0,0,263,266,
        5,33,0,0,264,266,3,22,11,0,265,255,1,0,0,0,265,256,1,0,0,0,265,257,
        1,0,0,0,265,261,1,0,0,0,265,262,1,0,0,0,265,263,1,0,0,0,265,264,
        1,0,0,0,266,51,1,0,0,0,267,269,3,56,28,0,268,267,1,0,0,0,268,269,
        1,0,0,0,269,270,1,0,0,0,270,274,3,54,27,0,271,273,3,58,29,0,272,
        271,1,0,0,0,273,276,1,0,0,0,274,272,1,0,0,0,274,275,1,0,0,0,275,
        279,1,0,0,0,276,274,1,0,0,0,277,279,5,31,0,0,278,268,1,0,0,0,278,
        277,1,0,0,0,279,53,1,0,0,0,280,281,7,8,0,0,281,55,1,0,0,0,282,283,
        5,15,0,0,283,57,1,0,0,0,284,285,5,36,0,0,285,59,1,0,0,0,286,287,
        7,9,0,0,287,61,1,0,0,0,288,289,7,10,0,0,289,63,1,0,0,0,24,67,74,
        87,104,114,118,121,132,135,140,155,167,189,200,211,222,233,244,251,
        253,265,268,274,278
    ]

class GrammarParser ( Parser ):

    grammarFileName = "Grammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'int'", "'main'", "'('", "')'", "'{'", 
                     "'}'", "','", "'='", "'typedef'", "'printf'", "'++'", 
                     "'--'", "'float'", "'char'", "'const'", "'+='", "'-='", 
                     "'*='", "'/='", "'%='", "'<<='", "'>>='", "'&='", "'^='", 
                     "'|='", "'while'", "'for'", "';'", "<INVALID>", "<INVALID>", 
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
                      "<INVALID>", "<INVALID>", "WHILE", "FOR", "TERMINAL", 
                      "NUMBER", "FLOAT", "ID", "CHAR", "CHAR_ESC", "PLUS", 
                      "MINUS", "MUL", "DIV", "MOD", "GT", "LT", "EQ", "GE", 
                      "LE", "NE", "AND", "OR", "NOT", "LSHIFT", "RSHIFT", 
                      "BITAND", "BITOR", "BITXOR", "BITNOT", "PRINTFREPLACER", 
                      "WS", "SINGLE_LINE_COMMENT", "MULTI_LINE_COMMENT" ]

    RULE_program = 0
    RULE_mainFunction = 1
    RULE_body = 2
    RULE_iterationStatement = 3
    RULE_forCondition = 4
    RULE_forFirst = 5
    RULE_forSecond = 6
    RULE_forThird = 7
    RULE_variableDeclaration = 8
    RULE_variableDeclarationQualifiers = 9
    RULE_variableDeclarationQualifier = 10
    RULE_castExpression = 11
    RULE_statement = 12
    RULE_typedefStatement = 13
    RULE_expressionStatement = 14
    RULE_expression = 15
    RULE_printCall = 16
    RULE_assignmentStatement = 17
    RULE_logicalExpression = 18
    RULE_comparisonExpression = 19
    RULE_additiveExpression = 20
    RULE_multiplicativeExpression = 21
    RULE_bitwiseExpression = 22
    RULE_shiftExpression = 23
    RULE_unaryExpression = 24
    RULE_primary = 25
    RULE_type = 26
    RULE_baseType = 27
    RULE_const = 28
    RULE_addressQualifier = 29
    RULE_assignmentOperator = 30
    RULE_comment = 31

    ruleNames =  [ "program", "mainFunction", "body", "iterationStatement", 
                   "forCondition", "forFirst", "forSecond", "forThird", 
                   "variableDeclaration", "variableDeclarationQualifiers", 
                   "variableDeclarationQualifier", "castExpression", "statement", 
                   "typedefStatement", "expressionStatement", "expression", 
                   "printCall", "assignmentStatement", "logicalExpression", 
                   "comparisonExpression", "additiveExpression", "multiplicativeExpression", 
                   "bitwiseExpression", "shiftExpression", "unaryExpression", 
                   "primary", "type", "baseType", "const", "addressQualifier", 
                   "assignmentOperator", "comment" ]

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
    WHILE=26
    FOR=27
    TERMINAL=28
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
            self.state = 67
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 64
                    self.statement() 
                self.state = 69
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

            self.state = 70
            self.mainFunction()
            self.state = 74
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 217439556880891434) != 0):
                self.state = 71
                self.statement()
                self.state = 76
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
            self.state = 77
            self.match(GrammarParser.T__0)
            self.state = 78
            self.match(GrammarParser.T__1)
            self.state = 79
            self.match(GrammarParser.T__2)
            self.state = 80
            self.match(GrammarParser.T__3)
            self.state = 81
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
            self.state = 83
            self.match(GrammarParser.T__4)
            self.state = 87
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 217439556880891434) != 0):
                self.state = 84
                self.statement()
                self.state = 89
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 90
            self.match(GrammarParser.T__5)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IterationStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(GrammarParser.WHILE, 0)

        def expression(self):
            return self.getTypedRuleContext(GrammarParser.ExpressionContext,0)


        def statement(self):
            return self.getTypedRuleContext(GrammarParser.StatementContext,0)


        def FOR(self):
            return self.getToken(GrammarParser.FOR, 0)

        def forCondition(self):
            return self.getTypedRuleContext(GrammarParser.ForConditionContext,0)


        def getRuleIndex(self):
            return GrammarParser.RULE_iterationStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIterationStatement" ):
                listener.enterIterationStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIterationStatement" ):
                listener.exitIterationStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIterationStatement" ):
                return visitor.visitIterationStatement(self)
            else:
                return visitor.visitChildren(self)




    def iterationStatement(self):

        localctx = GrammarParser.IterationStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_iterationStatement)
        try:
            self.state = 104
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [26]:
                self.enterOuterAlt(localctx, 1)
                self.state = 92
                self.match(GrammarParser.WHILE)
                self.state = 93
                self.match(GrammarParser.T__2)
                self.state = 94
                self.expression()
                self.state = 95
                self.match(GrammarParser.T__3)
                self.state = 96
                self.statement()
                pass
            elif token in [27]:
                self.enterOuterAlt(localctx, 2)
                self.state = 98
                self.match(GrammarParser.FOR)
                self.state = 99
                self.match(GrammarParser.T__2)
                self.state = 100
                self.forCondition()
                self.state = 101
                self.match(GrammarParser.T__3)
                self.state = 102
                self.statement()
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


    class ForConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def forFirst(self):
            return self.getTypedRuleContext(GrammarParser.ForFirstContext,0)


        def forSecond(self):
            return self.getTypedRuleContext(GrammarParser.ForSecondContext,0)


        def forThird(self):
            return self.getTypedRuleContext(GrammarParser.ForThirdContext,0)


        def getRuleIndex(self):
            return GrammarParser.RULE_forCondition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForCondition" ):
                listener.enterForCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForCondition" ):
                listener.exitForCondition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForCondition" ):
                return visitor.visitForCondition(self)
            else:
                return visitor.visitChildren(self)




    def forCondition(self):

        localctx = GrammarParser.ForConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_forCondition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 106
            self.forFirst()
            self.state = 107
            self.forSecond()
            self.state = 108
            self.forThird()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForFirstContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variableDeclaration(self):
            return self.getTypedRuleContext(GrammarParser.VariableDeclarationContext,0)


        def assignmentStatement(self):
            return self.getTypedRuleContext(GrammarParser.AssignmentStatementContext,0)


        def expressionStatement(self):
            return self.getTypedRuleContext(GrammarParser.ExpressionStatementContext,0)


        def TERMINAL(self):
            return self.getToken(GrammarParser.TERMINAL, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_forFirst

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForFirst" ):
                listener.enterForFirst(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForFirst" ):
                listener.exitForFirst(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForFirst" ):
                return visitor.visitForFirst(self)
            else:
                return visitor.visitChildren(self)




    def forFirst(self):

        localctx = GrammarParser.ForFirstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_forFirst)
        try:
            self.state = 114
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 110
                self.variableDeclaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 111
                self.assignmentStatement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 112
                self.expressionStatement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 113
                self.match(GrammarParser.TERMINAL)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForSecondContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expressionStatement(self):
            return self.getTypedRuleContext(GrammarParser.ExpressionStatementContext,0)


        def TERMINAL(self):
            return self.getToken(GrammarParser.TERMINAL, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_forSecond

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForSecond" ):
                listener.enterForSecond(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForSecond" ):
                listener.exitForSecond(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForSecond" ):
                return visitor.visitForSecond(self)
            else:
                return visitor.visitChildren(self)




    def forSecond(self):

        localctx = GrammarParser.ForSecondContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_forSecond)
        try:
            self.state = 118
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3, 10, 11, 12, 29, 30, 31, 32, 33, 34, 35, 36, 47, 50]:
                self.enterOuterAlt(localctx, 1)
                self.state = 116
                self.expressionStatement()
                pass
            elif token in [28]:
                self.enterOuterAlt(localctx, 2)
                self.state = 117
                self.match(GrammarParser.TERMINAL)
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


    class ForThirdContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(GrammarParser.ExpressionContext,0)


        def getRuleIndex(self):
            return GrammarParser.RULE_forThird

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForThird" ):
                listener.enterForThird(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForThird" ):
                listener.exitForThird(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForThird" ):
                return visitor.visitForThird(self)
            else:
                return visitor.visitChildren(self)




    def forThird(self):

        localctx = GrammarParser.ForThirdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_forThird)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 121
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1266774297287688) != 0):
                self.state = 120
                self.expression()


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


        def TERMINAL(self):
            return self.getToken(GrammarParser.TERMINAL, 0)

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
        self.enterRule(localctx, 16, self.RULE_variableDeclaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 123
            self.type_()
            self.state = 124
            self.variableDeclarationQualifiers()
            self.state = 125
            self.match(GrammarParser.TERMINAL)
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
        self.enterRule(localctx, 18, self.RULE_variableDeclarationQualifiers)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 135
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==31:
                self.state = 127
                self.variableDeclarationQualifier()
                self.state = 132
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==7:
                    self.state = 128
                    self.match(GrammarParser.T__6)
                    self.state = 129
                    self.variableDeclarationQualifier()
                    self.state = 134
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
        self.enterRule(localctx, 20, self.RULE_variableDeclarationQualifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 137
            self.match(GrammarParser.ID)
            self.state = 140
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==8:
                self.state = 138
                self.match(GrammarParser.T__7)
                self.state = 139
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
        self.enterRule(localctx, 22, self.RULE_castExpression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 142
            self.match(GrammarParser.T__2)
            self.state = 143
            self.type_()
            self.state = 144
            self.match(GrammarParser.T__3)
            self.state = 145
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


        def iterationStatement(self):
            return self.getTypedRuleContext(GrammarParser.IterationStatementContext,0)


        def TERMINAL(self):
            return self.getToken(GrammarParser.TERMINAL, 0)

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
        self.enterRule(localctx, 24, self.RULE_statement)
        try:
            self.state = 155
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 147
                self.expressionStatement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 148
                self.body()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 149
                self.variableDeclaration()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 150
                self.assignmentStatement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 151
                self.comment()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 152
                self.typedefStatement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 153
                self.iterationStatement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 154
                self.match(GrammarParser.TERMINAL)
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

        def TERMINAL(self):
            return self.getToken(GrammarParser.TERMINAL, 0)

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
        self.enterRule(localctx, 26, self.RULE_typedefStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 157
            self.match(GrammarParser.T__8)
            self.state = 158
            self.type_()
            self.state = 159
            self.match(GrammarParser.ID)
            self.state = 160
            self.match(GrammarParser.TERMINAL)
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


        def TERMINAL(self):
            return self.getToken(GrammarParser.TERMINAL, 0)

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
        self.enterRule(localctx, 28, self.RULE_expressionStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 162
            self.expression()
            self.state = 163
            self.match(GrammarParser.TERMINAL)
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
        self.enterRule(localctx, 30, self.RULE_expression)
        try:
            self.state = 167
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3, 11, 12, 29, 30, 31, 32, 33, 34, 35, 36, 47, 50]:
                self.enterOuterAlt(localctx, 1)
                self.state = 165
                self.logicalExpression(0)
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 2)
                self.state = 166
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
        self.enterRule(localctx, 32, self.RULE_printCall)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 169
            self.match(GrammarParser.T__9)
            self.state = 170
            self.match(GrammarParser.T__2)
            self.state = 171
            self.match(GrammarParser.PRINTFREPLACER)
            self.state = 172
            self.match(GrammarParser.T__6)
            self.state = 173
            self.logicalExpression(0)
            self.state = 174
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


        def TERMINAL(self):
            return self.getToken(GrammarParser.TERMINAL, 0)

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
        self.enterRule(localctx, 34, self.RULE_assignmentStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 176
            self.expression()
            self.state = 177
            self.assignmentOperator()
            self.state = 178
            self.expression()
            self.state = 179
            self.match(GrammarParser.TERMINAL)
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
        _startState = 36
        self.enterRecursionRule(localctx, 36, self.RULE_logicalExpression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 182
            self.comparisonExpression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 189
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = GrammarParser.LogicalExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_logicalExpression)
                    self.state = 184
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 185
                    _la = self._input.LA(1)
                    if not(_la==45 or _la==46):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 186
                    self.comparisonExpression(0) 
                self.state = 191
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

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
        _startState = 38
        self.enterRecursionRule(localctx, 38, self.RULE_comparisonExpression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 193
            self.additiveExpression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 200
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = GrammarParser.ComparisonExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_comparisonExpression)
                    self.state = 195
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 196
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 34634616274944) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 197
                    self.additiveExpression(0) 
                self.state = 202
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

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
        _startState = 40
        self.enterRecursionRule(localctx, 40, self.RULE_additiveExpression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 204
            self.multiplicativeExpression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 211
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = GrammarParser.AdditiveExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_additiveExpression)
                    self.state = 206
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 207
                    _la = self._input.LA(1)
                    if not(_la==34 or _la==35):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 208
                    self.multiplicativeExpression(0) 
                self.state = 213
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

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
        _startState = 42
        self.enterRecursionRule(localctx, 42, self.RULE_multiplicativeExpression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 215
            self.bitwiseExpression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 222
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = GrammarParser.MultiplicativeExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_multiplicativeExpression)
                    self.state = 217
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 218
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 481036337152) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 219
                    self.bitwiseExpression(0) 
                self.state = 224
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

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
        _startState = 44
        self.enterRecursionRule(localctx, 44, self.RULE_bitwiseExpression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 226
            self.shiftExpression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 233
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = GrammarParser.BitwiseExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_bitwiseExpression)
                    self.state = 228
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 229
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 7881299347898368) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 230
                    self.shiftExpression(0) 
                self.state = 235
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

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
        _startState = 46
        self.enterRecursionRule(localctx, 46, self.RULE_shiftExpression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 237
            self.unaryExpression()
            self._ctx.stop = self._input.LT(-1)
            self.state = 244
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = GrammarParser.ShiftExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_shiftExpression)
                    self.state = 239
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 240
                    _la = self._input.LA(1)
                    if not(_la==48 or _la==49):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 241
                    self.unaryExpression() 
                self.state = 246
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

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
        self.enterRule(localctx, 48, self.RULE_unaryExpression)
        self._la = 0 # Token type
        try:
            self.state = 253
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [11, 12, 34, 35, 36, 47, 50]:
                self.enterOuterAlt(localctx, 1)
                self.state = 247
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1266757654288384) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 248
                self.unaryExpression()
                pass
            elif token in [3, 29, 30, 31, 32, 33]:
                self.enterOuterAlt(localctx, 2)
                self.state = 249
                self.primary()
                self.state = 251
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
                if la_ == 1:
                    self.state = 250
                    _la = self._input.LA(1)
                    if not(_la==11 or _la==12):
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
        self.enterRule(localctx, 50, self.RULE_primary)
        try:
            self.state = 265
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 255
                self.match(GrammarParser.NUMBER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 256
                self.match(GrammarParser.FLOAT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 257
                self.match(GrammarParser.T__2)
                self.state = 258
                self.expression()
                self.state = 259
                self.match(GrammarParser.T__3)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 261
                self.match(GrammarParser.ID)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 262
                self.match(GrammarParser.CHAR)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 263
                self.match(GrammarParser.CHAR_ESC)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 264
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
        self.enterRule(localctx, 52, self.RULE_type)
        self._la = 0 # Token type
        try:
            self.state = 278
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 13, 14, 15]:
                self.enterOuterAlt(localctx, 1)
                self.state = 268
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==15:
                    self.state = 267
                    self.const()


                self.state = 270
                self.baseType()
                self.state = 274
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==36:
                    self.state = 271
                    self.addressQualifier()
                    self.state = 276
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            elif token in [31]:
                self.enterOuterAlt(localctx, 2)
                self.state = 277
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
        self.enterRule(localctx, 54, self.RULE_baseType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 280
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 24578) != 0)):
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
        self.enterRule(localctx, 56, self.RULE_const)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 282
            self.match(GrammarParser.T__14)
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
        self.enterRule(localctx, 58, self.RULE_addressQualifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 284
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
        self.enterRule(localctx, 60, self.RULE_assignmentOperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 286
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 67043584) != 0)):
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
        self.enterRule(localctx, 62, self.RULE_comment)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 288
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
        self._predicates[18] = self.logicalExpression_sempred
        self._predicates[19] = self.comparisonExpression_sempred
        self._predicates[20] = self.additiveExpression_sempred
        self._predicates[21] = self.multiplicativeExpression_sempred
        self._predicates[22] = self.bitwiseExpression_sempred
        self._predicates[23] = self.shiftExpression_sempred
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
         




