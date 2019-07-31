import module

print("\t\t\t\t ______________________________________")
print("\t\t\t\t|                                      |") 
print("\t\t\t\t| Welcome to Student Management System |")
print("\t\t\t\t|______________________________________|")

while True:
    module.menu()
    try:
        choice = int(input("Enter your choice : "))
        if choice>5 or choice<1:
            raise Exception("Invalid Choice")
    except Exception as e:
        print(e)
    else:
        if choice == 5:
            break
        else:
            module.choices(choice)

