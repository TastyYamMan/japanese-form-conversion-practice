from db import session
from models import Word
from .card_logic import flash_card
from .exit_cleanly import exit_cleanly
from .deck_functions import status_check, deck_size
import datetime
from random import shuffle

# TODO add ability to reverse input (in case of acidental y/n)
# TODO add timed revisions (i.e. haven't revised in a month) + times perfect answer so words that have been perfected 
# many times in a row get more months till they are revised
def revision(language):
    next_pass = []

    yesterday = datetime.datetime.now() - datetime.timedelta(days=1)
    if language == '日本語':
        words_nested = [
            session.query(Word).filter(
                Word.j_to_e_revision_status_id == i+1,
                Word.j_to_e_last_time_revised < yesterday
            ).limit(20).all()
            for i in range(3)
        ]
    else:
        words_nested = [
            session.query(Word).filter(
                Word.e_to_j_revision_status_id == i+1,
                Word.e_to_j_last_time_revised < yesterday
            ).limit(20).all()
            for i in range(3)
        ]
    
    words = [word for word_list in words_nested for word in word_list]

    if len(words) == 0:
        print('Nothing to revise!')
    
    status_check(deck, language)

    deck = []
    for word in words:
        deck.append({'word':word,'status':'in'})

    card_counter = 0
    i = 0
    while deck_size(deck) > 0:
        card = deck[i]
        if card['status'] == 'in':
            word = card['word']
            result = flash_card(word, language)
            if result is None:
                exit_cleanly(words)
                return
            if result:
                card['status'] = 'out'
            card_counter += 1
        i = (i + 1)%len(words)
        
        if card_counter % 10 == 0:
            status_check(deck, language)
    
    status_check(deck, language)
    exit_cleanly(words)