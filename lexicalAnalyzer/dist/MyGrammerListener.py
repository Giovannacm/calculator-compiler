# Generated from MyGrammer.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MyGrammerParser import MyGrammerParser
else:
    from MyGrammerParser import MyGrammerParser

# This class defines a complete listener for a parse tree produced by MyGrammerParser.
class MyGrammerListener(ParseTreeListener):

    # Enter a parse tree produced by MyGrammerParser#expr.
    def enterExpr(self, ctx:MyGrammerParser.ExprContext):
        pass

    # Exit a parse tree produced by MyGrammerParser#expr.
    def exitExpr(self, ctx:MyGrammerParser.ExprContext):
        pass


    # Enter a parse tree produced by MyGrammerParser#number.
    def enterNumber(self, ctx:MyGrammerParser.NumberContext):
        pass

    # Exit a parse tree produced by MyGrammerParser#number.
    def exitNumber(self, ctx:MyGrammerParser.NumberContext):
        pass



del MyGrammerParser