from models import Plant, Employee, is_valid_email

while True:
    print("1. Add Plant\n2. Gel all plants\n3. Add Employee\n4. Get all employees")
    try:
        flag = int(input("Choose menu item: "))
    except ValueError:
        print("Please enter a valid integer: ")
        continue

    if flag == 1:
        name = input("Plant name: ")
        address = input("Plant address: ")
        plant = Plant(name, address)
        plant.save()
    elif flag == 2:
        Plant.get_all()
    elif flag == 3:
        name = input("Employee name: ")
        email = input("Employee email: ")
        while not is_valid_email(email):
            print("Email is not correct, please, try again:")
            email = input("Email: ")
        plant_id = int(input("Plant id: "))
        employee = Employee(name, email, plant_id)
        employee.save()
    elif flag == 4:
        Employee.get_all()
    else:
        print("Invalid input")
