# Generated from MyGrammer.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\13")
        buf.write(":\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3")
        buf.write("\5\3\6\3\6\3\7\3\7\3\b\6\b#\n\b\r\b\16\b$\3\t\6\t(\n\t")
        buf.write("\r\t\16\t)\3\t\3\t\6\t.\n\t\r\t\16\t/\5\t\62\n\t\3\n\6")
        buf.write("\n\65\n\n\r\n\16\n\66\3\n\3\n\2\2\13\3\3\5\4\7\5\t\6\13")
        buf.write("\7\r\b\17\t\21\n\23\13\3\2\3\5\2\13\f\17\17\"\"\2>\2\3")
        buf.write("\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2")
        buf.write("\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2")
        buf.write("\2\3\25\3\2\2\2\5\27\3\2\2\2\7\31\3\2\2\2\t\33\3\2\2\2")
        buf.write("\13\35\3\2\2\2\r\37\3\2\2\2\17\"\3\2\2\2\21\'\3\2\2\2")
        buf.write("\23\64\3\2\2\2\25\26\7,\2\2\26\4\3\2\2\2\27\30\7\61\2")
        buf.write("\2\30\6\3\2\2\2\31\32\7-\2\2\32\b\3\2\2\2\33\34\7/\2\2")
        buf.write("\34\n\3\2\2\2\35\36\7*\2\2\36\f\3\2\2\2\37 \7+\2\2 \16")
        buf.write("\3\2\2\2!#\4\62;\2\"!\3\2\2\2#$\3\2\2\2$\"\3\2\2\2$%\3")
        buf.write("\2\2\2%\20\3\2\2\2&(\4\62;\2\'&\3\2\2\2()\3\2\2\2)\'\3")
        buf.write("\2\2\2)*\3\2\2\2*\61\3\2\2\2+-\7\60\2\2,.\4\62;\2-,\3")
        buf.write("\2\2\2./\3\2\2\2/-\3\2\2\2/\60\3\2\2\2\60\62\3\2\2\2\61")
        buf.write("+\3\2\2\2\61\62\3\2\2\2\62\22\3\2\2\2\63\65\t\2\2\2\64")
        buf.write("\63\3\2\2\2\65\66\3\2\2\2\66\64\3\2\2\2\66\67\3\2\2\2")
        buf.write("\678\3\2\2\289\b\n\2\29\24\3\2\2\2\b\2$)/\61\66\3\b\2")
        buf.write("\2")
        return buf.getvalue()


class MyGrammerLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    OPMUL = 1
    OPDIV = 2
    OPSOMA = 3
    OPSUB = 4
    AP = 5
    FP = 6
    NUMBERINT = 7
    NUMBERREAL = 8
    WS = 9

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'*'", "'/'", "'+'", "'-'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>",
            "OPMUL", "OPDIV", "OPSOMA", "OPSUB", "AP", "FP", "NUMBERINT", 
            "NUMBERREAL", "WS" ]

    ruleNames = [ "OPMUL", "OPDIV", "OPSOMA", "OPSUB", "AP", "FP", "NUMBERINT", 
                  "NUMBERREAL", "WS" ]

    grammarFileName = "MyGrammer.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


