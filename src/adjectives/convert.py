import pandas as pd
from random import randint

from adjectives.present_form import present_form
from adjectives.past_form import past_form
from adjectives.negative_form import negative_form
from adjectives.past_negative_form import past_negative_form
from adjectives.て_form import て_form

ADJS = pd.read_excel('adjectives/adjs.xlsx')

# TODO: create an adjective object (maybe do after creating a db).

FORMS = [
    present_form,
    past_form,
    negative_form,
    past_negative_form,
    て_form
]

def select_conversion():
    print('Convert from which form?')
    print('1) present')
    print('2) past')
    print('3) negative')
    print('4) past_negative')
    print('5) て')

    from_form = input()
    try:
        from_form = int(from_form)
    except:
        raise ValueError(f'Please a number from 1-{len(FORMS)}.')
    if from_form < 1 or from_form > len(FORMS):
        raise ValueError(f'Please a number from 1-{len(FORMS)}.')

    print('Convert to which form?')
    print('1) present')
    print('2) past')
    print('3) negative')
    print('4) past_negative')
    print('5) て')

    to_form = input()
    try:
        to_form = int(to_form)
    except:
        raise ValueError(f'Please a number from 1-{len(FORMS)}.')
    if to_form < 1 or to_form > len(FORMS):
        raise ValueError(f'Please a number from 1-{len(FORMS)}.')
    
    return {'from': FORMS[from_form - 1], 'to': FORMS[to_form - 1]}

def conversion_game():

    conversion = select_conversion()

    random_index = randint(0, len(ADJS)-1)
    adj = ADJS.iloc[random_index,:]
    print(f"{conversion['from'](adj)['kanji']}/{conversion['from'](adj)['kana']}")
    user_input = input()

    break_flag = False
    while user_input not in ('x','X','ｘ','Ｘ'):
        
        while not conversion['to'](adj).isin([user_input]).any():
            print(conversion['to'](adj))
            print('X')
            user_input = input()
            if user_input in ('x','X','ｘ','Ｘ'):
                break_flag = True
                break
        if break_flag:
            break
        print('O')
        random_index = randint(0, len(ADJS)-1)
        adj = ADJS.iloc[random_index,:]
        print(f"{conversion['from'](adj)['kanji']}/{conversion['from'](adj)['kana']}")
        user_input = input()
