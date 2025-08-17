from db import session
from models import Word
from .card_logic import flash_card
from .exit_cleanly import exit_cleanly
from .deck_functions import status_check, deck_size
from random import shuffle

# TODO add ability to reverse input (in case of acidental y/n)
def practice_lesson(language, all=False):
    from .memory_game import choose_lesson
    lesson, all = choose_lesson()
    
    if language == '日本語':
        query = session.query(Word).order_by(Word.j_to_e_revision_status_id)
    else:
        query = session.query(Word).order_by(Word.e_to_j_revision_status_id)

    if all:
        words = query.filter(Word.lesson == lesson).all()
    else:
        if language == '日本語':
            words = query.filter(Word.lesson == lesson, Word.j_to_e_revision_status_id is not None).all()
        else:
            words = query.filter(Word.lesson == lesson, Word.e_to_j_revision_status_id is not None).all()
    
    deck = []
    for word in words:
        deck.append({'word':word,'status':'in'})
    
    status_check(deck, language)

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
