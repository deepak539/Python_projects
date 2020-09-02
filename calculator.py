    # This program is to solve an expression

import math

# Cheking the precedence of an operator

def check_precedence(ind):
    dict_ = {'-':0,'+':0,'*':1,'/':1,'^':2}
    return dict_[ind]

""" Checking if the scanned character
    is operator or not"""

def is_operator(val):
    operators = ['+','-','/','*','^']
    if val in operators:
        return True
    return False

# Converting infix expression to postfix

def convert_in_to_post(arr):
    final = []
    stack = []
    result = []
    count = 0
    for i in arr:
        temp = []
        if i == '(':
            stack.append(i)                    # Pushing value to stack
        elif i == ')':
            for j in stack:
                if j == '(':
                    break
                else:
                    final.append(stack.pop())                    # Popping out value from stack and appending into final
        elif is_operator(i):
            if len(stack) == 0:
                stack.append(i)
            else:
                while check_precedence(i) <= check_precedence(stack[-1]):   # Checking precedence of operators
                    final.append(stack.pop())
                    if len(stack) == 0:
                        break    
                stack.append(i)
        else:
            final.append(int(i))
    while(len(stack) != 0):
        final.append(stack.pop())
                    
    return final

# This will evaluate postfix expression

def postfix_evaluate(stack_2):
    result = 0
    lst2 = []
    for items in stack_2:
        if is_operator(items):
            a = lst2.pop()
            b = lst2.pop()
            if items == '+':
                lst2.append(a+b)
            elif items == '-':
                lst2.append(b-a)
            elif items == '*':
                lst2.append(a*b)
            elif items == '/':
                lst2.append(b/a)
            elif items == '^':
                lst.append(math.pow(a,b))
            else:
                print("Invalid operator:-",items)
        else:
            lst2.append(items)
    return lst2
                
                

if __name__ == "__main__":
    str_= input()
    lst = []
    temp = 0
    for i in range(len(str_)-1):
        if is_operator(str_[i]) == False:
            var = int(str_[i])
            if is_operator(str_[i+1]) == True:
                lst.append(temp * 10 + var)
                temp = 0
            else:
                temp = temp * 10 + var
        else:
            lst.append(str_[i])
    if temp != 0:
        lst.append(temp * 10 + int(str_[-1]))
    else:
        lst.append(int(str_[-1]))
    postfix = convert_in_to_post(lst)
    ans = postfix_evaluate(postfix)
    print(ans[0])
