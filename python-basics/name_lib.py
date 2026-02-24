first_names = ["Joao", "Liam", "Garcia", "Alicia", "Yuji"]
last_names = ["Pedro", "Miller", "Mendoza", "Sander", "Ito"]

def get_full_name(first, last):
    return f"{first} {last}"

def get_full_names(first, last):
    full_names_list = []
    for first in first_names:
        for last in last_names:
            full_names_list.append(get_full_names(first, last))
    return full_names_list

