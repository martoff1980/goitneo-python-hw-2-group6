from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    # реалізація класу
    def __init__(self, value):
        super().__init__(value)


class Phone(Field):
    # реалізація класу
    def __init__(self, value):
        super().__init__(value)

        self.value = (
            str(value)
            .strip()
            .removeprefix("+")
            .replace("(", "")
            .replace(")", "")
            .replace("-", "")
            .replace(" ", "")
        )

        if len(self.value) != 0:
            self.value = "0000000000"


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    # реалізація класу
    def add_phone(self, phone):
        sanitize_phone_number = Phone(phone)
        self.phones.append(sanitize_phone_number)

    def remove_phone(self, phone):
        index = 0
        for item in self.phones:
            if item.value == phone:
                break
            index += 1
        return self.phones.pop(index)

    def edit_phone(self, old_value, new_value):
        for phone in self.phones:
            if phone == old_value:
                self.phones[self.phones.index(phone)] = new_value
                break

    def find_phone(self, phone):
        index = 0
        for item in self.phones:
            if item.value == phone:
                break
            index += 1
        return self.phones[index]

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):
    # реалізація класу
    def add_record(self, data):
        self.data.update({data.name: data.phones})

    def find(self, name):
        find_key = ""
        find_values = []
        for key, value in self.data.items():
            if str(key) == name:
                find_key = str(key)
                find_values = value
                break

        new_record = Record(find_key)
        for item in find_values:
            new_record.add_phone(item)
        return new_record

    def delete(self, name):
        for item in self.data.keys():
            if str(item) == name:
                self.data.pop(item)
                break


# Створення нової адресної книги
book = AddressBook()

# Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")
# Додавання запису John до адресної книги
book.add_record(john_record)

# Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")

# Додавання запису John до адресної книги
book.add_record(jane_record)

# Виведення всіх записів у книзі
for name, record in book.data.items():
    print(name.value, list(item.value for item in record))

# Знаходження та редагування телефону для John
john = book.find("John")
john.edit_phone("1234567890", "1112223333")

# Виведення: Contact name: John, phones: 1112223333; 5555555555
print(john)

# Пошук конкретного телефону у записі John
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

# Видалення запису Jane
book.delete("Jane")

# Виведення всіх записів у книзі
for name, record in book.data.items():
    print(name.value, list(item.value for item in record))
