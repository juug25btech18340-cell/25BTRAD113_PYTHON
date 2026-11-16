# ----------------------------------------------------------------------
# Experiment 8: Contact book using lists and dictionaries
# ----------------------------------------------------------------------
def experiment_8():
    contacts = {}

    def add_contact():
        name = input("Enter contact name: ").strip()
        if not name:
            print("Name cannot be empty!")
        elif name.lower() in (n.lower() for n in contacts):
            print("Contact already exists!")
        else:
            phone = input("Enter phone number: ").strip()
            email = input("Enter email address: ").strip()
            contacts[name] = {"Phone": phone, "Email": email}
            print("Contact added successfully!")

    def search_contact():
        name = input("Enter contact name to search: ").strip()
        for stored, d in contacts.items():
            if stored.lower() == name.lower():
                print(f"\nName: {stored}\nPhone: {d['Phone']}\nEmail: {d['Email']}")
                return
        print("Contact not found!")

    def display_contacts():
        print("\n----- CONTACT LIST -----")
        if not contacts:
            print("No contacts available.")
            return
        for name, d in contacts.items():
            print(f"Name: {name} | Phone: {d['Phone']} | Email: {d['Email']}")

    actions = {"1": add_contact, "2": search_contact, "3": display_contacts}
    while True:
        print("\n===== CONTACT BOOK =====")
        print("1. Add Contact  2. Search Contact  3. Display All  4. Exit")
        choice = input("Enter choice: ").strip()
        if choice == "4":
            break
        if choice in actions:
            actions[choice]()
        else:
            print("Invalid choice. Please enter 1-4.")


# ----------------------------------------------------------------------
# Experiment 9: Student grading system
# ----------------------------------------------------------------------
def calculate_grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    return "F"


def experiment_9():
    students = {}
    print("===== STUDENT GRADING SYSTEM =====")
    while True:
        print("\n1. Add Student Marks  2. Display Results  3. Exit")
        choice = input("Enter choice: ").strip()
        if choice == "1":
            name = input("Enter student name: ").strip()
            if not name:
                print("Name cannot be empty!")
                continue
            while True:
                marks = read_number("Enter marks (0-100): ")
                if 0 <= marks <= 100:
                    break
                print("Marks must be between 0 and 100.")
            grade = calculate_grade(marks)
            students[name] = {"Marks": marks, "Grade": grade}
            print(f"Student {name} added with Grade: {grade}")
        elif choice == "2":
            print("\n----- STUDENT GRADING RESULTS -----")
            if not students:
                print("No student records available.")
            for name, d in students.items():
                print(f"Name: {name} | Marks: {d['Marks']} | Grade: {d['Grade']}")
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please enter 1-3.")


# ----------------------------------------------------------------------
# Experiment 10: Word frequency counter
# ----------------------------------------------------------------------
def word_frequency_counter(text):
    clean_text = text.lower().translate(str.maketrans("", "", string.punctuation))
    frequency = {}
    for word in clean_text.split():
        frequency[word] = frequency.get(word, 0) + 1
    return frequency


def experiment_10():
    text = input("Enter a sentence: ").strip()
    if not text:
        text = "python data structures in python lab exercise"
        print("No input given, using sample:", text)
    print("----- WORD FREQUENCY RESULTS -----")
    for word, count in word_frequency_counter(text).items():
        print(f"'{word}': {count}")
