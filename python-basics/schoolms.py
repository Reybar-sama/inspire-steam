# Name : Rey Bar
# Date : 23/02/2026
# Program to record and display student details in Python & Excel


def main_menu():
    print("\n****** STUDENT SCHOOL MEMBERSHIP SYSTEM ******")
    print("1. Register New Student")
    print("2. Display existing students and student data")
    print("3. Exit")
    

def new_student():
    while True:
        print("\n-- New Student Info --")
        print = input(f"Enter Student ID: ")
        print = input(f"Enter Student Name: ")
        print = input(f"Enter Current Course: ")
        print = int(input(f"Enter Student Phone: "))

        choice = input("Enter option: ").strip().lower()

    if choice == "B":
        import name_lib

        print(f"Students: {len(name_lib.first_names)}")

        full_name = name_lib.get_full_name("Davis", "McClean")
        print(f"Full names: {full_name}")

        all_names = name_library.get_all_full_names()
        print(f"All students: {len(all_names)}")

    elif choice == "C":
        print("Exiting program...")
        quit()
