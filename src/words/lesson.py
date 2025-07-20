from db import session
from models import Word
from .card_logic import flash_card
from .config import STATUSES
from .exit_cleanly import exit_cleanly

# TODO add ability to reverse input (in case of acidental y/n)
def practice_lesson(language):
    from .memory_game import choose_lesson
    lesson = choose_lesson()
    next_pass = []

    if language == '日本語':
        words = session.query(Word).order_by(Word.j_to_e_revision_status_id).filter(
            Word.lesson == lesson
        ).all()
    else:
        words = session.query(Word).order_by(Word.e_to_j_revision_status_id).filter(
            Word.lesson == lesson
        ).all()

    for word in words:
        result = flash_card(word, language)
        if result is None:
            exit_cleanly(words)
            return
        if not result:
            next_pass.append(word)

    while next_pass:
        word = next_pass.pop(0)
        result = flash_card(word, language)
        if result is None:
            exit_cleanly(words)
            return
        if not result:
            next_pass.append(word)
    exit_cleanly(words)
