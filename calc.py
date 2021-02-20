def calc():         # haha calculator go brrr
    print("Welcome to calculator!")
    first = float(input("First Number: "))
    second = float(input("Second Number: "))
    oper = input("Enter an operator (sum, diff, prod, quo, exp, mod) ")
    if(oper == "sum"):
        answer = first + second
        print(answer)
    if(oper == "diff"):
        answer = first - second
        print(answer)
    if(oper == "prod"):
        answer = first * second
        print(answer)
    if(oper == "quo"):
        answer = first / second
        print(answer)
    if(oper == "exp"):
        answer = first ** second
        print(answer)
    if(oper == "mod"):
        answer = first % second
        print(answer)
