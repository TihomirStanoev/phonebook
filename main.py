import json
from os import path

ids = 'ids.txt'
phonebook_json = 'phonebook.json'



def id_generator() -> int:
    current_id = 0

    if path.exists(ids):
        with open(ids, 'r') as file:
            last_id = file.read()
        current_id = int(last_id) + 1
        with open(ids, 'w') as file:
            file.write(str(current_id))
    else:
        with open(ids, 'w') as file:
            file.write(str(current_id))

    return int(current_id)

def read_phonebook_json() -> list|bool:
    if path.exists(phonebook_json):
        with open(phonebook_json, 'r') as phonebook_file:
            phonebook = json.load(phonebook_file)
            return phonebook
    return False


def write_phonebook_json(new_phonebook: list) -> None:
    if path.exists(phonebook_json):
        with open(phonebook_json, 'w') as json_phones:
            json.dump(new_phonebook, json_phones)



def add_contact(first_name:str, last_name:str, phone:str) -> None:
    new_contact_id = id_generator()
    contacts = [{'id': new_contact_id, 'name': first_name, 'last_name': last_name, 'contact': phone}]

    current_phones = read_phonebook_json()

    if current_phones:
        contacts.extend(current_phones)

    with open(phonebook_json, 'w') as phones:
        json.dump(contacts, phones)

    print(f'{first_name} {last_name} - {phone} is saved!')



def contact_proccesing(firstname:str , lastname:str , phone:str, deliting:bool) -> None:
    phonebook = read_phonebook_json()
    contact_exist = False

    if phonebook:
        for contact in phonebook:
            if contact['name'] == firstname and contact['last_name'] == lastname and deliting == False:
                contact['contact'] = phone
                print(f'Contact: {firstname} {lastname}, new number {phone}!')
                contact_exist = True
                break
            elif contact['name'] == firstname and contact['last_name'] == lastname and contact['contact'] == phone and deliting == True:
                contact_exist = True
                phonebook.remove(contact)
                print(f'Contact: {firstname} {lastname} is deleted!')
                contact_exist = True
                break
    if contact_exist:
        write_phonebook_json(phonebook)

    else:
        print('No contacts')


def print_phonebooks() -> None:
    phonebook = read_phonebook_json()

    if phonebook:
        for contact in phonebook:
            print(f'{contact['name']:<10}', end=' ')
            print(f'{contact['last_name']:<10}', end=' ')
            print(f'{contact['contact']:<10}')
    else:
        print('No contacts')



# def delete_name(ft_name: str, lt_name: str) -> None:
#     phonebook = read_phonebook_json()
#     contact_exist = False

#     if phonebook:
#         for contact in phonebook:
#             if contact['name'] == ft_name and contact['last_name'] == lt_name:
#                 contact_exist = True
#                 phonebook.remove(contact)
#                 print(f'Contact: {ft_name} {lt_name} is deleted!')
#                 break
#     if contact_exist:
#         write_phonebook_json(phonebook)
#     else:
#         print('No contacts')


# def edit_name(edit_name:str , edit_last:str , new_phone:str ) -> None:
#     phonebook = read_phonebook_json()
#     contact_exist = False

#     if phonebook:
#         for contact in phonebook:
#             if contact['name'] == edit_name and contact['last_name'] == edit_last:
#                 contact['contact'] = new_phone
#                 contact_exist = True
#                 break
#     if contact_exist:
#         write_phonebook_json(phonebook)

#     else:
#         print('No contacts')



def main_menu():
    print('1. Show all contacts')
    print('2. Add new contact')
    print('3. Edit phone')
    print('4. Delete contact')
    print('0. Exit')


def main():

    print("Phonebook")
    while True:
        main_menu()

        choose = input('Make your choose: ')

        if choose == '1':
            print_phonebooks()

        elif choose == '2':
            fname = input('Enter first name: ').strip().capitalize()
            lname = input('Enter last name: ').strip().capitalize()
            phone = input('Enter phone number: ').strip()
            add_contact(fname, lname, phone)

        elif choose == '3':
            fname = input('Enter first name: ').strip().capitalize()
            lname = input('Enter last name: ').strip().capitalize()
            phone = input('Enter a new phone number: ').strip()
            deliting = False
            contact_proccesing(fname, lname, phone, deliting)

        elif choose == '4':
            fname = input('Enter first name: ').strip().capitalize()
            lname = input('Enter last name: ').strip().capitalize()
            phone = input('Enter phone number: ').strip()
            deliting = True
            contact_proccesing(fname, lname, phone, deliting)

        else:
            print('Goodbye!')
            break

if __name__ == '__main__':
    main()