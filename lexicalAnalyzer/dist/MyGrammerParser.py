# Generated from MyGrammer.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\13")
        buf.write("\34\4\2\t\2\4\3\t\3\3\2\3\2\3\2\3\2\3\2\3\2\5\2\r\n\2")
        buf.write("\3\2\3\2\3\2\3\2\3\2\3\2\7\2\25\n\2\f\2\16\2\30\13\2\3")
        buf.write("\3\3\3\3\3\2\3\2\4\2\4\2\5\3\2\3\4\3\2\5\6\3\2\t\n\2\34")
        buf.write("\2\f\3\2\2\2\4\31\3\2\2\2\6\7\b\2\1\2\7\r\5\4\3\2\b\t")
        buf.write("\7\7\2\2\t\n\5\2\2\2\n\13\7\b\2\2\13\r\3\2\2\2\f\6\3\2")
        buf.write("\2\2\f\b\3\2\2\2\r\26\3\2\2\2\16\17\f\6\2\2\17\20\t\2")
        buf.write("\2\2\20\25\5\2\2\7\21\22\f\5\2\2\22\23\t\3\2\2\23\25\5")
        buf.write("\2\2\6\24\16\3\2\2\2\24\21\3\2\2\2\25\30\3\2\2\2\26\24")
        buf.write("\3\2\2\2\26\27\3\2\2\2\27\3\3\2\2\2\30\26\3\2\2\2\31\32")
        buf.write("\t\4\2\2\32\5\3\2\2\2\5\f\24\26")
        return buf.getvalue()


class MyGrammerParser ( Parser ):

    grammarFileName = "MyGrammer.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'*'", "'/'", "'+'", "'-'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "OPMUL", "OPDIV", "OPSOMA", "OPSUB", 
                      "AP", "FP", "NUMBERINT", "NUMBERREAL", "WS" ]

    RULE_expr = 0
    RULE_number = 1

    ruleNames =  [ "expr", "number" ]

    EOF = Token.EOF
    OPMUL=1
    OPDIV=2
    OPSOMA=3
    OPSUB=4
    AP=5
    FP=6
    NUMBERINT=7
    NUMBERREAL=8
    WS=9

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.left = None # ExprContext
            self.atom = None # NumberContext
            self.op = None # Token
            self.right = None # ExprContext

        def number(self):
            return self.getTypedRuleContext(MyGrammerParser.NumberContext,0)


        def AP(self):
            return self.getToken(MyGrammerParser.AP, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyGrammerParser.ExprContext)
            else:
                return self.getTypedRuleContext(MyGrammerParser.ExprContext,i)


        def FP(self):
            return self.getToken(MyGrammerParser.FP, 0)

        def OPMUL(self):
            return self.getToken(MyGrammerParser.OPMUL, 0)

        def OPDIV(self):
            return self.getToken(MyGrammerParser.OPDIV, 0)

        def OPSOMA(self):
            return self.getToken(MyGrammerParser.OPSOMA, 0)

        def OPSUB(self):
            return self.getToken(MyGrammerParser.OPSUB, 0)

        def getRuleIndex(self):
            return MyGrammerParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MyGrammerParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 0
        self.enterRecursionRule(localctx, 0, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 10
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MyGrammerParser.NUMBERINT, MyGrammerParser.NUMBERREAL]:
                self.state = 5
                localctx.atom = self.number()
                pass
            elif token in [MyGrammerParser.AP]:
                self.state = 6
                self.match(MyGrammerParser.AP)
                self.state = 7
                self.expr(0)
                self.state = 8
                self.match(MyGrammerParser.FP)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 20
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 18
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                    if la_ == 1:
                        localctx = MyGrammerParser.ExprContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 12
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 13
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==MyGrammerParser.OPMUL or _la==MyGrammerParser.OPDIV):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 14
                        localctx.right = self.expr(5)
                        pass

                    elif la_ == 2:
                        localctx = MyGrammerParser.ExprContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 15
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 16
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==MyGrammerParser.OPSOMA or _la==MyGrammerParser.OPSUB):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 17
                        localctx.right = self.expr(4)
                        pass

             
                self.state = 22
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class NumberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBERINT(self):
            return self.getToken(MyGrammerParser.NUMBERINT, 0)

        def NUMBERREAL(self):
            return self.getToken(MyGrammerParser.NUMBERREAL, 0)

        def getRuleIndex(self):
            return MyGrammerParser.RULE_number

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumber" ):
                listener.enterNumber(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumber" ):
                listener.exitNumber(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumber" ):
                return visitor.visitNumber(self)
            else:
                return visitor.visitChildren(self)




    def number(self):

        localctx = MyGrammerParser.NumberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_number)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 23
            _la = self._input.LA(1)
            if not(_la==MyGrammerParser.NUMBERINT or _la==MyGrammerParser.NUMBERREAL):
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
        self._predicates[0] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 3)
         




