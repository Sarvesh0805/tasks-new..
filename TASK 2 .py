import math

def addition(p, q):
    return p + q

def subtraction(p, q):
    return p - q

def multiply(p, q):
    return p * q

def divide(p, q):
    if q != 0:
        return p / q
    else:
        return "Please enter a valid denominator except zero."


def Main():
    print("<----ARTHIMETIC CALCULATOR---->")
    print("Available operations:")
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.Exit")
    
    while True:
        
        choice = input("Enter your choice: ")
        
        if choice == "5":
            print("<----EXITING THE CALCULATOR---->")
            break
        a,b = map(float,input("Enter two numbers : ").split())
    
        if choice == "1":
            output = addition(a,b)
            operator="+"
        elif choice == "2":
            output = subtraction(a,b)
            operator="-"
        elif choice == "3":
            output = multiply(a,b)
            operator="*"
        elif choice == "4":
            output = divide(a,b)
            operator="/"
        else:
            output = "Invalid choice"
            operator=" "
        
        if operator:
            print("Result of {:.2f} {} {:.2f} is: {:.2f}".format(a, operator, b, output))
    
if __name__ == "__main__":
    Main()