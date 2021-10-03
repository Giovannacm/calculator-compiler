import sys
from antlr4 import *
from dist.MyGrammerLexer import MyGrammerLexer
from dist.MyGrammerParser import MyGrammerParser
from dist.MyGrammerVisitor import MyGrammerVisitor

#ATTENTION: when the grammar rules are changed, you need to generate the grammar files from the command: 
#  java -jar antlr-4.9.2-complete.jar -Dlanguage=Python3 MyGrammer.g4 -visitor -o dist

if __name__ == "__main__":
    data = FileStream(sys.argv[1])
    print(data)

    lexer = MyGrammerLexer(data)

    tokens = lexer.getAllTokens()

    for token in tokens:
        print(token.text, '->', MyGrammerLexer.ruleNames[token.type - 1])