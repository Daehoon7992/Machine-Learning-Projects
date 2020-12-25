#Date: 07/21/2019, 11:59PM EST
########################################
#                                      
# Name: Daehoon Gwak
########################################

class Node:
    def __init__(self, value):
        self.value = value  
        self.next = None 
    
    def __str__(self):
        return "Node({})".format(self.value) 

    __repr__ = __str__
                          

# ----    Copy your Stack code from LAB9 here ---------
class Stack:
    def __init__(self):
        # You can add a count variable in the constructor
        self.top = None
        self.count = 0
    
    def __str__(self):
        temp=self.top
        out=[]
        while temp:
            out.append(str(temp.value))
            temp=temp.next
        out='\n'.join(out)
        return ('Top:{}\nStack:\n{}'.format(self.top,out))

    __repr__=__str__
    
    def isEmpty(self):
        #write your code here
        return self.top == None

    def __len__(self):
        #write your code here
        return self.count

    def peek(self):
        #write your code here
        if self.isEmpty():
            return None
        return self.top.value

    def push(self,value):
        #write your code here
        newNode = Node(value)
        if self.isEmpty():
            self.top = newNode
            newNode.next = None

        else:
            newNode.next = self.top
            self.top = newNode

        self.count += 1

    def pop(self):
        #write your code here
        if self.isEmpty():
            return 'Stack is empty'

        else:
            self.count -= 1
            temp = self.top
            self.top = self.top.next
            temp.next = None
            return temp.value
# ----    Stack code ends here here ---------

def prec(operator): #function that checks the priority of operator
    if operator == '^':
        return 3
    
    elif operator == '*':
        return 2
    
    elif operator == '/':
        return 2
    
    elif operator == '+':
        return 1
    
    elif operator == '-':
        return 1

    else: #in this case, parentheses.
        return -1

def postfix(expr):
    '''
    Required: postfix must create and use a Stack for expression processing
    >>> postfix(' 2 ^        4')
    '2.0 4.0 ^'
    >>> postfix('2')
    '2.0'
    >>> postfix('    2 *       5.34        +       3      ^ 2    + 1+4   ')
    '2.0 5.34 * 3.0 2.0 ^ + 1.0 + 4.0 +'
    >>> postfix(' 2.1 *      5   +   3    ^ 2+ 1  +     4')
    '2.1 5.0 * 3.0 2.0 ^ + 1.0 + 4.0 +'
    >>> postfix('(2.5)')
    '2.5'
    >>> postfix ('((2))')
    '2.0'
    >>> postfix ('     2 *  ((  5   +   3)    ^ 2+(1  +4))    ')
    '2.0 5.0 3.0 + 2.0 ^ 1.0 4.0 + + *'
    >>> postfix ('  (   2 *  ((  5   +   3)    ^ 2+(1  +4)))    ')
    '2.0 5.0 3.0 + 2.0 ^ 1.0 4.0 + + *'
    >>> postfix ('  ((   2 *  ((  5   +   3)    ^ 2+(1  +4))))    ')
    '2.0 5.0 3.0 + 2.0 ^ 1.0 4.0 + + *'
    >>> postfix('   2 *  (  5   +   3)    ^ 2+(1  +4)    ')
    '2.0 5.0 3.0 + 2.0 ^ * 1.0 4.0 + +'
    >>> postfix('2 *    5   +   3    ^ -2       +1  +4') #consecutive operators
    'error message'
    >>> postfix('2    5') #no operators
    'error message'
    >>> postfix('25 +') #not enough number
    'error message'
    >>> postfix('   2 *  (  5   +   3)    ^ 2+(1  +4    ') #unncessary open parenthesis
    'error message'
    >>> postfix('   2 *  (  5   +   3)    ^ 2+)1  +4(    ') #unncessary close parenthesis
    'error message'
    >>> postfix('3+(3-1)3') #consecutive ) and number
    'error message'
    >>> postfix('3 $ 3') #unexpected expression
    'error message'
    >>> postfix('3+(*3)') #consecutive ( and operator
    'error message'
    >>> postfix('3+()') #consecutive parenthesis
    'error message'
    >>> postfix('3+(3+)') #consecutive operator and )
    'error message'
    '''
    if (len(expr)<=0) or (not isinstance(expr,str)): # error if expr is empty or not a string
        print("expr error: postfix")        
        return "error"

    # Your code starts here
    stk = Stack()
    postfix_list = []

    # replace all operators to make space so that we can tokenize each expression
    new = expr.replace('+',' + ').replace('-',' - ').replace('*',' * ').replace('/',' / ').replace('^',' ^ ').replace('(',' ( ').replace(')',' ) ')
    txt = new.split()
    for a in range(len(txt)):
        if txt[a].replace('.', '').isdigit(): # check if the index is integer or float
            if (a != 0) and (txt[a-1].replace('.', '').isdigit()):
                return 'error: no operator between consecutive operands' # error if there is no operator between operands; ex. 3   4 

            if not stk.isEmpty() and txt[a-1] == ')': # error if there are close parenthesis and number consecutively; ex. 3+(3-1)3
                return 'error: consecutive ) and number'

            postfix_list.append(float(txt[a]))


        elif txt[a] not in '+-*/^()': # error if unexpected charactor found
            return 'error: unexpected charactor'


        elif txt[-1] in '+-*/^': # error if there is no operand right after operator; ex. 24 +
            return 'error: not enough number'


        elif txt[0] in '+-*/^': # error if there is no operand right before operator; ex. + 24
            return 'error: not enough number'

      
        elif (stk.isEmpty() and txt[a] != ')') or (txt[a] == '('): # if stack is empty or if we meet open parenthesis, push to the stack
            if (a != 0) and (txt[a] == '(') and (txt[a-1].replace('.', '').isdigit()): # error for invalid multiplication expression; ex.3(4)
                return 'error: invalid expression. You can`t use multiplication with this form'
            stk.push(txt[a])


        elif (txt[a] in '+-*/^')  and (txt[a-1] in '+-*/^'): # extra credit # error if there are two consecutive operators
            return 'error: consecutive operators'


        else: # if the index is operator except (, then go this else statement
            top = stk.peek()
            if (not stk.isEmpty()) and (prec(txt[a]) > prec(top)): # check the precedence and push
                if txt[a-1] == '(' and txt[a] in '+-*/^': # error if there are open parenthesis and operator consecutively; ex. 3+(*3)
                    return 'error: consecutive ( and operator'
                stk.push(txt[a])


            else: # check the precedence and append to the list
                x = False
                while (not stk.isEmpty()) and (prec(txt[a]) <= prec(top)):
                    if txt[a-1] == '(' and txt[a] == ')': # error if there are open parenthesis and close parenthesis in together; ex. ()
                        return 'error: ()'

                    if txt[a-1] in '+-*/^' and txt[a] == ')': # error if there are operator and close parenthesis consecutively; ex. 3+(3+)
                        return 'error: consecutive operator and )'

                    if (stk.peek() == '^') and (txt[a] == '^'): # check if there are multiple exponential expression and stack them consecutively; ex. 2^2^3
                        break

                    stk.pop()
                    x = True
                    if top == '(': # we have to remove the open parenthesis so if the top stack is (, then get out of the loop
                        break
                    postfix_list.append(top) # otherwise, we append the operators
                    
                    if not stk.isEmpty():
                        top = stk.peek()

                    if stk.isEmpty() and  txt[a] == ')': # error if there is unnecessay error; ex. 2+3+4)
                        return 'error: unnecessary )'                  

                if txt[a] != ')': # we never push close parenthesis into the stack
                    stk.push(txt[a])

                elif x == False and stk.isEmpty() and  txt[a] == ')': # error if there is more than expected ); ex (3+2))
                    print('hello')
                    return 'error: unnecessary )'

    while len(stk) > 0: # at the end of the expression, if there is no more operands and operators are in stack, we append the rest in the list
        if stk.peek() == '(': # error message if there is unnecessary '('
            return 'error: unnecessary ('
        postfix_list.append(stk.pop())

    return " ".join(map(str, postfix_list))


