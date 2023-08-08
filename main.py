from lab6 import is_balanced, convertToPostfix

def main():
    while True:
        exp = "".join(input("Enter an expression to be converted into postfix form, or type 'quit' to exit:\n").split())
        if exp == "quit":
            break
        else:
            if is_balanced(exp):
                print(convertToPostfix(exp))
            else:
                print("Expression is unbalanced, try again.")
          
main()
