import json
import os

# checks wheteher the specified file exists.
my_file = "contacts.json"

# list of contacts
contacts = []

# write contacts to json file
def save_to_file():
    json_object = json.dumps(contacts, indent=4)
    print(json_object)
    with open("contacts.json", "w") as contact_file:
        contact_file.write(json_object)


# read json file
def load_file():
    global contacts
    file_exist = os.path.exists(my_file)
    # checks wheteher the specified path exists.
    if file_exist:
        with open("contacts.json", "r") as contact_file:
            contacts = json.load(contact_file)
        print(contacts)


# Display the menu for the user
def display_menu():
    print("*" * 20)
    print("a- Add") # Done
    print("e- Edit") # Done
    print("s- Search") # Done
    print("p- Print All") # Done
    print("d- Delete") # Done
    print("x- Exit") # Done
    print("*" * 20)


# Add name to the contact list
def add_contact():
    contact_dict = {}
    contact_name = input("Contact name:\n")
    contact_dict["Name"] = contact_name
    contact_age = input("Contact age:\n")
    contact_dict["Age"] = contact_age
    contact_gender = input("Contact gender:\n")
    contact_dict["Gender"] = contact_gender
    contacts.append(contact_dict)
    print("Contact added")


# Displays the contacts to the user
def print_all():
    number_of_contact = len(contacts)
    print("\n" * 5)
    print(f"Number of contacts: {number_of_contact}")
    for contact in contacts:
        print("-" * 15)
        for key, value in contact.items():
            print(f"{key}: {value}")
    print("-" * 15)
    print("\n" * 5)





# dislpays the search options
def search_menu():
    print("How would like to search:")
    print("n- search by name")
    print("a- search by age")
    print("g- search by gender")


# search by the contact's name
def name_search():
    contact_count = 0
    name_search = input("Enter the name you want to search:\n")
    for contact in contacts:
        if name_search == contact["Name"]:
            print(contact)
            contact_count += 1
    if contact_count == 0:
        print(f"Couldn't find contact by the name {name_search}")


# search by the contact's gender
def age_search():
    contact_count = 0
    age_search = input("Enter the age you want to search:\n")
    for contact in contacts:
        if age_search == contact["Age"]:
            print(contact)
            contact_count += 1
    if contact_count == 0:
        print(f"Couldn't find contact by the age {age_search}")


# search by the contact's gender
def gender_search():
    contact_count = 0
    gender_search = input("Enter the gender you want to search:\n")
    for contact in contacts:
        if gender_search == contact["Gender"]:
            print(contact)
            contact_count += 1
    if contact_count == 0:
        print(f"Couldn't find contact by the gender {gender_search}")


# Serach if the contact exists in the contact file
def search():
    user_input = input("")
    if user_input == "n":
        choice = "n"
    elif user_input == "a":
        choice = "a"
    elif user_input == "g":
        choice = "g"

    if choice == "n":
        name_search()
    if choice == "a":
        age_search()
    if choice == "g":
        gender_search()

# displays the delete options
def delete_menu():
    print("How would like to delete:")
    print("n- delete by name")
    print("a- delete by age") 
    print("g- delete by gender")


# delete by the contact's name
def name_delete():
    contact_count = 0
    name_delete = input("Enter the name you want to delete:\n")
    for contact in contacts[::-1]:
        if name_delete == contact["Name"]:
            contacts.remove(contact)
            print(f"The contact by the name {name_delete} has been deleted successfully")
            contact_count += 1
    if contact_count == 0:
        print(f"Couldn't find contact by the name {name_delete}")


# delete by the contact's gender
def age_delete():
    contact_count = 0
    age_delete = input("Enter the age you want to delete:\n")
    for contact in contacts[::-1]:
        if age_delete == contact["Age"]:
            contacts.remove(contact)
            print(f"The contact by the age {age_delete} has been deleted successfully")
            contact_count += 1
    if contact_count == 0:
        print(f"Couldn't find contact by the age {age_delete}")

# delete by the contact's gender
def gender_delete():
    contact_count = 0
    gender_delete = input("Enter the gender you want to delete:\n")
    for contact in contacts[::-1]:
        if gender_delete == contact["Gender"]:
            contacts.remove(contact)
            print(f"The contact by the gender {gender_delete} has been deleted successfully")
            contact_count += 1
    if contact_count == 0:
        print(f"Couldn't find contact by the gender {gender_delete}")


# Delete contact from contact file
def delete():
    user_input = input("")
    if user_input == "n":
        choice = "n"
    elif user_input == "a":
        choice = "a"
    elif user_input == "g":
        choice = "g"

    if choice == "n":
        name_delete()
    if choice == "a":
        age_delete()
    if choice == "g":
        gender_delete()

# displays the edit options
def edit_menu():
    print("What would like to edit:")
    print("n- edit the name")
    print("a- edit the age")
    print("g- edit the gender")




# Checks if the contact exists before displaying the menu and editing.
def edit_validation():
    name_list = []
    for contact in contacts:
        name_list.append(contact["Name"])
    name_to_edit = input("Enter the name of the contact you want to edit:\n")
    if name_to_edit in name_list:
        return name_to_edit
    return False



# Edit the contact's name
def edit_name(name_to_edit):
    new_name = input("Enter your edit:\n")
    for contact in contacts:
        if name_to_edit == contact["Name"]:
            contact["Name"] = new_name
            print("Name Changed successfully")


# Edit the contact's age
def edit_age(name_to_edit):
    new_age = input("Enter your edit:\n")
    for contact in contacts:
        if name_to_edit == contact["Name"]:
            contact["Age"] = new_age
            print("Age changed successfully")



# Edit the contact's gender
def edit_gender(name_to_edit):
    new_gender = input("Enter your edit:\n")
    for contact in contacts:
        if name_to_edit == contact["Name"]:
            contact["Gender"] = new_gender
            print("Gender changed successfully")



# edit a contact name from the contact file
def edit():
    name = edit_validation()
    print(name)
    edit_menu()
    user_input = input("")
    if user_input == "n":
        choice = "n"
    elif user_input == "a":
        choice = "a"
    elif user_input == "g":
        choice = "g"

    if choice == "n":
        edit_name(name)
    if choice == "a":
        edit_age(name)
    if choice == "g":
        edit_gender(name)


def main():
    user_input = ''
    load_file()
    while user_input != "x":
        if user_input == 'a':
            add_contact()
        elif user_input == 'p':
            print_all()
        elif user_input == 's':
            search_menu()
            search()
        elif user_input == 'd':
            delete_menu()
            delete()
        elif user_input == 'e':
            if edit_validation:
                edit()
            else:
                print("Couldn't find the contact")
        display_menu()
        user_input = input("What to do?\n")

    save_to_file()

  
if __name__ == "__main__":
    main()

