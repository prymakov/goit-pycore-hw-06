from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    def __init__(self, name):
        super().__init__(name)
        

class Phone(Field):
    def __init__(self, number):
        super().__init__(number)


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {', '.join(p.value for p in self.phones)}"
        
    def add_phone(self, number):        
        if len(number) != 10:
            print(f"wrong format number {number}")
        else:
            self.phones.append(Phone(number))

    def find_phone(self, number):
        for p in self.phones:
            if p.value == number:
                return p
        return None

    def remove_phone(self, number):
        if self.find_phone(number) != None:
            self.phones.remove(self.find_phone(number))
        else:
            print(f"Phone {number} for contact {self.name} not found")
                       
    def edit_phone(self, old_number, new_number):
        for i, p in enumerate(self.phones):
            if p.value == old_number:
                self.phones[i] = Phone(new_number)
                return
        print(f"Phone number {old_number} not found.")

class AddressBook(UserDict):

    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name, None)

    def delete(self, name):
        if name in self.data:
            del self.data[name]
        else:
            print(f"Contact {name} not found.")

def main():
    book = AddressBook()

# Створення нової адресної книги
    book = AddressBook()

    # Створення запису для John
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")
    john_record.add_phone("1")

    # Додавання запису John до адресної книги
    book.add_record(john_record)

    # Створення та додавання нового запису для Jane
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    # Виведення всіх записів у книзі
    for name, record in book.data.items():
        print(record)

    # Знаходження та редагування телефону для John
    john = book.find("John")
    john.edit_phone("1234567890", "1112223333")

    print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

    # Пошук конкретного телефону у записі John
    found_phone = john.find_phone("5555555555")
    print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

    # Видалення запису Jane
    book.delete("Jane")

if __name__ == "__main__":
    main()