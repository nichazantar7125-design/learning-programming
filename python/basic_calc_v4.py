
# Main menu function
def main_menu():
    print("### MAIN MENU ###")
    print("[1], Addition")
    print("[2], Substraction")
    print("[3], Multiplication")
    print("[4], Division")
    print("[5], Average")
    print("[6]loat(in, All operations")

# Inputs
n1 = float(input("Enter first number: "))
n2 = float(input("Enter second number: "))
main_menu()
opt = int(input("Enter any option: "))

if (opt == 1):
    add = n1 + n2
    print(f"Addition is:  {add}")
else:
    if(opt == 2):
        subs = n1 - n2
        print(f"Substraction is:  {subs}")
    else:
        if(opt == 3):
            mult = n1 * n2
            print(f"Multiplication is:  {mult}")
        else:
            if(opt == 4):
                div = n1 / n2
                print(f"Division is:  {div}")
            else:
                if(opt == 5):
                    avg = (n1 + n2) /2
                    print(f"Average is:  {avg}")
                else:
                    if(opt == 6):
                        add = n1 + n2
                        subs = n1 - n2
                        mult = n1 * n2
                        div = n1 / n2
                        avg = (n1 + n2) /2
                        print(f"Addition is:  {add}")
                        print(f"Substraction is:  {subs}")
                        print(f"Multiplication is:  {mult}")
                        print(f"Division is:  {div}")
                        print(f"Average is:  {avg}")
                    else:
                        print(":::Invalid option:::")