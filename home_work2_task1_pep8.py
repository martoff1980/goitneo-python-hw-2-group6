def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)

        except KeyError:
            return f"User with current name not founded."

        except IndexError:
            return f"User not selected."

        except TypeError:
            return f"User not found."

        except ValueError:
            return "Give me name and phone please."

    return inner


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = int(phone)
    return "Contact added."


def select_contact(args, contacts):
    name = args[0]
    # user_consist is type None mean that
    # name is absent in contacts
    user_consist = type(contacts[name])
    phone = int(contacts.get(name))
    return f"Contact: {phone}."


def change_contact(args, contacts):
    name, phone = args
    # user_consist is type None mean that
    # name is absent in contacts
    user_consist = type(contacts[name])
    contacts[name] = int(phone)
    return "Contact changed."


def all_contacts(contacts):
    return contacts


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            print(add_contact(args, contacts))

        elif command == "all":
            print(all_contacts(contacts))

        elif command == "change":
            print(change_contact(args, contacts))

        elif command == "phone":
            print(select_contact(args, contacts))

        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
