import pandas as pd
from random import randint

WORDS = pd.read_excel('words/words.xlsx')

# TODO: create an adjective object (maybe do after creating a db).

LANGUAGES = [
    日本語,
    english
]

ACTIVITIES = [
    practice_lesson#,
    #revision
]

LESSONS = 26

def select_game():
    print('Translate from which language?')
    print('1) 日本語')
    print('2) English')

    from_language = input()
    try:
        from_language = int(from_language)
    except:
        raise ValueError(f'Please a number from 1-{len(LANGUAGES)}.')
    if from_language < 1 or from_language > len(LANGUAGES):
        raise ValueError(f'Please a number from 1-{len(LANGUAGES)}.')
    
    print('What activity would you like to do?')
    print('1) Practice a lesson')
    #print('2) Revision')

    activity = input()
    try:
        activity = int(activity)
    except:
        raise ValueError(f'Please a number from 1-{len(LANGUAGES)}.')
    if activity < 1 or activity > len(LANGUAGES):
        raise ValueError(f'Please a number from 1-{len(LANGUAGES)}.')
    
    return LANGUAGES[from_language - 1], ACTIVITIES[activity - 1]

def choose_lesson():
    print(f'Which lesson do you want to practice (1-{LESSONS})?')

    lesson = input()
    try:
        lesson = int(lesson)
    except:
        raise ValueError(f'Please a number from 1-{LESSONS}.')
    if lesson < 1 or lesson > LESSONS:
        raise ValueError(f'Please a number from 1-{LESSONS}.')
    return lesson

def practice_lesson():
    

def flash_card():

    language, activity = select_game()
    activity()
        

    random_index = randint(0, len()-1)
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
