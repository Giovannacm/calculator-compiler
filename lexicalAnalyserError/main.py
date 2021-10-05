import sys
from antlr4 import *
from dist.MyGrammerLexer import MyGrammerLexer
from dist.MyGrammerParser import MyGrammerParser
from dist.MyGrammerVisitor import MyGrammerVisitor
from CustomErrorListener import CustomErrorListener

#ATTENTION: when the grammar rules are changed, you need to generate the grammar files from the command: 
#  java -jar antlr-4.9.2-complete.jar -Dlanguage=Python3 MyGrammer.g4 -visitor -o dist

#Command to run this code (with the virtual enviroment activated):
#  python main.py code.txt

if __name__ == "__main__":
    data = FileStream(sys.argv[1])
    print(data)

    cel = CustomErrorListener()

    lexer = MyGrammerLexer(data)
    lexer.removeErrorListeners()
    lexer.addErrorListener(cel)

    tokens = lexer.getAllTokens()

    for token in tokens:
        print(token.text, '->', MyGrammerLexer.ruleNames[token.type - 1])


#Developed by Giovanna Marinho and Guilherme Molina