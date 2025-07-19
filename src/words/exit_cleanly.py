from db import session
from models import Word

def exit_cleanly(words):
    for word in words:
        word.incorrect_count = 0
    session.commit()