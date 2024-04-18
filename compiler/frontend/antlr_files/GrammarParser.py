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
        4,1,61,321,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,1,0,5,0,74,8,0,10,0,12,0,77,9,0,1,0,1,0,
        5,0,81,8,0,10,0,12,0,84,9,0,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,2,5,2,
        94,8,2,10,2,12,2,97,9,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,
        1,3,1,3,1,3,1,3,3,3,113,8,3,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,3,5,
        123,8,5,1,6,1,6,3,6,127,8,6,1,7,3,7,130,8,7,1,8,1,8,1,8,1,9,1,9,
        1,9,1,10,1,10,1,10,1,10,1,11,1,11,1,11,5,11,145,8,11,10,11,12,11,
        148,9,11,3,11,150,8,11,1,12,1,12,1,12,3,12,155,8,12,1,13,1,13,1,
        13,1,13,1,13,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,
        14,3,14,173,8,14,1,15,1,15,1,15,1,15,1,15,1,16,1,16,1,16,1,17,1,
        17,3,17,185,8,17,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,19,1,19,1,
        19,1,19,1,19,1,20,1,20,1,20,1,20,1,20,1,20,3,20,205,8,20,1,21,1,
        21,1,21,3,21,210,8,21,1,22,1,22,1,22,1,22,1,22,1,22,5,22,218,8,22,
        10,22,12,22,221,9,22,1,23,1,23,1,23,1,23,1,23,1,23,5,23,229,8,23,
        10,23,12,23,232,9,23,1,24,1,24,1,24,1,24,1,24,1,24,5,24,240,8,24,
        10,24,12,24,243,9,24,1,25,1,25,1,25,1,25,1,25,1,25,5,25,251,8,25,
        10,25,12,25,254,9,25,1,26,1,26,1,26,1,26,1,26,1,26,5,26,262,8,26,
        10,26,12,26,265,9,26,1,27,1,27,1,27,1,27,1,27,1,27,5,27,273,8,27,
        10,27,12,27,276,9,27,1,28,1,28,1,28,1,28,3,28,282,8,28,3,28,284,
        8,28,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,3,29,296,
        8,29,1,30,3,30,299,8,30,1,30,1,30,3,30,303,8,30,1,30,5,30,306,8,
        30,10,30,12,30,309,9,30,1,31,1,31,1,32,1,32,1,33,1,33,1,34,1,34,
        1,35,1,35,1,35,0,6,44,46,48,50,52,54,36,0,2,4,6,8,10,12,14,16,18,
        20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,
        64,66,68,70,0,11,1,0,49,50,1,0,43,48,1,0,38,39,1,0,40,42,1,0,54,
        56,1,0,52,53,4,0,13,14,38,40,51,51,54,54,1,0,13,14,2,0,1,1,15,16,
        2,0,8,8,18,27,1,0,60,61,326,0,75,1,0,0,0,2,85,1,0,0,0,4,91,1,0,0,
        0,6,112,1,0,0,0,8,114,1,0,0,0,10,122,1,0,0,0,12,126,1,0,0,0,14,129,
        1,0,0,0,16,131,1,0,0,0,18,134,1,0,0,0,20,137,1,0,0,0,22,149,1,0,
        0,0,24,151,1,0,0,0,26,156,1,0,0,0,28,172,1,0,0,0,30,174,1,0,0,0,
        32,179,1,0,0,0,34,184,1,0,0,0,36,186,1,0,0,0,38,193,1,0,0,0,40,198,
        1,0,0,0,42,206,1,0,0,0,44,211,1,0,0,0,46,222,1,0,0,0,48,233,1,0,
        0,0,50,244,1,0,0,0,52,255,1,0,0,0,54,266,1,0,0,0,56,283,1,0,0,0,
        58,295,1,0,0,0,60,298,1,0,0,0,62,310,1,0,0,0,64,312,1,0,0,0,66,314,
        1,0,0,0,68,316,1,0,0,0,70,318,1,0,0,0,72,74,3,28,14,0,73,72,1,0,
        0,0,74,77,1,0,0,0,75,73,1,0,0,0,75,76,1,0,0,0,76,78,1,0,0,0,77,75,
        1,0,0,0,78,82,3,2,1,0,79,81,3,28,14,0,80,79,1,0,0,0,81,84,1,0,0,
        0,82,80,1,0,0,0,82,83,1,0,0,0,83,1,1,0,0,0,84,82,1,0,0,0,85,86,5,
        1,0,0,86,87,5,2,0,0,87,88,5,3,0,0,88,89,5,4,0,0,89,90,3,4,2,0,90,
        3,1,0,0,0,91,95,5,5,0,0,92,94,3,28,14,0,93,92,1,0,0,0,94,97,1,0,
        0,0,95,93,1,0,0,0,95,96,1,0,0,0,96,98,1,0,0,0,97,95,1,0,0,0,98,99,
        5,6,0,0,99,5,1,0,0,0,100,101,5,30,0,0,101,102,5,3,0,0,102,103,3,
        34,17,0,103,104,5,4,0,0,104,105,3,28,14,0,105,113,1,0,0,0,106,107,
        5,31,0,0,107,108,5,3,0,0,108,109,3,8,4,0,109,110,5,4,0,0,110,111,
        3,28,14,0,111,113,1,0,0,0,112,100,1,0,0,0,112,106,1,0,0,0,113,7,
        1,0,0,0,114,115,3,10,5,0,115,116,3,12,6,0,116,117,3,14,7,0,117,9,
        1,0,0,0,118,123,3,20,10,0,119,123,3,38,19,0,120,123,3,32,16,0,121,
        123,5,32,0,0,122,118,1,0,0,0,122,119,1,0,0,0,122,120,1,0,0,0,122,
        121,1,0,0,0,123,11,1,0,0,0,124,127,3,32,16,0,125,127,5,32,0,0,126,
        124,1,0,0,0,126,125,1,0,0,0,127,13,1,0,0,0,128,130,3,34,17,0,129,
        128,1,0,0,0,129,130,1,0,0,0,130,15,1,0,0,0,131,132,5,28,0,0,132,
        133,5,32,0,0,133,17,1,0,0,0,134,135,5,29,0,0,135,136,5,32,0,0,136,
        19,1,0,0,0,137,138,3,60,30,0,138,139,3,22,11,0,139,140,5,32,0,0,
        140,21,1,0,0,0,141,146,3,24,12,0,142,143,5,7,0,0,143,145,3,24,12,
        0,144,142,1,0,0,0,145,148,1,0,0,0,146,144,1,0,0,0,146,147,1,0,0,
        0,147,150,1,0,0,0,148,146,1,0,0,0,149,141,1,0,0,0,149,150,1,0,0,
        0,150,23,1,0,0,0,151,154,5,35,0,0,152,153,5,8,0,0,153,155,3,34,17,
        0,154,152,1,0,0,0,154,155,1,0,0,0,155,25,1,0,0,0,156,157,5,3,0,0,
        157,158,3,60,30,0,158,159,5,4,0,0,159,160,3,56,28,0,160,27,1,0,0,
        0,161,173,3,32,16,0,162,173,3,4,2,0,163,173,3,20,10,0,164,173,3,
        38,19,0,165,173,3,70,35,0,166,173,3,30,15,0,167,173,3,40,20,0,168,
        173,3,6,3,0,169,173,3,16,8,0,170,173,3,18,9,0,171,173,5,32,0,0,172,
        161,1,0,0,0,172,162,1,0,0,0,172,163,1,0,0,0,172,164,1,0,0,0,172,
        165,1,0,0,0,172,166,1,0,0,0,172,167,1,0,0,0,172,168,1,0,0,0,172,
        169,1,0,0,0,172,170,1,0,0,0,172,171,1,0,0,0,173,29,1,0,0,0,174,175,
        5,9,0,0,175,176,3,60,30,0,176,177,5,35,0,0,177,178,5,32,0,0,178,
        31,1,0,0,0,179,180,3,34,17,0,180,181,5,32,0,0,181,33,1,0,0,0,182,
        185,3,44,22,0,183,185,3,36,18,0,184,182,1,0,0,0,184,183,1,0,0,0,
        185,35,1,0,0,0,186,187,5,10,0,0,187,188,5,3,0,0,188,189,5,58,0,0,
        189,190,5,7,0,0,190,191,3,44,22,0,191,192,5,4,0,0,192,37,1,0,0,0,
        193,194,3,34,17,0,194,195,3,68,34,0,195,196,3,34,17,0,196,197,5,
        32,0,0,197,39,1,0,0,0,198,199,5,11,0,0,199,200,5,3,0,0,200,201,3,
        34,17,0,201,202,5,4,0,0,202,204,3,4,2,0,203,205,3,42,21,0,204,203,
        1,0,0,0,204,205,1,0,0,0,205,41,1,0,0,0,206,209,5,12,0,0,207,210,
        3,4,2,0,208,210,3,40,20,0,209,207,1,0,0,0,209,208,1,0,0,0,210,43,
        1,0,0,0,211,212,6,22,-1,0,212,213,3,46,23,0,213,219,1,0,0,0,214,
        215,10,2,0,0,215,216,7,0,0,0,216,218,3,46,23,0,217,214,1,0,0,0,218,
        221,1,0,0,0,219,217,1,0,0,0,219,220,1,0,0,0,220,45,1,0,0,0,221,219,
        1,0,0,0,222,223,6,23,-1,0,223,224,3,48,24,0,224,230,1,0,0,0,225,
        226,10,2,0,0,226,227,7,1,0,0,227,229,3,48,24,0,228,225,1,0,0,0,229,
        232,1,0,0,0,230,228,1,0,0,0,230,231,1,0,0,0,231,47,1,0,0,0,232,230,
        1,0,0,0,233,234,6,24,-1,0,234,235,3,50,25,0,235,241,1,0,0,0,236,
        237,10,2,0,0,237,238,7,2,0,0,238,240,3,50,25,0,239,236,1,0,0,0,240,
        243,1,0,0,0,241,239,1,0,0,0,241,242,1,0,0,0,242,49,1,0,0,0,243,241,
        1,0,0,0,244,245,6,25,-1,0,245,246,3,52,26,0,246,252,1,0,0,0,247,
        248,10,2,0,0,248,249,7,3,0,0,249,251,3,52,26,0,250,247,1,0,0,0,251,
        254,1,0,0,0,252,250,1,0,0,0,252,253,1,0,0,0,253,51,1,0,0,0,254,252,
        1,0,0,0,255,256,6,26,-1,0,256,257,3,54,27,0,257,263,1,0,0,0,258,
        259,10,2,0,0,259,260,7,4,0,0,260,262,3,54,27,0,261,258,1,0,0,0,262,
        265,1,0,0,0,263,261,1,0,0,0,263,264,1,0,0,0,264,53,1,0,0,0,265,263,
        1,0,0,0,266,267,6,27,-1,0,267,268,3,56,28,0,268,274,1,0,0,0,269,
        270,10,2,0,0,270,271,7,5,0,0,271,273,3,56,28,0,272,269,1,0,0,0,273,
        276,1,0,0,0,274,272,1,0,0,0,274,275,1,0,0,0,275,55,1,0,0,0,276,274,
        1,0,0,0,277,278,7,6,0,0,278,284,3,56,28,0,279,281,3,58,29,0,280,
        282,7,7,0,0,281,280,1,0,0,0,281,282,1,0,0,0,282,284,1,0,0,0,283,
        277,1,0,0,0,283,279,1,0,0,0,284,57,1,0,0,0,285,296,5,33,0,0,286,
        296,5,34,0,0,287,288,5,3,0,0,288,289,3,34,17,0,289,290,5,4,0,0,290,
        296,1,0,0,0,291,296,5,35,0,0,292,296,5,36,0,0,293,296,5,37,0,0,294,
        296,3,26,13,0,295,285,1,0,0,0,295,286,1,0,0,0,295,287,1,0,0,0,295,
        291,1,0,0,0,295,292,1,0,0,0,295,293,1,0,0,0,295,294,1,0,0,0,296,
        59,1,0,0,0,297,299,3,64,32,0,298,297,1,0,0,0,298,299,1,0,0,0,299,
        302,1,0,0,0,300,303,3,62,31,0,301,303,5,35,0,0,302,300,1,0,0,0,302,
        301,1,0,0,0,303,307,1,0,0,0,304,306,3,66,33,0,305,304,1,0,0,0,306,
        309,1,0,0,0,307,305,1,0,0,0,307,308,1,0,0,0,308,61,1,0,0,0,309,307,
        1,0,0,0,310,311,7,8,0,0,311,63,1,0,0,0,312,313,5,17,0,0,313,65,1,
        0,0,0,314,315,5,40,0,0,315,67,1,0,0,0,316,317,7,9,0,0,317,69,1,0,
        0,0,318,319,7,10,0,0,319,71,1,0,0,0,26,75,82,95,112,122,126,129,
        146,149,154,172,184,204,209,219,230,241,252,263,274,281,283,295,
        298,302,307
    ]

