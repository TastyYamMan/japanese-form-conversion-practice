import words.memory_game
import verbs.convert
import adjectives.convert

# TODO: Don't need two files for for conversion games they are the same but with different forms and objects (verbs/adjs)
#        i.e. consolidate to one file

GAMES = [
    memory_game := words.memory_game.memory_game,
    verbs := verbs.convert.conversion_game,
    adjs := adjectives.convert.conversion_game
]

def select_game():
    print('What game do you want to play?')
    print('1) Memory card game')
    print('2) Verb conversion')
    print('3) Adjective conversion')


    game = input()
    try:
        game = int(game)
    except:
        raise ValueError(f'Please a number from 1-{len(GAMES)}.')
    if game < 1 or game > len(GAMES):
        raise ValueError(f'Please a number from 1-{len(GAMES)}.')
    
    GAMES[game-1]()

if __name__ == '__main__':
    select_game()
