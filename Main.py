from AddEmployee import AddEmployee

class Main:
    while True:
        try:
            choice = int(input("Welcome to Employee Management. Here you can add employees or view existing.\n"
                           "Press 1 to add new employee.\nPress 2 to view employees.\nPress 3 to exit.\n"))
            if choice == 1:
                empNr = input("\nPlease enter employee-number: ")
                name = input("\nPlease enter name of the employee: ")
                profession = input("\nPlease enter job title: ")

                AddEmployee.addNewEmployee(empNr, name, profession)
                break

            elif choice == 2:
                # Add call to getEmployees
                break

            elif choice == 3:
                break
        except:
            print("Exceptiion")
