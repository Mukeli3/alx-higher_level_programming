if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    a = int a
    b = int b
    if argv != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    elif operator != '+' or '-' or '*' or '/':
        print('Unknown operator. Available operators: +, -, * and /')
        exit(1)
    else:
        print("{} + {} = {}".format(a, b, add(a, b)))
        print("{} - {} = {}".format(a, b, sub(a, b)))
        print("{} * {} = {}".format(a, b, mul(a, b)))
        print("{} / {} = {}".format(a, b, div(a, b)))
