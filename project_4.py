# Simple Calculator

'''
Operator Assigning
1) Addition - 1
2) Subtraction - 2
3) Multiplication - 3
4) Division - 4
5) For exit - 5
'''
# Defining functions of the operations

def add(x, y):
    return x + y
# we can use same variable in all the definition
def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    if y == 0:
        return "Error! Can't divide by ZERO"
    return x / y

while True:
    print("\nSelect your choice of operator")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. EXIT")

    choice = input("Enter your choice 1/2/3/4/5 : ")

    if choice == '5':
        print("You Have Exited The Calculator")
        break    # exit fron the loop 

    if choice in ('1', '2', '3', '4'):

        try:
            n1 = float(input("Enter First Number : "))
            n2 = float(input("Enter Second Number : "))

        except ValueError:
            print("Invalid Input! Enter a number.")
            continue     
            # breaks the current execution and continue from the start(or loop)

        if choice == '1':
            print("Result :", add(n1, n2))    # n1, n2 ki value direct x and y me jake store ho jayegi

        elif choice == '2':
            print("Result : ", sub(n1, n2))

        elif choice == '3':
            print("Result : ", mul(n1, n2))

        elif choice == '4':
            print("Result : ", div(n1, n2))

    else:
        print("Invalid Number Operator, Try Again")
