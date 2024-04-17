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
        4,1,59,303,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,1,0,5,0,70,8,0,10,0,12,0,73,9,0,1,0,1,0,5,0,77,8,0,10,0,12,
        0,80,9,0,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,2,5,2,90,8,2,10,2,12,2,93,
        9,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,
        109,8,3,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,3,5,119,8,5,1,6,1,6,3,6,
        123,8,6,1,7,3,7,126,8,7,1,8,1,8,1,8,1,9,1,9,1,9,1,10,1,10,1,10,1,
        10,1,11,1,11,1,11,5,11,141,8,11,10,11,12,11,144,9,11,3,11,146,8,
        11,1,12,1,12,1,12,3,12,151,8,12,1,13,1,13,1,13,1,13,1,13,1,14,1,
        14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,3,14,168,8,14,1,15,1,
        15,1,15,1,15,1,15,1,16,1,16,1,16,1,17,1,17,3,17,180,8,17,1,18,1,
        18,1,18,1,18,1,18,1,18,1,18,1,19,1,19,1,19,1,19,1,19,1,20,1,20,1,
        20,1,20,1,20,1,20,5,20,200,8,20,10,20,12,20,203,9,20,1,21,1,21,1,
        21,1,21,1,21,1,21,5,21,211,8,21,10,21,12,21,214,9,21,1,22,1,22,1,
        22,1,22,1,22,1,22,5,22,222,8,22,10,22,12,22,225,9,22,1,23,1,23,1,
        23,1,23,1,23,1,23,5,23,233,8,23,10,23,12,23,236,9,23,1,24,1,24,1,
        24,1,24,1,24,1,24,5,24,244,8,24,10,24,12,24,247,9,24,1,25,1,25,1,
        25,1,25,1,25,1,25,5,25,255,8,25,10,25,12,25,258,9,25,1,26,1,26,1,
        26,1,26,3,26,264,8,26,3,26,266,8,26,1,27,1,27,1,27,1,27,1,27,1,27,
        1,27,1,27,1,27,1,27,3,27,278,8,27,1,28,3,28,281,8,28,1,28,1,28,5,
        28,285,8,28,10,28,12,28,288,9,28,1,28,3,28,291,8,28,1,29,1,29,1,
        30,1,30,1,31,1,31,1,32,1,32,1,33,1,33,1,33,0,6,40,42,44,46,48,50,
        34,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,
        44,46,48,50,52,54,56,58,60,62,64,66,0,11,1,0,47,48,1,0,41,46,1,0,
        36,37,1,0,38,40,1,0,52,54,1,0,50,51,4,0,11,12,36,38,49,49,52,52,
        1,0,11,12,2,0,1,1,13,14,2,0,8,8,16,25,1,0,58,59,307,0,71,1,0,0,0,
        2,81,1,0,0,0,4,87,1,0,0,0,6,108,1,0,0,0,8,110,1,0,0,0,10,118,1,0,
        0,0,12,122,1,0,0,0,14,125,1,0,0,0,16,127,1,0,0,0,18,130,1,0,0,0,
        20,133,1,0,0,0,22,145,1,0,0,0,24,147,1,0,0,0,26,152,1,0,0,0,28,167,
        1,0,0,0,30,169,1,0,0,0,32,174,1,0,0,0,34,179,1,0,0,0,36,181,1,0,
        0,0,38,188,1,0,0,0,40,193,1,0,0,0,42,204,1,0,0,0,44,215,1,0,0,0,
        46,226,1,0,0,0,48,237,1,0,0,0,50,248,1,0,0,0,52,265,1,0,0,0,54,277,
        1,0,0,0,56,290,1,0,0,0,58,292,1,0,0,0,60,294,1,0,0,0,62,296,1,0,
        0,0,64,298,1,0,0,0,66,300,1,0,0,0,68,70,3,28,14,0,69,68,1,0,0,0,
        70,73,1,0,0,0,71,69,1,0,0,0,71,72,1,0,0,0,72,74,1,0,0,0,73,71,1,
        0,0,0,74,78,3,2,1,0,75,77,3,28,14,0,76,75,1,0,0,0,77,80,1,0,0,0,
        78,76,1,0,0,0,78,79,1,0,0,0,79,1,1,0,0,0,80,78,1,0,0,0,81,82,5,1,
        0,0,82,83,5,2,0,0,83,84,5,3,0,0,84,85,5,4,0,0,85,86,3,4,2,0,86,3,
        1,0,0,0,87,91,5,5,0,0,88,90,3,28,14,0,89,88,1,0,0,0,90,93,1,0,0,
        0,91,89,1,0,0,0,91,92,1,0,0,0,92,94,1,0,0,0,93,91,1,0,0,0,94,95,
        5,6,0,0,95,5,1,0,0,0,96,97,5,28,0,0,97,98,5,3,0,0,98,99,3,34,17,
        0,99,100,5,4,0,0,100,101,3,28,14,0,101,109,1,0,0,0,102,103,5,29,
        0,0,103,104,5,3,0,0,104,105,3,8,4,0,105,106,5,4,0,0,106,107,3,28,
        14,0,107,109,1,0,0,0,108,96,1,0,0,0,108,102,1,0,0,0,109,7,1,0,0,
        0,110,111,3,10,5,0,111,112,3,12,6,0,112,113,3,14,7,0,113,9,1,0,0,
        0,114,119,3,20,10,0,115,119,3,38,19,0,116,119,3,32,16,0,117,119,
        5,30,0,0,118,114,1,0,0,0,118,115,1,0,0,0,118,116,1,0,0,0,118,117,
        1,0,0,0,119,11,1,0,0,0,120,123,3,32,16,0,121,123,5,30,0,0,122,120,
        1,0,0,0,122,121,1,0,0,0,123,13,1,0,0,0,124,126,3,34,17,0,125,124,
        1,0,0,0,125,126,1,0,0,0,126,15,1,0,0,0,127,128,5,26,0,0,128,129,
        5,30,0,0,129,17,1,0,0,0,130,131,5,27,0,0,131,132,5,30,0,0,132,19,
        1,0,0,0,133,134,3,56,28,0,134,135,3,22,11,0,135,136,5,30,0,0,136,
        21,1,0,0,0,137,142,3,24,12,0,138,139,5,7,0,0,139,141,3,24,12,0,140,
        138,1,0,0,0,141,144,1,0,0,0,142,140,1,0,0,0,142,143,1,0,0,0,143,
        146,1,0,0,0,144,142,1,0,0,0,145,137,1,0,0,0,145,146,1,0,0,0,146,
        23,1,0,0,0,147,150,5,33,0,0,148,149,5,8,0,0,149,151,3,34,17,0,150,
        148,1,0,0,0,150,151,1,0,0,0,151,25,1,0,0,0,152,153,5,3,0,0,153,154,
        3,56,28,0,154,155,5,4,0,0,155,156,3,52,26,0,156,27,1,0,0,0,157,168,
        3,32,16,0,158,168,3,4,2,0,159,168,3,20,10,0,160,168,3,38,19,0,161,
        168,3,66,33,0,162,168,3,30,15,0,163,168,3,6,3,0,164,168,3,16,8,0,
        165,168,3,18,9,0,166,168,5,30,0,0,167,157,1,0,0,0,167,158,1,0,0,
        0,167,159,1,0,0,0,167,160,1,0,0,0,167,161,1,0,0,0,167,162,1,0,0,
        0,167,163,1,0,0,0,167,164,1,0,0,0,167,165,1,0,0,0,167,166,1,0,0,
        0,168,29,1,0,0,0,169,170,5,9,0,0,170,171,3,56,28,0,171,172,5,33,
        0,0,172,173,5,30,0,0,173,31,1,0,0,0,174,175,3,34,17,0,175,176,5,
        30,0,0,176,33,1,0,0,0,177,180,3,40,20,0,178,180,3,36,18,0,179,177,
        1,0,0,0,179,178,1,0,0,0,180,35,1,0,0,0,181,182,5,10,0,0,182,183,
        5,3,0,0,183,184,5,56,0,0,184,185,5,7,0,0,185,186,3,40,20,0,186,187,
        5,4,0,0,187,37,1,0,0,0,188,189,3,34,17,0,189,190,3,64,32,0,190,191,
        3,34,17,0,191,192,5,30,0,0,192,39,1,0,0,0,193,194,6,20,-1,0,194,
        195,3,42,21,0,195,201,1,0,0,0,196,197,10,2,0,0,197,198,7,0,0,0,198,
        200,3,42,21,0,199,196,1,0,0,0,200,203,1,0,0,0,201,199,1,0,0,0,201,
        202,1,0,0,0,202,41,1,0,0,0,203,201,1,0,0,0,204,205,6,21,-1,0,205,
        206,3,44,22,0,206,212,1,0,0,0,207,208,10,2,0,0,208,209,7,1,0,0,209,
        211,3,44,22,0,210,207,1,0,0,0,211,214,1,0,0,0,212,210,1,0,0,0,212,
        213,1,0,0,0,213,43,1,0,0,0,214,212,1,0,0,0,215,216,6,22,-1,0,216,
        217,3,46,23,0,217,223,1,0,0,0,218,219,10,2,0,0,219,220,7,2,0,0,220,
        222,3,46,23,0,221,218,1,0,0,0,222,225,1,0,0,0,223,221,1,0,0,0,223,
        224,1,0,0,0,224,45,1,0,0,0,225,223,1,0,0,0,226,227,6,23,-1,0,227,
        228,3,48,24,0,228,234,1,0,0,0,229,230,10,2,0,0,230,231,7,3,0,0,231,
        233,3,48,24,0,232,229,1,0,0,0,233,236,1,0,0,0,234,232,1,0,0,0,234,
        235,1,0,0,0,235,47,1,0,0,0,236,234,1,0,0,0,237,238,6,24,-1,0,238,
        239,3,50,25,0,239,245,1,0,0,0,240,241,10,2,0,0,241,242,7,4,0,0,242,
        244,3,50,25,0,243,240,1,0,0,0,244,247,1,0,0,0,245,243,1,0,0,0,245,
        246,1,0,0,0,246,49,1,0,0,0,247,245,1,0,0,0,248,249,6,25,-1,0,249,
        250,3,52,26,0,250,256,1,0,0,0,251,252,10,2,0,0,252,253,7,5,0,0,253,
        255,3,52,26,0,254,251,1,0,0,0,255,258,1,0,0,0,256,254,1,0,0,0,256,
        257,1,0,0,0,257,51,1,0,0,0,258,256,1,0,0,0,259,260,7,6,0,0,260,266,
        3,52,26,0,261,263,3,54,27,0,262,264,7,7,0,0,263,262,1,0,0,0,263,
        264,1,0,0,0,264,266,1,0,0,0,265,259,1,0,0,0,265,261,1,0,0,0,266,
        53,1,0,0,0,267,278,5,31,0,0,268,278,5,32,0,0,269,270,5,3,0,0,270,
        271,3,34,17,0,271,272,5,4,0,0,272,278,1,0,0,0,273,278,5,33,0,0,274,
        278,5,34,0,0,275,278,5,35,0,0,276,278,3,26,13,0,277,267,1,0,0,0,
        277,268,1,0,0,0,277,269,1,0,0,0,277,273,1,0,0,0,277,274,1,0,0,0,
        277,275,1,0,0,0,277,276,1,0,0,0,278,55,1,0,0,0,279,281,3,60,30,0,
        280,279,1,0,0,0,280,281,1,0,0,0,281,282,1,0,0,0,282,286,3,58,29,
        0,283,285,3,62,31,0,284,283,1,0,0,0,285,288,1,0,0,0,286,284,1,0,
        0,0,286,287,1,0,0,0,287,291,1,0,0,0,288,286,1,0,0,0,289,291,5,33,
        0,0,290,280,1,0,0,0,290,289,1,0,0,0,291,57,1,0,0,0,292,293,7,8,0,
        0,293,59,1,0,0,0,294,295,5,15,0,0,295,61,1,0,0,0,296,297,5,38,0,
        0,297,63,1,0,0,0,298,299,7,9,0,0,299,65,1,0,0,0,300,301,7,10,0,0,
        301,67,1,0,0,0,24,71,78,91,108,118,122,125,142,145,150,167,179,201,
        212,223,234,245,256,263,265,277,280,286,290
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
                     "'|='", "'break'", "'continue'", "'while'", "'for'", 
                     "';'", "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'+'", "'-'", "'*'", "'/'", "'%'", "'>'", 
                     "'<'", "'=='", "'>='", "'<='", "'!='", "'&&'", "'||'", 
                     "'!'", "'<<'", "'>>'", "'&'", "'|'", "'^'", "'~'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "BREAK", "CONTINUE", "WHILE", 
                      "FOR", "TERMINAL", "NUMBER", "FLOAT", "ID", "CHAR", 
                      "CHAR_ESC", "PLUS", "MINUS", "MUL", "DIV", "MOD", 
                      "GT", "LT", "EQ", "GE", "LE", "NE", "AND", "OR", "NOT", 
                      "LSHIFT", "RSHIFT", "BITAND", "BITOR", "BITXOR", "BITNOT", 
                      "PRINTFREPLACER", "WS", "SINGLE_LINE_COMMENT", "MULTI_LINE_COMMENT" ]

    RULE_program = 0
    RULE_mainFunction = 1
    RULE_body = 2
    RULE_iterationStatement = 3
    RULE_forCondition = 4
    RULE_forFirst = 5
    RULE_forSecond = 6
    RULE_forThird = 7
    RULE_breakStatement = 8
    RULE_continueStatement = 9
    RULE_variableDeclaration = 10
    RULE_variableDeclarationQualifiers = 11
    RULE_variableDeclarationQualifier = 12
    RULE_castExpression = 13
    RULE_statement = 14
    RULE_typedefStatement = 15
    RULE_expressionStatement = 16
    RULE_expression = 17
    RULE_printCall = 18
    RULE_assignmentStatement = 19
    RULE_logicalExpression = 20
    RULE_comparisonExpression = 21
    RULE_additiveExpression = 22
    RULE_multiplicativeExpression = 23
    RULE_bitwiseExpression = 24
    RULE_shiftExpression = 25
    RULE_unaryExpression = 26
    RULE_primary = 27
    RULE_type = 28
    RULE_baseType = 29
    RULE_const = 30
    RULE_addressQualifier = 31
    RULE_assignmentOperator = 32
    RULE_comment = 33

    ruleNames =  [ "program", "mainFunction", "body", "iterationStatement", 
                   "forCondition", "forFirst", "forSecond", "forThird", 
                   "breakStatement", "continueStatement", "variableDeclaration", 
                   "variableDeclarationQualifiers", "variableDeclarationQualifier", 
                   "castExpression", "statement", "typedefStatement", "expressionStatement", 
                   "expression", "printCall", "assignmentStatement", "logicalExpression", 
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
    BREAK=26
    CONTINUE=27
    WHILE=28
    FOR=29
    TERMINAL=30
    NUMBER=31
    FLOAT=32
    ID=33
    CHAR=34
    CHAR_ESC=35
    PLUS=36
    MINUS=37
    MUL=38
    DIV=39
    MOD=40
    GT=41
    LT=42
    EQ=43
    GE=44
    LE=45
    NE=46
    AND=47
    OR=48
    NOT=49
    LSHIFT=50
    RSHIFT=51
    BITAND=52
    BITOR=53
    BITXOR=54
    BITNOT=55
    PRINTFREPLACER=56
    WS=57
    SINGLE_LINE_COMMENT=58
    MULTI_LINE_COMMENT=59

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
            self.state = 71
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 68
                    self.statement() 
                self.state = 73
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

            self.state = 74
            self.mainFunction()
            self.state = 78
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 869758227724697130) != 0):
                self.state = 75
                self.statement()
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
            self.state = 81
            self.match(GrammarParser.T__0)
            self.state = 82
            self.match(GrammarParser.T__1)
            self.state = 83
            self.match(GrammarParser.T__2)
            self.state = 84
            self.match(GrammarParser.T__3)
            self.state = 85
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
            self.state = 87
            self.match(GrammarParser.T__4)
            self.state = 91
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 869758227724697130) != 0):
                self.state = 88
                self.statement()
                self.state = 93
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 94
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
            self.state = 108
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [28]:
                self.enterOuterAlt(localctx, 1)
                self.state = 96
                self.match(GrammarParser.WHILE)
                self.state = 97
                self.match(GrammarParser.T__2)
                self.state = 98
                self.expression()
                self.state = 99
                self.match(GrammarParser.T__3)
                self.state = 100
                self.statement()
                pass
            elif token in [29]:
                self.enterOuterAlt(localctx, 2)
                self.state = 102
                self.match(GrammarParser.FOR)
                self.state = 103
                self.match(GrammarParser.T__2)
                self.state = 104
                self.forCondition()
                self.state = 105
                self.match(GrammarParser.T__3)
                self.state = 106
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
            self.state = 110
            self.forFirst()
            self.state = 111
            self.forSecond()
            self.state = 112
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
            self.state = 118
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 114
                self.variableDeclaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 115
                self.assignmentStatement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 116
                self.expressionStatement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 117
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
            self.state = 122
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3, 10, 11, 12, 31, 32, 33, 34, 35, 36, 37, 38, 49, 52]:
                self.enterOuterAlt(localctx, 1)
                self.state = 120
                self.expressionStatement()
                pass
            elif token in [30]:
                self.enterOuterAlt(localctx, 2)
                self.state = 121
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
            self.state = 125
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 5067097189129224) != 0):
                self.state = 124
                self.expression()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BreakStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(GrammarParser.BREAK, 0)

        def TERMINAL(self):
            return self.getToken(GrammarParser.TERMINAL, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_breakStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBreakStatement" ):
                listener.enterBreakStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBreakStatement" ):
                listener.exitBreakStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreakStatement" ):
                return visitor.visitBreakStatement(self)
            else:
                return visitor.visitChildren(self)




    def breakStatement(self):

        localctx = GrammarParser.BreakStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_breakStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 127
            self.match(GrammarParser.BREAK)
            self.state = 128
            self.match(GrammarParser.TERMINAL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ContinueStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(GrammarParser.CONTINUE, 0)

        def TERMINAL(self):
            return self.getToken(GrammarParser.TERMINAL, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_continueStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterContinueStatement" ):
                listener.enterContinueStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitContinueStatement" ):
                listener.exitContinueStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinueStatement" ):
                return visitor.visitContinueStatement(self)
            else:
                return visitor.visitChildren(self)




    def continueStatement(self):

        localctx = GrammarParser.ContinueStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_continueStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 130
            self.match(GrammarParser.CONTINUE)
            self.state = 131
            self.match(GrammarParser.TERMINAL)
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
        self.enterRule(localctx, 20, self.RULE_variableDeclaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 133
            self.type_()
            self.state = 134
            self.variableDeclarationQualifiers()
            self.state = 135
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
        self.enterRule(localctx, 22, self.RULE_variableDeclarationQualifiers)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 145
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==33:
                self.state = 137
                self.variableDeclarationQualifier()
                self.state = 142
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==7:
                    self.state = 138
                    self.match(GrammarParser.T__6)
                    self.state = 139
                    self.variableDeclarationQualifier()
                    self.state = 144
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
        self.enterRule(localctx, 24, self.RULE_variableDeclarationQualifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 147
            self.match(GrammarParser.ID)
            self.state = 150
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==8:
                self.state = 148
                self.match(GrammarParser.T__7)
                self.state = 149
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
        self.enterRule(localctx, 26, self.RULE_castExpression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 152
            self.match(GrammarParser.T__2)
            self.state = 153
            self.type_()
            self.state = 154
            self.match(GrammarParser.T__3)
            self.state = 155
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


        def breakStatement(self):
            return self.getTypedRuleContext(GrammarParser.BreakStatementContext,0)


        def continueStatement(self):
            return self.getTypedRuleContext(GrammarParser.ContinueStatementContext,0)


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
        self.enterRule(localctx, 28, self.RULE_statement)
        try:
            self.state = 167
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 157
                self.expressionStatement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 158
                self.body()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 159
                self.variableDeclaration()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 160
                self.assignmentStatement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 161
                self.comment()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 162
                self.typedefStatement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 163
                self.iterationStatement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 164
                self.breakStatement()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 165
                self.continueStatement()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 166
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
        self.enterRule(localctx, 30, self.RULE_typedefStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 169
            self.match(GrammarParser.T__8)
            self.state = 170
            self.type_()
            self.state = 171
            self.match(GrammarParser.ID)
            self.state = 172
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
        self.enterRule(localctx, 32, self.RULE_expressionStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 174
            self.expression()
            self.state = 175
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
        self.enterRule(localctx, 34, self.RULE_expression)
        try:
            self.state = 179
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3, 11, 12, 31, 32, 33, 34, 35, 36, 37, 38, 49, 52]:
                self.enterOuterAlt(localctx, 1)
                self.state = 177
                self.logicalExpression(0)
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 2)
                self.state = 178
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
        self.enterRule(localctx, 36, self.RULE_printCall)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 181
            self.match(GrammarParser.T__9)
            self.state = 182
            self.match(GrammarParser.T__2)
            self.state = 183
            self.match(GrammarParser.PRINTFREPLACER)
            self.state = 184
            self.match(GrammarParser.T__6)
            self.state = 185
            self.logicalExpression(0)
            self.state = 186
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
        self.enterRule(localctx, 38, self.RULE_assignmentStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 188
            self.expression()
            self.state = 189
            self.assignmentOperator()
            self.state = 190
            self.expression()
            self.state = 191
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
        _startState = 40
        self.enterRecursionRule(localctx, 40, self.RULE_logicalExpression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 194
            self.comparisonExpression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 201
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = GrammarParser.LogicalExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_logicalExpression)
                    self.state = 196
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 197
                    _la = self._input.LA(1)
                    if not(_la==47 or _la==48):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 198
                    self.comparisonExpression(0) 
                self.state = 203
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
        _startState = 42
        self.enterRecursionRule(localctx, 42, self.RULE_comparisonExpression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 205
            self.additiveExpression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 212
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = GrammarParser.ComparisonExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_comparisonExpression)
                    self.state = 207
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 208
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 138538465099776) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 209
                    self.additiveExpression(0) 
                self.state = 214
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
        _startState = 44
        self.enterRecursionRule(localctx, 44, self.RULE_additiveExpression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 216
            self.multiplicativeExpression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 223
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = GrammarParser.AdditiveExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_additiveExpression)
                    self.state = 218
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 219
                    _la = self._input.LA(1)
                    if not(_la==36 or _la==37):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 220
                    self.multiplicativeExpression(0) 
                self.state = 225
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
        _startState = 46
        self.enterRecursionRule(localctx, 46, self.RULE_multiplicativeExpression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 227
            self.bitwiseExpression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 234
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = GrammarParser.MultiplicativeExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_multiplicativeExpression)
                    self.state = 229
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 230
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1924145348608) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 231
                    self.bitwiseExpression(0) 
                self.state = 236
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
        _startState = 48
        self.enterRecursionRule(localctx, 48, self.RULE_bitwiseExpression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 238
            self.shiftExpression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 245
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = GrammarParser.BitwiseExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_bitwiseExpression)
                    self.state = 240
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 241
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 31525197391593472) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 242
                    self.shiftExpression(0) 
                self.state = 247
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
        _startState = 50
        self.enterRecursionRule(localctx, 50, self.RULE_shiftExpression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 249
            self.unaryExpression()
            self._ctx.stop = self._input.LT(-1)
            self.state = 256
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = GrammarParser.ShiftExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_shiftExpression)
                    self.state = 251
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 252
                    _la = self._input.LA(1)
                    if not(_la==50 or _la==51):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 253
                    self.unaryExpression() 
                self.state = 258
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
        self.enterRule(localctx, 52, self.RULE_unaryExpression)
        self._la = 0 # Token type
        try:
            self.state = 265
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [11, 12, 36, 37, 38, 49, 52]:
                self.enterOuterAlt(localctx, 1)
                self.state = 259
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 5067030617135104) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 260
                self.unaryExpression()
                pass
            elif token in [3, 31, 32, 33, 34, 35]:
                self.enterOuterAlt(localctx, 2)
                self.state = 261
                self.primary()
                self.state = 263
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
                if la_ == 1:
                    self.state = 262
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
        self.enterRule(localctx, 54, self.RULE_primary)
        try:
            self.state = 277
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 267
                self.match(GrammarParser.NUMBER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 268
                self.match(GrammarParser.FLOAT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 269
                self.match(GrammarParser.T__2)
                self.state = 270
                self.expression()
                self.state = 271
                self.match(GrammarParser.T__3)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 273
                self.match(GrammarParser.ID)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 274
                self.match(GrammarParser.CHAR)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 275
                self.match(GrammarParser.CHAR_ESC)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 276
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
        self.enterRule(localctx, 56, self.RULE_type)
        self._la = 0 # Token type
        try:
            self.state = 290
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 13, 14, 15]:
                self.enterOuterAlt(localctx, 1)
                self.state = 280
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==15:
                    self.state = 279
                    self.const()


                self.state = 282
                self.baseType()
                self.state = 286
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==38:
                    self.state = 283
                    self.addressQualifier()
                    self.state = 288
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            elif token in [33]:
                self.enterOuterAlt(localctx, 2)
                self.state = 289
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
        self.enterRule(localctx, 58, self.RULE_baseType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 292
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
        self.enterRule(localctx, 60, self.RULE_const)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 294
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
        self.enterRule(localctx, 62, self.RULE_addressQualifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 296
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
        self.enterRule(localctx, 64, self.RULE_assignmentOperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 298
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
        self.enterRule(localctx, 66, self.RULE_comment)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 300
            _la = self._input.LA(1)
            if not(_la==58 or _la==59):
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
        self._predicates[20] = self.logicalExpression_sempred
        self._predicates[21] = self.comparisonExpression_sempred
        self._predicates[22] = self.additiveExpression_sempred
        self._predicates[23] = self.multiplicativeExpression_sempred
        self._predicates[24] = self.bitwiseExpression_sempred
        self._predicates[25] = self.shiftExpression_sempred
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
         




