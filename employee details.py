
employees = []

def add_employee():
    print("Enter employee details:")
    name = input("Name: ")
    designation = input("Designation: ")
    account_number = input("Account Number: ")
    date_of_joining = input("Date of Joining (YYYY-MM-DD): ")
    basic_pay = float(input("Basic Pay: "))
    da = float(input("Dearness Allowance (DA): "))
    hra = float(input("House Rent Allowance (HRA): "))
    ca = float(input("Conveyance Allowance (CA): "))

    gross_salary = basic_pay + da + hra + ca

    employee = {
        "Name": name,
        "Designation": designation,
        "Account Number": account_number,
        "Date of Joining": date_of_joining,
        "Basic Pay": basic_pay,
        "DA": da,
        "HRA": hra,
        "CA": ca,
        "Gross Salary": gross_salary
    }

    employees.append(employee)
    print("Employee added successfully!")

def display_employee(employee):
    print("\nEmployee Details:")
    for key, value in employee.items():
        print(f"{key}: {value}")
while True:
    print("\nOptions:")
    print("1. Add Employee")
    print("2. View Employee Details")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_employee()
    elif choice == "2":
        if len(employees) == 0:
            print("No employees in the system.")
        else:
            account_number = input("Enter employee's account number: ")
            found = False
            for employee in employees:
                if employee["Account Number"] == account_number:
                    display_employee(employee)
                    found = True
                    break
            if not found:
                print("Employee not found.")
    elif choice == "3":
        break
    else:
        print("Invalid choice. Please try again.")
