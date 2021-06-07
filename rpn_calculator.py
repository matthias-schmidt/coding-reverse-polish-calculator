# Write your code here.
# Feel free to use as many scripts as you want/need to improve the readability.


def calculator():

    """
    Function prompting the user to input numbers or operation signs and interpreting this as a calculation in Reverse Polish Notation (RPN) on request.
    Args: None
    Returns: None
    Operations: + - * / ** sqrt int // %.
    Action keys: c clear, s status, enter evaluate, q quit
    """


    def evaluate(S):

        stack = []
        for x in S:
            if x not in opns: 
                stack.append(x)
            else:
                try:
                    if x == '+': stack.append(stack.pop() + stack.pop())
                    elif x == '-': stack.append(- stack.pop() + stack.pop())
                    elif x == '*': stack.append(stack.pop() * stack.pop())
                    elif x == '/': stack.append(1 / stack.pop() * stack.pop())
                    elif x == '**': 
                        x2, x1 = stack.pop(), stack.pop()
                        stack.append(x1**x2)
                    elif x == 'sqrt': stack[-1] **= 1/2
                    elif x == 'int': stack[-1] = int(stack[-1])
                    elif x == '//': 
                        x2, x1 = stack.pop(), stack.pop()
                        stack.append(x1 // x2)
                    elif x == '%':
                        x2, x1 = stack.pop(), stack.pop()
                        stack.append(x1 % x2)
                except: 
                    print('Invalid input')
                    return S

        return stack

    print('Enter a number or an operation (+ - * / ** sqrt int // %)')
    print('c/s/enter for clearing/printing/evaluating stack')
    print('q for quitting')

    stack = []
    opns = {'+', '-', '*', '/', '**', 'sqrt', 'int', '//', '%'}
    eingabe = input('Input: ')

    while eingabe != 'q':
        if eingabe == 'c': stack.clear()
        elif eingabe == 's': print(stack)
        elif eingabe == '': 
            stack = evaluate(stack)
            print(stack)
        else:
            if eingabe in opns: stack.append(eingabe)
            else:
                try:
                    stack.append(float(eingabe))
                except:
                    print('Invalid input')
                    pass

        eingabe = input('Input: ')

    print('Bye!')