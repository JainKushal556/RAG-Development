op1 = float (input("Enter First Number :"))
op2 = float (input("Enter Second Number :"))
op = input("Enter Operator ( +, -, *, /, %, **): ")

if op == '+':
    print(op1+op2)
elif op == '-':
    print(op1-op2)
elif op == '*':
    print(op1*op2)
elif op == '%':
    print(op1%op2)
elif op == '/':
    print(op1/op2)
elif op == "**":
    print(op1**op2)
else:
    print("Please enter a valid operator! ")