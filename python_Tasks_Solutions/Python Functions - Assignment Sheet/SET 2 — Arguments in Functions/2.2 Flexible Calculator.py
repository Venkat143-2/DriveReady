# Flexible Calculator ⭐
# calculator(a, b, op="+") supporting + - * /.
# calculator(10, 5)         ->  15
# calculator(10, 5, "-")    ->  5
# calculator(10, 5, "*")    ->  50
# calculator(10, 0, "/")    ->  Error: cannot divide by zero
# calculator(10, 5, "%")    ->  Error: unknown operator '%'
def calculator(a,b,operator):
    match operator:
        case '+':
            print(a+b)
        case '-':
            print(a-b)
        case '/':
            if b==0:
                print('''Error : can't divide by zero''')
            else:
                print(a/b)
        case '*':
            print(a*b)
        case _:
            print('Error : invalid operator')
a,b=map(int,input('Enter 2 Numbers : ').split(' '))
op=input('Enter the Operator to perform operation on Operands : ')
calculator(a,b,op)
