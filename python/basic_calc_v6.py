
# Main menu function
def main_menu():
    print("### MAIN MENU ###")
    print("[1], Addition")
    print("[2], Substraction")
    print("[3], Multiplication")
    print("[4], Division")
    print("[5], Average")
    print("[6], All operations")

# Inputs

n1 = float(input("Enter first number: "))
n2 = float(input("Enter second number: "))
main_menu()
opt = int(input("Enter any option: "))
    
match opt:
    case 1:
        add = n1 + n2
        print(f"Addition is:  {add}")
    case 2:
        subs = n1 - n2
        print(f"Substraction is:  {subs}")
    case 3:
        mult = n1 * n2
        print(f"Multiplication is:  {mult}")
    case 4:
        div = n1 / n2
        print(f"Division is:  {div}")
    case 5:
        avg = (n1 + n2) /2
        print(f"Average is:  {avg}")
    case 6:
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
    case _:
        print(":::Invalid option:::")