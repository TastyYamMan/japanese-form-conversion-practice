import json
from random import randint

from て_form import て_form
from た_form import た_form

with open('verbs.json', 'r') as f:
    VERBS = json.load(f)

GAMES = [
    (て_form,'forward'),
    (て_form,'backward'),
    (た_form,'forward'),
    (た_form,'backward')
]

def select_game():
    print('For the game you wish to play what for?')
    print('1) ます_to_て')
    print('2) て_to_ます')
    print('3) ます_to_た')
    print('4) た_to_ます')

    game = input()
    try:
        game = int(game)
    except:
        raise ValueError(f'Please a number from 1-{len(GAMES)}.')
    if game < 1 or game > len(GAMES):
        raise ValueError(f'Please a number from 1-{len(GAMES)}.')
    return GAMES[game-1]

def correct_conversion(game, verb, input):
    if game[1] == 'forward':
        return input in game[0](verb).values()
    return input in verb.values()

def conversion_game():

    game = select_game()

    random_index = randint(0, len(VERBS)-1)
    verb = VERBS[random_index]
    if game[1] == 'forward':
        print(f"{verb['kanji']}/{verb['kana']}")
    else:
        print(f"{game[0](verb)['kanji']}/{game[0](verb)['kana']}")
    user_input = input()
    break_flag = False
    while user_input not in ('x','X','ｘ','Ｘ'):
        
        while not correct_conversion(game, verb, user_input):
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
        if game[1] == 'forward':
            print(f"{verb['kanji']}/{verb['kana']}")
        else:
            print(f"{game[0](verb)['kanji']}/{game[0](verb)['kana']}")
        user_input = input()
    #if convert_from in ('ます', 'masu'):
    #    if convert_to in ('て', 'te'):
