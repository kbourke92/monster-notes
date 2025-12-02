import os
from datetime import datetime
import shutil  # for terminal size


FILENAME = Path("notes.txt")
BACKUP_DIR = Path("backups")
BACKUP_DIR.mkdir(exist_ok=True)  # ensure backup directory exists

# ASCII Art
monster_ascii = r"""
     .-"      "-.
     /            \
    |,  .-.  .-.  ,|
    | )(_o/  \o_)( |
    |/     /\     \|
    (_     ^^     _)
     \__|IIIIII|__/
     | \IIIIII/ |
    \          /
     `--------`

   ~ Nom nom nom ~
     Pages scattered everywhere!
"""


# Main
def main():
    while True:
        show_menu()
        choice = get_menu_choice()

        if choice == '1':
            note = get_note_input("Feed monster here: ")
            write_note(note)

        elif choice == '2':
            note = get_note_input("Change diet here: ")
            append_note(note)

        elif choice == '3':
            read_notes()

        elif choice == '4':
            delete_all_notes()

        elif choice == '5':
            print("Goodbye!!")
            break


# Input Validation
def get_menu_choice():
    """Get validated menu choice from the user (1-5)."""
    while True:
        choice = input("Enter choice (1-5): ").strip()
        if choice in {'1','2','3','4','5'}:
            return choice
        print("Invalid! Enter a number from 1 to 5.")