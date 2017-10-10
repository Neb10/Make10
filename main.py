import abc
import itertools

# Generate permuations using built in library
def permutate(myList, mySize):
    return list(itertools.product(myList, repeat=mySize))

# Generate bracket structure using binary tree at n-1 levels
def gendistinct(n):
    # Place holder for numbers
    leafnode = 'None'
    
    dp = []
    newset = set()
    newset.add(leafnode)
    dp.append(newset)
    for i in range(1,n):
        newset = set()
        for j in range(i):
            for leftchild in dp[j]:
                for rightchild in dp[i-j-1]:
                    newset.add('(' + leftchild + '?' + rightchild + ')')
        dp.append(newset)
    return dp[-1]

# Nest loops to replace
def findSolution(terms, operatorList, leadingSymbol, bracketList, solution):
    for bracketExp in bracketList:
        for operatorSet in operatorList:
            operatorExp = bracketExp
            for operator in operatorSet:
                operatorExp = operatorExp.replace('?', operator, 1)

            for leadingSymSet in leadingSymbol:
                leadingSymExp = operatorExp
                for n in range(len(terms)):
                    myNumber = leadingSymSet[n] + str(terms[n]+0.0)
                    leadingSymExp = leadingSymExp.replace('None', myNumber, 1)
                
                myExpression = leadingSymExp
                
                try:
                    if eval(myExpression) == solution + 0.0:
                        return myExpression
                except:
                    next
    return None
                
# Evaluting dual operators and pretty print
def cleanExpression (expression):
    expression = expression.replace('+-','-')
    expression = expression.replace('-+','-')
    expression = expression.replace('--','+')
    expression = expression.replace('**','^')
    expression = expression.replace('.0','')
    return expression


#basic operators
extendedOperators = False
operatorList = ['+', '-', '*', '/']
if extendedOperators == True:
    operatorList.append('**')
    operatorList.append('%')

# user input
numbers = []
while len(numbers) < 1 || :
    if len(numbers) < 1:
        userInput = input('Enter a number: ')
    else:
        userInput = input('Enter another number (finish to move on): ')
    if userInput = 
    numbers.append(digit)
    
#numbers = [1,1,1]
solution = input('Desired Solution: ')

operatorPermList = permutate(operatorList, len(numbers)-1)
leadingSym = permutate(['','-'], len(numbers))
bracketList = gendistinct(len(numbers))
mySln = findSolution(numbers, operatorPermList, leadingSym, bracketList, solution)

if mySln == None:
    print repr(numbers) + ": No solution equaling to " + repr(solution)
else:
    print repr(numbers) + ": " + cleanExpression(mySln) + " = " + repr(solution)
