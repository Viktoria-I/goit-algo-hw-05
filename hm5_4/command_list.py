from errors import input_error


@input_error
def add_contact(args, contacts):

    name, phone = args

    if name in contacts:
        return "Contact already exists."
    
    contacts[name] = phone
    return "Contact added."


@input_error
def change_contact(args, contacts):

    name, phone = args

    if name not in contacts:
        return "Contact not found." 
    
    contacts[name] = phone
    return "Contact updated."


@input_error
def show_phone(args, contacts):

    name = args[0]
    
    if name in contacts:
        return f"{name}: {contacts[name]}"
    else:
        return "Contact not found."
    

@input_error
def show_all(contacts):

    for name, phone in contacts.items():
        print("Your contacts:")
        print(f"{name}: {phone}")
        print()

