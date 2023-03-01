from utils.helpers import write_new_human, get_all_humans, check_email, edit_human, is_email_unique

while True:
    print("1. Add new person!\n2. Get all persons!)\n3. Edit information about human\n")
    flag = int(input("Choose what you want to do: "))

    if flag == 1:
        first_name = input("First Name: ")
        last_name = input("Last Name: ")
        email = input("Email: ")

        while not check_email(email):
            print("Email is not correct, please, try again:")
            email = input("Email: ")

        while not is_email_unique(email):
            print("Еhis email already exists in the database")
            email = input("Enter new email: ")

        human_dict = {'first_name': first_name, "last_name": last_name, "email": email}
        write_new_human(human_dict)

    elif flag == 2:
        humans = get_all_humans()
        for human in humans:
            print(human["first_name"])
            print(human["last_name"])
            print(human["email"])
            print("=========================================================")

    elif flag == 3:
        id = int(input("Enter id to edit: "))
        edit_human(id)

    else:
        print("Don't have this menu item")
        break