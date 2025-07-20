import datetime
from db import session

def upgrade_status(word, language):
    if language == '日本語':
        if word.j_to_e_revision_status_id is None:
            word.j_to_e_revision_status_id = 0
        elif word.j_to_e_revision_status_id in [1,2]:
            word.j_to_e_revision_status_id -= 1
        elif word.j_to_e_revision_status_id == 3 and word.incorrect_count < 2:
            word.j_to_e_revision_status_id -= 1
        word.j_to_e_last_time_revised = datetime.datetime.now()
    else:
        if word.e_to_j_revision_status_id is None:
            word.e_to_j_revision_status_id = 0
        elif word.e_to_j_revision_status_id in [1,2]:
            word.e_to_j_revision_status_id -= 1
        elif word.e_to_j_revision_status_id == 3 and word.incorrect_count < 2:
            word.e_to_j_revision_status_id -= 1
        word.e_to_j_last_time_revised = datetime.datetime.now()
    word.incorrect_count = 0
    session.commit()

def downgrade_status(word, language):
    if language == '日本語':
        if word.j_to_e_revision_status_id is None:
            word.j_to_e_revision_status_id = 2
        elif word.j_to_e_revision_status_id <= 1:
            word.j_to_e_revision_status_id = 2
        elif word.j_to_e_revision_status_id == 2 and word.incorrect_count > 1:
            word.j_to_e_revision_status_id = 3
    else:
        if word.e_to_j_revision_status_id is None:
            word.e_to_j_revision_status_id = 2
        elif word.e_to_j_revision_status_id <= 1:
            word.e_to_j_revision_status_id = 2
        elif word.e_to_j_revision_status_id == 2 and word.incorrect_count > 1:
            word.e_to_j_revision_status_id = 3
    word.incorrect_count += 1
    session.commit()

def flash_card(word, language):
    if language == '日本語':
        print(f"L-{word.lesson}:{word.kanji}/{word.kana} {word.j_to_e_revision_status_id}")
    else:
        print(f"L-{word.lesson}:{word.meaning} {word.e_to_j_revision_status_id}")

    user_input = input()
    if user_input in ('x','X','ｘ','Ｘ'):
        return None

    if language == '日本語':
        print(f"L-{word.lesson}:{word.meaning}")
    else:
        print(f"L-{word.lesson}:{word.kanji}/{word.kana}")

    user_input = input()
    if user_input in ('x','X','ｘ','Ｘ'):
        return None

    while user_input not in ('y','Y','ｙ','Ｙ', 'n', 'N', 'ｎ', 'Ｎ'):
        if user_input in ('x','X','ｘ','Ｘ'):
            return None
        user_input = input()

    if user_input in ('y','Y','ｙ','Ｙ'):
        upgrade_status(word, language)
        return True
    else:
        downgrade_status(word, language)
        return False
