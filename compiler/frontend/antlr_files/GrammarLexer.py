# Generated from Grammar.g4 by ANTLR 4.13.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,66,442,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,
        2,6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,
        13,7,13,2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,
        19,2,20,7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,
        26,7,26,2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,
        32,2,33,7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,
        39,7,39,2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,
        45,2,46,7,46,2,47,7,47,2,48,7,48,2,49,7,49,2,50,7,50,2,51,7,51,2,
        52,7,52,2,53,7,53,2,54,7,54,2,55,7,55,2,56,7,56,2,57,7,57,2,58,7,
        58,2,59,7,59,2,60,7,60,2,61,7,61,2,62,7,62,2,63,7,63,2,64,7,64,2,
        65,7,65,1,0,1,0,1,1,1,1,1,2,1,2,1,3,1,3,1,4,1,4,1,5,1,5,1,5,1,5,
        1,5,1,5,1,5,1,6,1,6,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,9,
        1,9,1,9,1,10,1,10,1,10,1,11,1,11,1,11,1,11,1,12,1,12,1,12,1,12,1,
        12,1,12,1,13,1,13,1,13,1,13,1,13,1,14,1,14,1,14,1,14,1,14,1,15,1,
        15,1,15,1,15,1,15,1,15,1,16,1,16,1,16,1,17,1,17,1,17,1,18,1,18,1,
        18,1,19,1,19,1,19,1,20,1,20,1,20,1,21,1,21,1,21,1,21,1,22,1,22,1,
        22,1,22,1,23,1,23,1,23,1,24,1,24,1,24,1,25,1,25,1,25,1,26,1,26,1,
        26,1,26,1,26,1,26,1,26,1,27,1,27,1,27,1,27,1,27,1,28,1,28,1,28,1,
        28,1,28,1,28,1,28,1,28,1,29,1,29,1,29,1,30,1,30,1,30,1,30,1,30,1,
        31,1,31,1,31,1,31,1,31,1,31,1,32,1,32,1,32,1,32,1,32,1,32,1,32,1,
        33,1,33,1,33,1,33,1,33,1,33,1,33,1,33,1,33,1,34,1,34,1,34,1,34,1,
        34,1,34,1,35,1,35,1,35,1,35,1,36,1,36,1,37,1,37,1,37,5,37,292,8,
        37,10,37,12,37,295,9,37,3,37,297,8,37,1,38,4,38,300,8,38,11,38,12,
        38,301,1,38,1,38,5,38,306,8,38,10,38,12,38,309,9,38,1,38,1,38,4,
        38,313,8,38,11,38,12,38,314,3,38,317,8,38,1,39,1,39,5,39,321,8,39,
        10,39,12,39,324,9,39,1,40,1,40,1,40,1,40,1,41,1,41,1,41,1,41,1,41,
        1,41,1,41,1,41,3,41,338,8,41,1,41,1,41,1,42,1,42,1,43,1,43,1,44,
        1,44,1,45,1,45,1,46,1,46,1,47,1,47,1,48,1,48,1,49,1,49,1,49,1,50,
        1,50,1,50,1,51,1,51,1,51,1,52,1,52,1,52,1,53,1,53,1,53,1,54,1,54,
        1,54,1,55,1,55,1,56,1,56,1,56,1,57,1,57,1,57,1,58,1,58,1,59,1,59,
        1,60,1,60,1,61,1,61,1,62,1,62,1,62,1,62,1,62,1,62,1,62,1,62,1,62,
        1,62,1,62,1,62,1,62,1,62,1,62,1,62,1,62,1,62,1,62,1,62,3,62,410,
        8,62,1,63,4,63,413,8,63,11,63,12,63,414,1,63,1,63,1,64,1,64,1,64,
        1,64,5,64,423,8,64,10,64,12,64,426,9,64,1,64,3,64,429,8,64,1,65,
        1,65,1,65,1,65,5,65,435,8,65,10,65,12,65,438,9,65,1,65,1,65,1,65,
        2,424,436,0,66,1,1,3,2,5,3,7,4,9,5,11,6,13,7,15,8,17,9,19,10,21,
        11,23,12,25,13,27,14,29,15,31,16,33,17,35,18,37,19,39,20,41,21,43,
        22,45,23,47,24,49,25,51,26,53,27,55,28,57,29,59,30,61,31,63,32,65,
        33,67,34,69,35,71,36,73,37,75,38,77,39,79,40,81,41,83,42,85,43,87,
        44,89,45,91,46,93,47,95,48,97,49,99,50,101,51,103,52,105,53,107,
        54,109,55,111,56,113,57,115,58,117,59,119,60,121,61,123,62,125,63,
        127,64,129,65,131,66,1,0,7,1,0,49,57,1,0,48,57,3,0,65,90,95,95,97,
        122,4,0,48,57,65,90,95,95,97,122,1,0,0,255,3,0,9,10,13,13,32,32,
        1,1,10,10,458,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,
        9,1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,0,0,15,1,0,0,0,0,17,1,0,0,0,0,
        19,1,0,0,0,0,21,1,0,0,0,0,23,1,0,0,0,0,25,1,0,0,0,0,27,1,0,0,0,0,
        29,1,0,0,0,0,31,1,0,0,0,0,33,1,0,0,0,0,35,1,0,0,0,0,37,1,0,0,0,0,
        39,1,0,0,0,0,41,1,0,0,0,0,43,1,0,0,0,0,45,1,0,0,0,0,47,1,0,0,0,0,
        49,1,0,0,0,0,51,1,0,0,0,0,53,1,0,0,0,0,55,1,0,0,0,0,57,1,0,0,0,0,
        59,1,0,0,0,0,61,1,0,0,0,0,63,1,0,0,0,0,65,1,0,0,0,0,67,1,0,0,0,0,
        69,1,0,0,0,0,71,1,0,0,0,0,73,1,0,0,0,0,75,1,0,0,0,0,77,1,0,0,0,0,
        79,1,0,0,0,0,81,1,0,0,0,0,83,1,0,0,0,0,85,1,0,0,0,0,87,1,0,0,0,0,
        89,1,0,0,0,0,91,1,0,0,0,0,93,1,0,0,0,0,95,1,0,0,0,0,97,1,0,0,0,0,
        99,1,0,0,0,0,101,1,0,0,0,0,103,1,0,0,0,0,105,1,0,0,0,0,107,1,0,0,
        0,0,109,1,0,0,0,0,111,1,0,0,0,0,113,1,0,0,0,0,115,1,0,0,0,0,117,
        1,0,0,0,0,119,1,0,0,0,0,121,1,0,0,0,0,123,1,0,0,0,0,125,1,0,0,0,
        0,127,1,0,0,0,0,129,1,0,0,0,0,131,1,0,0,0,1,133,1,0,0,0,3,135,1,
        0,0,0,5,137,1,0,0,0,7,139,1,0,0,0,9,141,1,0,0,0,11,143,1,0,0,0,13,
        150,1,0,0,0,15,152,1,0,0,0,17,154,1,0,0,0,19,162,1,0,0,0,21,165,
        1,0,0,0,23,168,1,0,0,0,25,172,1,0,0,0,27,178,1,0,0,0,29,183,1,0,
        0,0,31,188,1,0,0,0,33,194,1,0,0,0,35,197,1,0,0,0,37,200,1,0,0,0,
        39,203,1,0,0,0,41,206,1,0,0,0,43,209,1,0,0,0,45,213,1,0,0,0,47,217,
        1,0,0,0,49,220,1,0,0,0,51,223,1,0,0,0,53,226,1,0,0,0,55,233,1,0,
        0,0,57,238,1,0,0,0,59,246,1,0,0,0,61,249,1,0,0,0,63,254,1,0,0,0,
        65,260,1,0,0,0,67,267,1,0,0,0,69,276,1,0,0,0,71,282,1,0,0,0,73,286,
        1,0,0,0,75,296,1,0,0,0,77,316,1,0,0,0,79,318,1,0,0,0,81,325,1,0,
        0,0,83,329,1,0,0,0,85,341,1,0,0,0,87,343,1,0,0,0,89,345,1,0,0,0,
        91,347,1,0,0,0,93,349,1,0,0,0,95,351,1,0,0,0,97,353,1,0,0,0,99,355,
        1,0,0,0,101,358,1,0,0,0,103,361,1,0,0,0,105,364,1,0,0,0,107,367,
        1,0,0,0,109,370,1,0,0,0,111,373,1,0,0,0,113,375,1,0,0,0,115,378,
        1,0,0,0,117,381,1,0,0,0,119,383,1,0,0,0,121,385,1,0,0,0,123,387,
        1,0,0,0,125,409,1,0,0,0,127,412,1,0,0,0,129,418,1,0,0,0,131,430,
        1,0,0,0,133,134,5,40,0,0,134,2,1,0,0,0,135,136,5,41,0,0,136,4,1,
        0,0,0,137,138,5,44,0,0,138,6,1,0,0,0,139,140,5,123,0,0,140,8,1,0,
        0,0,141,142,5,125,0,0,142,10,1,0,0,0,143,144,5,112,0,0,144,145,5,
        114,0,0,145,146,5,105,0,0,146,147,5,110,0,0,147,148,5,116,0,0,148,
        149,5,102,0,0,149,12,1,0,0,0,150,151,5,61,0,0,151,14,1,0,0,0,152,
        153,5,58,0,0,153,16,1,0,0,0,154,155,5,116,0,0,155,156,5,121,0,0,
        156,157,5,112,0,0,157,158,5,101,0,0,158,159,5,100,0,0,159,160,5,
        101,0,0,160,161,5,102,0,0,161,18,1,0,0,0,162,163,5,43,0,0,163,164,
        5,43,0,0,164,20,1,0,0,0,165,166,5,45,0,0,166,167,5,45,0,0,167,22,
        1,0,0,0,168,169,5,105,0,0,169,170,5,110,0,0,170,171,5,116,0,0,171,
        24,1,0,0,0,172,173,5,102,0,0,173,174,5,108,0,0,174,175,5,111,0,0,
        175,176,5,97,0,0,176,177,5,116,0,0,177,26,1,0,0,0,178,179,5,99,0,
        0,179,180,5,104,0,0,180,181,5,97,0,0,181,182,5,114,0,0,182,28,1,
        0,0,0,183,184,5,118,0,0,184,185,5,111,0,0,185,186,5,105,0,0,186,
        187,5,100,0,0,187,30,1,0,0,0,188,189,5,99,0,0,189,190,5,111,0,0,
        190,191,5,110,0,0,191,192,5,115,0,0,192,193,5,116,0,0,193,32,1,0,
        0,0,194,195,5,43,0,0,195,196,5,61,0,0,196,34,1,0,0,0,197,198,5,45,
        0,0,198,199,5,61,0,0,199,36,1,0,0,0,200,201,5,42,0,0,201,202,5,61,
        0,0,202,38,1,0,0,0,203,204,5,47,0,0,204,205,5,61,0,0,205,40,1,0,
        0,0,206,207,5,37,0,0,207,208,5,61,0,0,208,42,1,0,0,0,209,210,5,60,
        0,0,210,211,5,60,0,0,211,212,5,61,0,0,212,44,1,0,0,0,213,214,5,62,
        0,0,214,215,5,62,0,0,215,216,5,61,0,0,216,46,1,0,0,0,217,218,5,38,
        0,0,218,219,5,61,0,0,219,48,1,0,0,0,220,221,5,94,0,0,221,222,5,61,
        0,0,222,50,1,0,0,0,223,224,5,124,0,0,224,225,5,61,0,0,225,52,1,0,
        0,0,226,227,5,115,0,0,227,228,5,119,0,0,228,229,5,105,0,0,229,230,
        5,116,0,0,230,231,5,99,0,0,231,232,5,104,0,0,232,54,1,0,0,0,233,
        234,5,99,0,0,234,235,5,97,0,0,235,236,5,115,0,0,236,237,5,101,0,
        0,237,56,1,0,0,0,238,239,5,100,0,0,239,240,5,101,0,0,240,241,5,102,
        0,0,241,242,5,97,0,0,242,243,5,117,0,0,243,244,5,108,0,0,244,245,
        5,116,0,0,245,58,1,0,0,0,246,247,5,105,0,0,247,248,5,102,0,0,248,
        60,1,0,0,0,249,250,5,101,0,0,250,251,5,108,0,0,251,252,5,115,0,0,
        252,253,5,101,0,0,253,62,1,0,0,0,254,255,5,98,0,0,255,256,5,114,
        0,0,256,257,5,101,0,0,257,258,5,97,0,0,258,259,5,107,0,0,259,64,
        1,0,0,0,260,261,5,114,0,0,261,262,5,101,0,0,262,263,5,116,0,0,263,
        264,5,117,0,0,264,265,5,114,0,0,265,266,5,110,0,0,266,66,1,0,0,0,
        267,268,5,99,0,0,268,269,5,111,0,0,269,270,5,110,0,0,270,271,5,116,
        0,0,271,272,5,105,0,0,272,273,5,110,0,0,273,274,5,117,0,0,274,275,
        5,101,0,0,275,68,1,0,0,0,276,277,5,119,0,0,277,278,5,104,0,0,278,
        279,5,105,0,0,279,280,5,108,0,0,280,281,5,101,0,0,281,70,1,0,0,0,
        282,283,5,102,0,0,283,284,5,111,0,0,284,285,5,114,0,0,285,72,1,0,
        0,0,286,287,5,59,0,0,287,74,1,0,0,0,288,297,5,48,0,0,289,293,7,0,
        0,0,290,292,7,1,0,0,291,290,1,0,0,0,292,295,1,0,0,0,293,291,1,0,
        0,0,293,294,1,0,0,0,294,297,1,0,0,0,295,293,1,0,0,0,296,288,1,0,
        0,0,296,289,1,0,0,0,297,76,1,0,0,0,298,300,7,1,0,0,299,298,1,0,0,
        0,300,301,1,0,0,0,301,299,1,0,0,0,301,302,1,0,0,0,302,303,1,0,0,
        0,303,307,5,46,0,0,304,306,7,1,0,0,305,304,1,0,0,0,306,309,1,0,0,
        0,307,305,1,0,0,0,307,308,1,0,0,0,308,317,1,0,0,0,309,307,1,0,0,
        0,310,312,5,46,0,0,311,313,7,1,0,0,312,311,1,0,0,0,313,314,1,0,0,
        0,314,312,1,0,0,0,314,315,1,0,0,0,315,317,1,0,0,0,316,299,1,0,0,
        0,316,310,1,0,0,0,317,78,1,0,0,0,318,322,7,2,0,0,319,321,7,3,0,0,
        320,319,1,0,0,0,321,324,1,0,0,0,322,320,1,0,0,0,322,323,1,0,0,0,
        323,80,1,0,0,0,324,322,1,0,0,0,325,326,5,39,0,0,326,327,7,4,0,0,
        327,328,5,39,0,0,328,82,1,0,0,0,329,337,5,39,0,0,330,331,5,92,0,
        0,331,338,5,110,0,0,332,333,5,92,0,0,333,338,5,116,0,0,334,335,5,
        92,0,0,335,338,5,48,0,0,336,338,9,0,0,0,337,330,1,0,0,0,337,332,
        1,0,0,0,337,334,1,0,0,0,337,336,1,0,0,0,338,339,1,0,0,0,339,340,
        5,39,0,0,340,84,1,0,0,0,341,342,5,43,0,0,342,86,1,0,0,0,343,344,
        5,45,0,0,344,88,1,0,0,0,345,346,5,42,0,0,346,90,1,0,0,0,347,348,
        5,47,0,0,348,92,1,0,0,0,349,350,5,37,0,0,350,94,1,0,0,0,351,352,
        5,62,0,0,352,96,1,0,0,0,353,354,5,60,0,0,354,98,1,0,0,0,355,356,
        5,61,0,0,356,357,5,61,0,0,357,100,1,0,0,0,358,359,5,62,0,0,359,360,
        5,61,0,0,360,102,1,0,0,0,361,362,5,60,0,0,362,363,5,61,0,0,363,104,
        1,0,0,0,364,365,5,33,0,0,365,366,5,61,0,0,366,106,1,0,0,0,367,368,
        5,38,0,0,368,369,5,38,0,0,369,108,1,0,0,0,370,371,5,124,0,0,371,
        372,5,124,0,0,372,110,1,0,0,0,373,374,5,33,0,0,374,112,1,0,0,0,375,
        376,5,60,0,0,376,377,5,60,0,0,377,114,1,0,0,0,378,379,5,62,0,0,379,
        380,5,62,0,0,380,116,1,0,0,0,381,382,5,38,0,0,382,118,1,0,0,0,383,
        384,5,124,0,0,384,120,1,0,0,0,385,386,5,94,0,0,386,122,1,0,0,0,387,
        388,5,126,0,0,388,124,1,0,0,0,389,390,5,34,0,0,390,391,5,37,0,0,
        391,392,5,115,0,0,392,410,5,34,0,0,393,394,5,34,0,0,394,395,5,37,
        0,0,395,396,5,100,0,0,396,410,5,34,0,0,397,398,5,34,0,0,398,399,
        5,37,0,0,399,400,5,120,0,0,400,410,5,34,0,0,401,402,5,34,0,0,402,
        403,5,37,0,0,403,404,5,102,0,0,404,410,5,34,0,0,405,406,5,34,0,0,
        406,407,5,37,0,0,407,408,5,99,0,0,408,410,5,34,0,0,409,389,1,0,0,
        0,409,393,1,0,0,0,409,397,1,0,0,0,409,401,1,0,0,0,409,405,1,0,0,
        0,410,126,1,0,0,0,411,413,7,5,0,0,412,411,1,0,0,0,413,414,1,0,0,
        0,414,412,1,0,0,0,414,415,1,0,0,0,415,416,1,0,0,0,416,417,6,63,0,
        0,417,128,1,0,0,0,418,419,5,47,0,0,419,420,5,47,0,0,420,424,1,0,
        0,0,421,423,9,0,0,0,422,421,1,0,0,0,423,426,1,0,0,0,424,425,1,0,
        0,0,424,422,1,0,0,0,425,428,1,0,0,0,426,424,1,0,0,0,427,429,7,6,
        0,0,428,427,1,0,0,0,429,130,1,0,0,0,430,431,5,47,0,0,431,432,5,42,
        0,0,432,436,1,0,0,0,433,435,9,0,0,0,434,433,1,0,0,0,435,438,1,0,
        0,0,436,437,1,0,0,0,436,434,1,0,0,0,437,439,1,0,0,0,438,436,1,0,
        0,0,439,440,5,42,0,0,440,441,5,47,0,0,441,132,1,0,0,0,14,0,293,296,
        301,307,314,316,322,337,409,414,424,428,436,1,6,0,0
    ]

class GrammarLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    T__9 = 10
    T__10 = 11
    T__11 = 12
    T__12 = 13
    T__13 = 14
    T__14 = 15
    T__15 = 16
    T__16 = 17
    T__17 = 18
    T__18 = 19
    T__19 = 20
    T__20 = 21
    T__21 = 22
    T__22 = 23
    T__23 = 24
    T__24 = 25
    T__25 = 26
    SWITCH = 27
    CASE = 28
    DEFAULT = 29
    IF = 30
    ELSE = 31
    BREAK = 32
    RETURN = 33
    CONTINUE = 34
    WHILE = 35
    FOR = 36
    TERMINAL = 37
    NUMBER = 38
    FLOAT = 39
    ID = 40
    CHAR = 41
    CHAR_ESC = 42
    PLUS = 43
    MINUS = 44
    MUL = 45
    DIV = 46
    MOD = 47
    GT = 48
    LT = 49
    EQ = 50
    GE = 51
    LE = 52
    NE = 53
    AND = 54
    OR = 55
    NOT = 56
    LSHIFT = 57
    RSHIFT = 58
    BITAND = 59
    BITOR = 60
    BITXOR = 61
    BITNOT = 62
    PRINTFREPLACER = 63
    WS = 64
    SINGLE_LINE_COMMENT = 65
    MULTI_LINE_COMMENT = 66

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'('", "')'", "','", "'{'", "'}'", "'printf'", "'='", "':'", 
            "'typedef'", "'++'", "'--'", "'int'", "'float'", "'char'", "'void'", 
            "'const'", "'+='", "'-='", "'*='", "'/='", "'%='", "'<<='", 
            "'>>='", "'&='", "'^='", "'|='", "'switch'", "'case'", "'default'", 
            "'if'", "'else'", "'break'", "'return'", "'continue'", "'while'", 
            "'for'", "';'", "'+'", "'-'", "'*'", "'/'", "'%'", "'>'", "'<'", 
            "'=='", "'>='", "'<='", "'!='", "'&&'", "'||'", "'!'", "'<<'", 
            "'>>'", "'&'", "'|'", "'^'", "'~'" ]

    symbolicNames = [ "<INVALID>",
            "SWITCH", "CASE", "DEFAULT", "IF", "ELSE", "BREAK", "RETURN", 
            "CONTINUE", "WHILE", "FOR", "TERMINAL", "NUMBER", "FLOAT", "ID", 
            "CHAR", "CHAR_ESC", "PLUS", "MINUS", "MUL", "DIV", "MOD", "GT", 
            "LT", "EQ", "GE", "LE", "NE", "AND", "OR", "NOT", "LSHIFT", 
            "RSHIFT", "BITAND", "BITOR", "BITXOR", "BITNOT", "PRINTFREPLACER", 
            "WS", "SINGLE_LINE_COMMENT", "MULTI_LINE_COMMENT" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "T__11", "T__12", "T__13", 
                  "T__14", "T__15", "T__16", "T__17", "T__18", "T__19", 
                  "T__20", "T__21", "T__22", "T__23", "T__24", "T__25", 
                  "SWITCH", "CASE", "DEFAULT", "IF", "ELSE", "BREAK", "RETURN", 
                  "CONTINUE", "WHILE", "FOR", "TERMINAL", "NUMBER", "FLOAT", 
                  "ID", "CHAR", "CHAR_ESC", "PLUS", "MINUS", "MUL", "DIV", 
                  "MOD", "GT", "LT", "EQ", "GE", "LE", "NE", "AND", "OR", 
                  "NOT", "LSHIFT", "RSHIFT", "BITAND", "BITOR", "BITXOR", 
                  "BITNOT", "PRINTFREPLACER", "WS", "SINGLE_LINE_COMMENT", 
                  "MULTI_LINE_COMMENT" ]

    grammarFileName = "Grammar.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


