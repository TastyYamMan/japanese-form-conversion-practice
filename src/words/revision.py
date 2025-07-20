from db import session
from models import Word
from .card_logic import flash_card
from .config import STATUSES
from .exit_cleanly import exit_cleanly
import datetime

# TODO add ability to reverse input (in case of acidental y/n)
# TODO add timed revisions (i.e. haven't revised in a month) + times perfect answer so words that have been perfected 
# many times in a row get more months till they are revised
def revision(language):
    next_pass = []

    if language == '日本語':
        words = [
            session.query(Word).filter(
                Word.j_to_e_revision_status_id == i+1,
                (Word.j_to_e_last_time_revised - datetime.datetime.now()).days > 1
            ).limit(20).all()
            for i in range(3)
        ]
    else:
        words = [
            session.query(Word).filter(
                Word.e_to_j_revision_status_id == i+1,
                (Word.e_to_j_last_time_revised - datetime.datetime.now()).days > 1
            ).limit(20).all()
            for i in range(3)
        ]
    if len(words) == 0:
        print('Nothing to revise!')
         
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
