import itertools
import sys

def insert(original, new, pos):
  '''Inserts new inside original at pos.'''
  return original[:pos] + new + original[pos:]

def permutate(myList, mySize):
    return list(itertools.product(myList, repeat=mySize))

myBrackets = []
def Brackets(output, open, close, pairs):
    if open == pairs & close == pairs:
        myBrackets.append(output)
        return output
    else:
        if open < pairs:
            Brackets(output + "(", open+1, close, pairs)
        if close < open:
            Brackets(output + ")", open, close+1, pairs)
            
def brackets(n):
    for i in range(n+1):
        Brackets("", 0, 0, i)

numbers = ['4','2','9','4']
#numbers = ['1','2','3','4']
#numbers = [1, 1, 3, 4]
#numbers = ['1', '1', '3', '4']
symbols = ['+', '-', '*', '/']
leadingSymbols = permutate(['','-'], len(numbers))

brackets(len(numbers))

#for bracketLine in myBrackets:
 #   print bracketLine
    
# Change strings to floating point
for n in range(len(numbers)):
    numbers[n] = str(float(numbers[n]) + 0.0)

# permeating the symbol list only lennumbers - 1 because spaces in between
symbolsPermList = permutate(symbols, len(numbers)-1)

for leadingSymSet in leadingSymbols:
    for exprSymbols in symbolsPermList:

        # creating the expression

        # leading symbol can either be + or -
        expression = leadingSymSet[0] + numbers[0]

        # creating the rest of the expression
        for index in range(len(exprSymbols)):
            expression = expression + exprSymbols[index] + leadingSymSet[index] + numbers[index+1]

        #print expression
        """
        # adding brackets
        for bracketLine in myBrackets:
            index = 0
            
            for n in range(len(bracketLine)):
                #if n < len(bracketLine):
                #    if bracketLine[n] = ')'
                #expression = insert(expression, bracketChar, index)
                index += 1;
                
        #"""
        expression = expression.replace('+-','-')
        expression = expression.replace('-+','-')
        expression = expression.replace('--','+')
        
        # evaluation the expression and testing if it equals to 10
        if eval(expression) == 10:
            expression = expression.replace('.0','')
            print expression + " = 10"
