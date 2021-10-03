# calculator-compiler
Codes related to the activities of the Compilers discipline at São Paulo State Univeristy.

# Note
when the grammar (MyGrammer.g4) rules are changed, you need to generate the grammar files from the command: 
java -jar antlr-4.9.2-complete.jar -Dlanguage=Python3 MyGrammer.g4 -visitor -o dist

# An virtual enviroment (not added in this repository) with the ANTLR4 runtime is needed: 
pip install antlr4-python3-runtime

# Command to run the code: 
python main.py code.txt
