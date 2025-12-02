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


def get_note_input(prompt):
    """Get validated note input from the user (non-empty)."""
    while True:
        note = input(prompt).strip()
        if note:
            return note
        print("Note cannot be empty!")


def get_confirmation(prompt):
    """Prompt user for yes/no confirmation."""
    while True:
        response = input(prompt + " (yes/no): ").strip().lower()
        if response in {'yes','no'}:
            return response
        print("Please type 'yes' or 'no'.")


def write_note(note):
    """Overwrite notes and save with timestamp."""
    timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M]")
    try:
        with FILENAME.open('w', encoding='utf-8') as f:
            f.write(f"{timestamp} {note}\n")
        save_backup()
        print("Note written and saved. Mmmm yummy notes!")
    except Exception as e:
        print(f"Error writing note: {e}")


def append_note(note):
    """Append a new note with timestamp."""
    timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M]")
    try:
        with FILENAME.open('a', encoding='utf-8') as f:
            f.write(f"{timestamp} {note}\n")
        save_backup()
        print("Appended note successfully. Delicious!")
    except Exception as e:
        print(f"Error appending note: {e}")


def read_notes():
    """Read notes from file."""
    if not FILENAME.exists():
        print("You haven't fed me any notes yet.")
        return
    print("\n--- Your Notes ---")
    try:
        with FILENAME.open('r', encoding='utf-8') as f:
            for line in f:
                print(line.strip())
    except Exception as e:
        print(f"Error reading notes: {e}")


def delete_all_notes():
    """Delete main notes and all backups with confirmation."""
    confirm = get_confirmation("Are you sure you want to remove all notes?")
    if confirm != 'yes':
        print("Deletion cancelled.")
        return

    deleted_any = False
    # Delete main notes
    if FILENAME.exists():
        try:
            FILENAME.unlink()
            deleted_any = True
            print(f"Deleted: {FILENAME}")
        except Exception as e:
            print(f"Could not delete {FILENAME}: {e}")