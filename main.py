# from collections import UserDict
# import re

# class Field:
#     def __init__(self, value):
#         self.value = value

#     def __str__(self):
#         return str(self.value)

# class Name:
#     def __init__(self, first_name):
#         self.set_first_name(first_name)

#     def set_first_name(self, first_name):
#         if not first_name or not isinstance(first_name, str):
#             raise ValueError("First name is required and must be a non-empty string")
#         self.first_name = first_name

# class Phone:
#     def __init__(self, number):
#         self.validate_phone_number(number)
#         self.number = number

#     def validate_phone_number(self, number):
#         if not self.is_valid_number(number):
#             raise ValueError("Invalid phone number")

#     def is_valid_number(self, number):
#         if re.match(r'^\d{10}$', number) is None:
#             return None
#         else:
#             return number
        
#     def get_phone_number(self):
#         return self.number

# # class Record:
# #     def __init__(self, name):
# #         self.name = Name(name)
# #         self.phones = []

# #     def edit_phone(self, old_phone, new_phone):
# #         old_phone_found = False
    
# #         for i, phone_obj in enumerate(self.phones):
# #             if phone_obj.value == old_phone:
# #                 old_phone_found = True
# #                 self.phones[i] = Phone(new_phone)
# #                 break
            
# #         if not old_phone_found:
# #             raise ValueError("Phone number does not exist")

# class Record:
#     def __init__(self, name, phones=None):
#         self.set_name(name)
#         self.phones = phones or []

#     def set_name(self, name):
#         if not isinstance(name, Name):
#             raise ValueError("Name must be an instance of the Name class")
#         self._name = name

#     def add_phone(self, phone):
#         if not isinstance(phone, Phone):
#             raise ValueError("Phone must be an instance of the Phone class")
#         self.phones.append(phone)

#     def remove_phone(self, phone_number):
#         for phone in self.phones:
#             if phone.get_phone_number() == phone_number:
#                 self.phones.remove(phone)
#                 return f"Phone number {phone_number} removed successfully"
#         return f"Phone number {phone_number} not found"

#     def edit_phone(self, old_phone_number, new_phone_number):
#         for phone in self.phones:
#             if phone.get_phone_number() == old_phone_number:
#                 phone.validate_phone_number(new_phone_number)
#                 phone.number = new_phone_number
#                 return f"Phone number {old_phone_number} edited successfully"
#         return f"Phone number {old_phone_number} not found"

#     def find_phone(self, phone_number):
#         for phone in self.phones:
#             if phone.get_phone_number() == phone_number:
#                 return f"Phone number {phone_number} found"
#         return f"Phone number {phone_number} not found"

#     def __str__(self):
#         return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

# class AddressBook(UserDict):
#     def add_record(self, data):

from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, first_name):
        self.set_first_name(first_name)

    def set_first_name(self, first_name):
        if not isinstance(first_name, str) or not first_name.strip():
            raise ValueError("First name is required and must be a non-empty string")
        self.value = first_name.strip()

class Phone(Field):
    def __init__(self, number):
        self.set_phone_number(number)

    def set_phone_number(self, number):
        if not (number.isdigit() and len(number) == 10):
            raise ValueError("Invalid phone number")
        self.value = number

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        try:
            phone_obj = Phone(phone)
            self.phones.append(phone_obj)
            return f"Phone number {phone} added successfully"
        except ValueError as e:
            return f"Error: {e}"

    def remove_phone(self, phone):
        for phone_obj in self.phones:
            if phone_obj.value == phone:
                self.phones.remove(phone_obj)
                return f"Phone number {phone} removed successfully"
        return f"Phone number {phone} not found"

    def edit_phone(self, old_phone, new_phone):
        for phone_obj in self.phones:
            if phone_obj.value == old_phone:
                phone_obj.set_phone_number(new_phone)
                return f"Phone number {old_phone} edited successfully"
        raise ValueError(f"Phone number {old_phone} not found")

    def find_phone(self, phone):
        for phone_obj in self.phones:
            if phone_obj.value == phone:
                return phone_obj
        return None

    def get_phones(self):
        return [str(phone.value) for phone in self.phones]

    def __str__(self):
        phones_str = "; ".join(self.get_phones())
        return f"Contact name: {self.name}, phones: {phones_str}"

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        if name in self.data:
            del self.data[name]
            return f"Record {name} deleted successfully"
        return f"Record {name} not found"


    



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