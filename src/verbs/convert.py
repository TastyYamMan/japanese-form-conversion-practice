import json
from random import randint

from verbs.ます_form import ます_form
from verbs.て_form import て_form
from verbs.た_form import た_form
from verbs.ない_form import ない_form
from verbs.う_form import う_form

# TODO: Switch to xlsx
with open('verbs/verbs.json', 'r') as f:
    VERBS = json.load(f)

# TODO: create a verb object (maybe do after creating a db).

FORMS = [
    ます_form,
    て_form,
    た_form,
    ない_form,
    う_form
]

def select_conversion():
    print('Convert from which form?')
    print('1) ます')
    print('2) て')
    print('3) た')
    print('4) ない')
    print('5) う')

    from_form = input()
    try:
        from_form = int(from_form)
    except:
        raise ValueError(f'Please a number from 1-{len(FORMS)}.')
    if from_form < 1 or from_form > len(FORMS):
        raise ValueError(f'Please a number from 1-{len(FORMS)}.')

    print('Convert to which form?')
    print('1) ます')
    print('2) て')
    print('3) た')
    print('4) ない')
    print('5) う')

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

    random_index = randint(0, len(VERBS)-1)
    verb = VERBS[random_index]
    print(f"{conversion['from'](verb)['kanji']}/{conversion['from'](verb)['kana']}")
    user_input = input()

    break_flag = False
    while user_input not in ('x','X','ｘ','Ｘ'):
        
        while user_input not in conversion['to'](verb).values():
            print(conversion['to'](verb))
            print('X')
            user_input = input()
            if user_input in ('x','X','ｘ','Ｘ'):
                break_flag = True
                break
        if break_flag:
            break
        print('O')
        random_index = randint(0, len(VERBS)-1)
        verb = VERBS[random_index]
        print(f"{conversion['from'](verb)['kanji']}/{conversion['from'](verb)['kana']}")
        user_input = input()