def calculator(expr):
    '''
    Required: calculator must call postfix
              calculator must create and use a Stack to compute the final result as shown in the video lecture
    >>> calculator('    4  +      3 -2')
    5.0
    >>> calculator('  4  + 3.65 - 2 / 2')
    6.65
    >>> calculator(' 23 / 12 - 223 +      5.25 * 4    *      3423')
    71661.91666666667
    >>> calculator('   2   - 3         *4')
    -10.0
    >>> calculator(' 3 *   (        ( (10 - 2*3)))')
    12.0
    >>> calculator(' 8 / 4  * (3 - 2.45      * (  4- 2 ^   3)) + 3')
    28.6
    >>> calculator(' 2   *  ( 4 + 2 *   (5-3^2)+1)+4')
    -2.0
    >>> calculator('2.5 + 3 * ( 2 +(3) *(5^2 - 2*3^(2) ) *(4) ) * ( 2 /8 + 2*( 3 - 1/ 3) ) - 2/ 3^2')
    1442.7777777777778
    >>> calculator("4++ 3 +2") #consecutive operators
    'error message'
    >>> calculator("4    3 +2") #no operators
    'error message'
    >>> calculator('(2)*10 - 3*(2 - 3*2)) ') #unncessary close parenthesis
    'error message'
    >>> calculator('(2)*10 - 3*/(2 - 3*2) ') #consecutive operators
    'error message'
    >>> calculator(')2(*10 - 3*(2 - 3*2) ') #unncessary close parenthesis
    'error message'
    '''
    if len(expr)<=0 or not isinstance(expr,str): 
        print("expr error: calculator")
        return "error"

    # Your code starts here
    operand = Stack() # stack all operands

    value = postfix(expr) # call postfix function to prepare to calculate

    if 'error' in value: # error message if the expression contains error so that we can`t calculate them
        return value

    for x in value.split(): # tokenizing values
        if x.replace('.', '').isdigit(): # push to stack if the value is operand
            operand.push(x)

        else:
            if x == '^': # exponential. we swap a and b, otherwise we get the wrong value; ex, 2^3 = 8 not 9
                a = float(operand.pop())
                b = float(operand.pop())
                answer = b ** a
                operand.push(answer)

            elif x == '*': # multiplication
                a = float(operand.pop())
                b = float(operand.pop())
                answer = b * a
                operand.push(answer)

            elif x == '/': # division. we swap a and b, otherwise we get the wrong value; ex, 4/2 = 2 not 1/2
                a = float(operand.pop())
                b = float(operand.pop())
                answer = b / a
                operand.push(answer)

            elif x == '+': # plus
                a = float(operand.pop())
                b = float(operand.pop())
                answer = a + b
                operand.push(answer)

            elif x == '-': # minus. we swap a and b, otherwise we get the wrong value; ex, 4-2 = 2 not -2
                a = float(operand.pop())
                b = float(operand.pop())
                answer = b - a
                operand.push(answer)

    final = operand.pop() # pop out the final value in the stack

    return final


    
