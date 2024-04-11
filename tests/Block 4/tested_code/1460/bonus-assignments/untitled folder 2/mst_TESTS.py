

from my_saint_tysm import change, check, check_first_n_characters, is_full_line_comment, Things_to_check

NAME = "Albert Zhao"
MAX_CHARACTERS =   100
CHARS_PER_TAB = 4
FILE_NAME = "werewolves.py"


copy = Things_to_check.copy()
copy['has_starting_comment'] = False
change(FILE_NAME, copy)