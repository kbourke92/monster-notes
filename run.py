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