class GrammarParser ( Parser ):

    grammarFileName = "Grammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'int'", "'main'", "'('", "')'", "'{'", 
                     "'}'", "','", "'='", "'typedef'", "'printf'", "'if'", 
                     "'else'", "'++'", "'--'", "'float'", "'char'", "'const'", 
                     "'+='", "'-='", "'*='", "'/='", "'%='", "'<<='", "'>>='", 
                     "'&='", "'^='", "'|='", "'break'", "'continue'", "'while'", 
                     "'for'", "';'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'+'", "'-'", "'*'", "'/'", 
                     "'%'", "'>'", "'<'", "'=='", "'>='", "'<='", "'!='", 
                     "'&&'", "'||'", "'!'", "'<<'", "'>>'", "'&'", "'|'", 
                     "'^'", "'~'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "BREAK", "CONTINUE", "WHILE", "FOR", "TERMINAL", "NUMBER", 
                      "FLOAT", "ID", "CHAR", "CHAR_ESC", "PLUS", "MINUS", 
                      "MUL", "DIV", "MOD", "GT", "LT", "EQ", "GE", "LE", 
                      "NE", "AND", "OR", "NOT", "LSHIFT", "RSHIFT", "BITAND", 
                      "BITOR", "BITXOR", "BITNOT", "PRINTFREPLACER", "WS", 
                      "SINGLE_LINE_COMMENT", "MULTI_LINE_COMMENT" ]

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
    RULE_ifStatement = 20
    RULE_elseStatement = 21
    RULE_logicalExpression = 22
    RULE_comparisonExpression = 23
    RULE_additiveExpression = 24
    RULE_multiplicativeExpression = 25
    RULE_bitwiseExpression = 26
    RULE_shiftExpression = 27
    RULE_unaryExpression = 28
    RULE_primary = 29
    RULE_type = 30
    RULE_baseType = 31
    RULE_const = 32
    RULE_addressQualifier = 33
    RULE_assignmentOperator = 34
    RULE_comment = 35

    ruleNames =  [ "program", "mainFunction", "body", "iterationStatement", 
                   "forCondition", "forFirst", "forSecond", "forThird", 
                   "breakStatement", "continueStatement", "variableDeclaration", 
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
    BREAK=28
    CONTINUE=29
    WHILE=30
    FOR=31
    TERMINAL=32
    NUMBER=33
    FLOAT=34
    ID=35
    CHAR=36
    CHAR_ESC=37
    PLUS=38
    MINUS=39
    MUL=40
    DIV=41
    MOD=42
    GT=43
    LT=44
    EQ=45
    GE=46
    LE=47
    NE=48
    AND=49
    OR=50
    NOT=51
    LSHIFT=52
    RSHIFT=53
    BITAND=54
    BITOR=55
    BITXOR=56
    BITNOT=57
    PRINTFREPLACER=58
    WS=59
    SINGLE_LINE_COMMENT=60
    MULTI_LINE_COMMENT=61

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
            self.state = 75
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 72
                    self.statement() 
                self.state = 77
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

            self.state = 78
            self.mainFunction()
            self.state = 82
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 3479032910898785834) != 0):
                self.state = 79
                self.statement()
                self.state = 84
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
            self.state = 85
            self.match(GrammarParser.T__0)
            self.state = 86
            self.match(GrammarParser.T__1)
            self.state = 87
            self.match(GrammarParser.T__2)
            self.state = 88
            self.match(GrammarParser.T__3)
            self.state = 89
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
            self.state = 91
            self.match(GrammarParser.T__4)
            self.state = 95
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 3479032910898785834) != 0):
                self.state = 92
                self.statement()
                self.state = 97
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 98
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
            self.state = 112
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [30]:
                self.enterOuterAlt(localctx, 1)
                self.state = 100
                self.match(GrammarParser.WHILE)
                self.state = 101
                self.match(GrammarParser.T__2)
                self.state = 102
                self.expression()
                self.state = 103
                self.match(GrammarParser.T__3)
                self.state = 104
                self.statement()
                pass
            elif token in [31]:
                self.enterOuterAlt(localctx, 2)
                self.state = 106
                self.match(GrammarParser.FOR)
                self.state = 107
                self.match(GrammarParser.T__2)
                self.state = 108
                self.forCondition()
                self.state = 109
                self.match(GrammarParser.T__3)
                self.state = 110
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
            self.state = 114
            self.forFirst()
            self.state = 115
            self.forSecond()
            self.state = 116
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
            self.state = 122
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 118
                self.variableDeclaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 119
                self.assignmentStatement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 120
                self.expressionStatement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 121
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
            self.state = 126
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3, 10, 13, 14, 33, 34, 35, 36, 37, 38, 39, 40, 51, 54]:
                self.enterOuterAlt(localctx, 1)
                self.state = 124
                self.expressionStatement()
                pass
            elif token in [32]:
                self.enterOuterAlt(localctx, 2)
                self.state = 125
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
            self.state = 129
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 20268388756513800) != 0):
                self.state = 128
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
            self.state = 131
            self.match(GrammarParser.BREAK)
            self.state = 132
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
            self.state = 134
            self.match(GrammarParser.CONTINUE)
            self.state = 135
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
            self.state = 137
            self.type_()
            self.state = 138
            self.variableDeclarationQualifiers()
            self.state = 139
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
            self.state = 149
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==35:
                self.state = 141
                self.variableDeclarationQualifier()
                self.state = 146
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==7:
                    self.state = 142
                    self.match(GrammarParser.T__6)
                    self.state = 143
                    self.variableDeclarationQualifier()
                    self.state = 148
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
            self.state = 151
            self.match(GrammarParser.ID)
            self.state = 154
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==8:
                self.state = 152
                self.match(GrammarParser.T__7)
                self.state = 153
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
            self.state = 156
            self.match(GrammarParser.T__2)
            self.state = 157
            self.type_()
            self.state = 158
            self.match(GrammarParser.T__3)
            self.state = 159
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
            self.state = 172
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 161
                self.expressionStatement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 162
                self.body()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 163
                self.variableDeclaration()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 164
                self.assignmentStatement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 165
                self.comment()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 166
                self.typedefStatement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 167
                self.ifStatement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 168
                self.iterationStatement()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 169
                self.breakStatement()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 170
                self.continueStatement()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 171
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
            self.state = 174
            self.match(GrammarParser.T__8)
            self.state = 175
            self.type_()
            self.state = 176
            self.match(GrammarParser.ID)
            self.state = 177
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
            self.state = 179
            self.expression()
            self.state = 180
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
            self.state = 184
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3, 13, 14, 33, 34, 35, 36, 37, 38, 39, 40, 51, 54]:
                self.enterOuterAlt(localctx, 1)
                self.state = 182
                self.logicalExpression(0)
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 2)
                self.state = 183
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
            self.state = 186
            self.match(GrammarParser.T__9)
            self.state = 187
            self.match(GrammarParser.T__2)
            self.state = 188
            self.match(GrammarParser.PRINTFREPLACER)
            self.state = 189
            self.match(GrammarParser.T__6)
            self.state = 190
            self.logicalExpression(0)
            self.state = 191
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
            self.state = 193
            self.expression()
            self.state = 194
            self.assignmentOperator()
            self.state = 195
            self.expression()
            self.state = 196
            self.match(GrammarParser.TERMINAL)
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
        self.enterRule(localctx, 40, self.RULE_ifStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 198
            self.match(GrammarParser.T__10)
            self.state = 199
            self.match(GrammarParser.T__2)
            self.state = 200
            self.expression()
            self.state = 201
            self.match(GrammarParser.T__3)
            self.state = 202
            self.body()
            self.state = 204
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==12:
                self.state = 203
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
        self.enterRule(localctx, 42, self.RULE_elseStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 206
            self.match(GrammarParser.T__11)
            self.state = 209
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [5]:
                self.state = 207
                self.body()
                pass
            elif token in [11]:
                self.state = 208
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
        _startState = 44
        self.enterRecursionRule(localctx, 44, self.RULE_logicalExpression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 212
            self.comparisonExpression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 219
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = GrammarParser.LogicalExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_logicalExpression)
                    self.state = 214
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 215
                    _la = self._input.LA(1)
                    if not(_la==49 or _la==50):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 216
                    self.comparisonExpression(0) 
                self.state = 221
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

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
        _startState = 46
        self.enterRecursionRule(localctx, 46, self.RULE_comparisonExpression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 223
            self.additiveExpression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 230
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = GrammarParser.ComparisonExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_comparisonExpression)
                    self.state = 225
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 226
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 554153860399104) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 227
                    self.additiveExpression(0) 
                self.state = 232
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

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
        _startState = 48
        self.enterRecursionRule(localctx, 48, self.RULE_additiveExpression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 234
            self.multiplicativeExpression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 241
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = GrammarParser.AdditiveExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_additiveExpression)
                    self.state = 236
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 237
                    _la = self._input.LA(1)
                    if not(_la==38 or _la==39):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 238
                    self.multiplicativeExpression(0) 
                self.state = 243
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

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
        _startState = 50
        self.enterRecursionRule(localctx, 50, self.RULE_multiplicativeExpression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 245
            self.bitwiseExpression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 252
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = GrammarParser.MultiplicativeExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_multiplicativeExpression)
                    self.state = 247
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 248
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 7696581394432) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 249
                    self.bitwiseExpression(0) 
                self.state = 254
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

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
        _startState = 52
        self.enterRecursionRule(localctx, 52, self.RULE_bitwiseExpression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 256
            self.shiftExpression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 263
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,18,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = GrammarParser.BitwiseExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_bitwiseExpression)
                    self.state = 258
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 259
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 126100789566373888) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 260
                    self.shiftExpression(0) 
                self.state = 265
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

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
        _startState = 54
        self.enterRecursionRule(localctx, 54, self.RULE_shiftExpression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 267
            self.unaryExpression()
            self._ctx.stop = self._input.LT(-1)
            self.state = 274
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = GrammarParser.ShiftExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_shiftExpression)
                    self.state = 269
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 270
                    _la = self._input.LA(1)
                    if not(_la==52 or _la==53):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 271
                    self.unaryExpression() 
                self.state = 276
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

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
        self.enterRule(localctx, 56, self.RULE_unaryExpression)
        self._la = 0 # Token type
        try:
            self.state = 283
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [13, 14, 38, 39, 40, 51, 54]:
                self.enterOuterAlt(localctx, 1)
                self.state = 277
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 20268122468540416) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 278
                self.unaryExpression()
                pass
            elif token in [3, 33, 34, 35, 36, 37]:
                self.enterOuterAlt(localctx, 2)
                self.state = 279
                self.primary()
                self.state = 281
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
                if la_ == 1:
                    self.state = 280
                    _la = self._input.LA(1)
                    if not(_la==13 or _la==14):
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
        self.enterRule(localctx, 58, self.RULE_primary)
        try:
            self.state = 295
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 285
                self.match(GrammarParser.NUMBER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 286
                self.match(GrammarParser.FLOAT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 287
                self.match(GrammarParser.T__2)
                self.state = 288
                self.expression()
                self.state = 289
                self.match(GrammarParser.T__3)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 291
                self.match(GrammarParser.ID)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 292
                self.match(GrammarParser.CHAR)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 293
                self.match(GrammarParser.CHAR_ESC)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 294
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


        def ID(self):
            return self.getToken(GrammarParser.ID, 0)

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
        self.enterRule(localctx, 60, self.RULE_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 298
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==17:
                self.state = 297
                self.const()


            self.state = 302
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 15, 16]:
                self.state = 300
                self.baseType()
                pass
            elif token in [35]:
                self.state = 301
                self.match(GrammarParser.ID)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 307
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==40:
                self.state = 304
                self.addressQualifier()
                self.state = 309
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
        self.enterRule(localctx, 62, self.RULE_baseType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 310
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 98306) != 0)):
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
        self.enterRule(localctx, 64, self.RULE_const)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 312
            self.match(GrammarParser.T__16)
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
        self.enterRule(localctx, 66, self.RULE_addressQualifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 314
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
        self.enterRule(localctx, 68, self.RULE_assignmentOperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 316
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 268173568) != 0)):
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
        self.enterRule(localctx, 70, self.RULE_comment)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 318
            _la = self._input.LA(1)
            if not(_la==60 or _la==61):
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
        self._predicates[22] = self.logicalExpression_sempred
        self._predicates[23] = self.comparisonExpression_sempred
        self._predicates[24] = self.additiveExpression_sempred
        self._predicates[25] = self.multiplicativeExpression_sempred
        self._predicates[26] = self.bitwiseExpression_sempred
        self._predicates[27] = self.shiftExpression_sempred
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
         




