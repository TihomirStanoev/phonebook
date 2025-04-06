# 📞Simple Phonebook Application

This is a basic command-line phonebook application written in Python. It allows you to store, view, edit, and delete contacts. The contact data is stored in a `phonebook.json` file.

## ✨ Features

* **Add New Contact:** Allows you to enter the first name, last name, and phone number of a new contact, which is then saved to the phonebook.
* **Show All Contacts:** Displays a list of all contacts currently stored in the phonebook, formatted with first name, last name, and phone number.
* **Edit Phone Number:** Enables you to update the phone number of an existing contact by entering their first and last name and the new phone number.
* **Delete Contact:** Lets you remove a contact from the phonebook by entering their first name, last name, and phone number.
* **Data Storage:** Contacts are stored in a `phonebook.json` file using the JSON format for easy readability and data persistence.
* **Unique ID Generation:** Each new contact is automatically assigned a unique numerical ID, which is tracked in the `ids.txt` file.

## ▶️ How to Use

1.  **Save the code:** Save the provided Python code as a `.py` file (e.g., `main.py`).
2.  **Run the script:** Open your terminal or command prompt, navigate to the directory where you saved the file, and run the script using the command:
    ```bash
    python main.py
    ```
3.  **Follow the menu:** The application will display a menu with the following options:
    ```
    Phonebook
    1. Show all contacts
    2. Add new contact
    3. Edit phone
    4. Delete contact
    0. Exit
    ```
4.  **Enter your choice:** Type the number corresponding to the action you want to perform and press Enter.
5.  **Provide input:** The application will prompt you for the necessary information (first name, last name, phone number) based on your chosen action.
6.  **Exit:** To close the application, enter `0`.

## 📂 File Structure

* `main.py`: The main Python script containing the phonebook application logic.
* `ids.txt`: A text file that stores the last generated unique ID for contacts. This helps in assigning unique IDs to new entries.
* `phonebook.json`: A JSON file where the contact data (names and phone numbers) is stored. This file will be created automatically when you add your first contact or if it doesn't exist.

## 📌 Notes

* The application identifies contacts for editing and deletion based on their first name, last name, and (for deletion) phone number. Ensure you provide the correct information to avoid unintended modifications or deletions.
* This is a simple implementation for learning purposes. More features and error handling could be added to enhance its functionality.
