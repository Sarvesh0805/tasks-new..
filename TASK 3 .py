import secrets
import string

def Generating_Password(l):
    character = string.ascii_letters + string.digits + string.punctuation
    generate = ''.join(secrets.choice(character) for _ in range(l))
    return generate

def Main():
    try:
        print("<----PASSWORD GENERATOR---->")
        name = input("Enter Your Name: ")
        
        while True:
            l = int(input("Enter the Length of the Password or Enter 0 To Exit: "))
            
            if l == 0:
                print("<----EXITING PASSWORD GENERATOR---->")
                break
            
            if l <= 0:
                print("Length Should Be More Than 0.")
                continue
            
            generate = Generating_Password(l)
            print("Here's Your Generated Password: {}".format(generate))
            
            choice = input("Do You Want To Reset Your Password?: ")
            if choice.lower() != 'yes':
                print("<----EXITING PASSWORD GENERATOR---->")
                break
    
    except Exception as e:
        print("Error:", str(e))
        
    except ValueError:
        print("Entered Length Is Invalid.")

if __name__ == "__main__":
    Main()