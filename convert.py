import json
from random import randint

from ます_to_て import ます_to_て

with open('verbs.json', 'r') as f:
    VERBS = json.load(f)

def conversion_game():#convert_from, convert_to):
    random_index = randint(0, len(VERBS)-1)
    word = VERBS[random_index]
    print(f"{word['kanji']}/{word['kana']}")
    user_input = input()
    break_flag = False
    while user_input not in ('x','X','ｘ','Ｘ'):
        while ます_to_て(word) != user_input:
            print('X')
            user_input = input()
            if user_input in ('x','X','ｘ','Ｘ'):
                break_flag = True
                break
        if break_flag:
            break
        print('O')
        random_index = randint(0, len(VERBS)-1)
        word = VERBS[random_index]
        print(f"{word['kanji']}/{word['kana']}")
        user_input = input()
    #if convert_from in ('ます', 'masu'):
    #    if convert_to in ('て', 'te'):
