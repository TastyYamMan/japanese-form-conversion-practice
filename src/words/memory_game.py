from .config import LANGUAGES, LESSONS
from .lesson import practice_lesson
from .revision import revision

ACTIVITIES = [practice_lesson, revision]

def select_game():
    print('Translate from which language?')
    print('1) 日本語')
    print('2) English')
    from_language = int(input())

    print('What activity would you like to do?')
    print('1) Practice a lesson')
    print('2) Revision')
    activity = int(input())

    return LANGUAGES[from_language - 1], ACTIVITIES[activity - 1]

def choose_lesson():
    print(f'Which lesson do you want to practice (1-{LESSONS})?')
    lesson = int(input())
    print(f'Do you want to practice with all words? (y/n)')
    all = input()
    if all in ('Y','y','ｙ','Ｙ'):
        all = True
    elif all in ('N','n','ｎ','Ｎ'):
        all = False
    else:
        raise ValueError('input needs to be y/n.')
    return lesson, all

def memory_game():
    language, activity = select_game()
    activity(language)
