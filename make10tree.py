import abc
import itertools

def permutate(myList, mySize):
    return list(itertools.product(myList, repeat=mySize))

class Expression:
    """All types of expressions"""
    left = None
    right = None
    operator = None
    
    def __init__(self, expr1, expr2, symbol):
        """Initialise the expression"""
        self.left = expr1
        self.right = expr2
        self.operator = symbol
        
    def compute(self):
        """Computes the value of the expression"""
        leftRes = self.computeLeft()
        rightRes = self.computeRight()

        if self.operator is '+':
            return leftRes + rightRes
        elif self.operator is '-':
            return leftRes - rightRes
        elif self.operator is '*':
            return leftRes * rightRes
        elif self.operator is '/':
            return (leftRes + 0.0) / (rightRes + 0.0)

    def computeLeft(self):
        """Compute the left side of the expression tree"""
        if isinstance(self.left, Expression):
            return self.left.compute()
        else:
            return self.left
        
    def computeRight(self):
        """Compute the right side of the expression tree"""
        if isinstance(self.right, Expression):
            return self.right.compute()
        else:
            return self.right

    def __str__(self):
        """Returns a string representation of the expression"""
        output = "("
        
        if isinstance(self.left, Expression):
            output += self.left.__str__()
        else:
            output += str(self.left)
            
        output += self.operator
        
        if isinstance(self.right, Expression):
            output += self.right.__str__()
        else:
            output += str(self.right)
        
        return output + ')'
    
class PlusExp(Expression):
    """Adding two numbers"""
    def __init__(self, expr1, expr2):
        Expression.__init__(self, expr1, expr2, '+')

class MinusExp(Expression):
    """Subtracting two numbers"""
    def __init__(self, expr1, expr2):
        Expression.__init__(self, expr1, expr2, '-')

class StarExp(Expression):
    """Multiplying two numbers"""
    def __init__(self, expr1, expr2):
        Expression.__init__(self, expr1, expr2, '*')

class SlashExp(Expression):
    """Dividing two numbers"""
    def __init__(self, expr1, expr2):
        Expression.__init__(self, expr1, expr2, '/')

#p1 = MinusExp(PlusExp(-4, StarExp(2, 9)), 4)
#print p1.__str__() + ' = ' + str(p1.compute()).replace('.0','')

seqList = permutate([0,1],2)
numbers = [4, 2, 9, 4]
numbers = [1, 1, 3, 3]
operatorList = ['+', '-', '*', '/', '%', '**']
operatorPermList = permutate(operatorList, len(numbers)-1)
leadingSymbols = permutate(['','-'], len(numbers))
bracketExpList = []

def gendistinct(n):
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

alltrees = gendistinct(4)
#for tree in alltrees:
    #print tree

for seq in seqList:
    n0 = Expression(None,None,'?')
    current = n0
    for n in seq:
        newNode = Expression(None, None, '?')
        if n == 0:
            current.left = newNode
            current = current.left
        elif n == 1:
            current.right = newNode
            current = current.right
    bracketExpList.append(n0.__str__())

bracketExpList.append('((None?None)?(None?None))')

for bracketExp in alltrees:
    for operatorSet in operatorPermList:
        operatorExp = bracketExp
        for operator in operatorSet:
            operatorExp = operatorExp.replace('?', operator, 1)

        for leadingSymSet in leadingSymbols:
            leadingSymExp = operatorExp
            for n in range(len(numbers)):
                myNumber = leadingSymSet[n] + str(numbers[n]+0.0)
                leadingSymExp = leadingSymExp.replace('None', myNumber, 1)
            
            myExpression = leadingSymExp
            if '((1.0**1.0)+(3.0*3.0))' in myExpression:
                print myExpression 
            
            try:
                if eval(myExpression) == 10.0:
                    myExpression = myExpression.replace('+-','-')
                    myExpression = myExpression.replace('-+','-')
                    myExpression = myExpression.replace('--','+')
                    myExpression = myExpression.replace('**','^')
                    myExpression = myExpression.replace('.0','')
                    print myExpression + " = 10"
            except:
                None
