from ArrayStack import AraayStack
from EvalPostfix import evalPostfix

def precdence (op):
    if (op == '(' or op == ')'):
        return 0
    elif (op == '+' or op == '-'):
        return 1
    elif (op == '*' or op == '/'):
        return 2
    else:
        return -1
    

# 중위 표기 수식의 후위식 변환
def Infix2Postfix(expr):
    s = AraayStack(100)
    output = []
    
    for term in expr :
        if term == '(':
            s.push(term)
            
        elif term == ')':
            while not s.isEmpty():
                op = s.pop()
                if op == '(':
                    break
                else:
                    output.append(op)
                    
        elif term in "+-*/":
            while not s.isEmpty():
                op = s.peek()
                if (precdence(term) <= precdence(op)):
                    output.append(op)
                    s.pop()
                else:
                    break
            s.push(term)
        else:
            output.append(term)
    while not s.isEmpty():
        output.append(s.pop())
    return output



if __name__ == "__main__" :
    print('중위표기식 후위표기 변환₩n')
    
    infix1 = ['8', '/', '2', '-', '3', '+', '(', '3', '*', '2', ')']
    infix2 = ['1', '/', '2', '*', '4', '*', '(', '1', '/', '4', ')']
    
    postfix1 = Infix2Postfix(infix1)
    postfix2 = Infix2Postfix(infix2)
    
    result1 = evalPostfix(postfix1)
    result2 = evalPostfix(postfix2)
    
    print('  중위표기: ', infix1)
    print('  후위표기: ', postfix1)
    print('  계산결과: ', result1,)