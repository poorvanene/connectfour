'''POORVA NENE 38426682'''
import connectfour

'''module that consists of the functions that are the same in both user interfaces'''

def print_game_board(GameState) -> None:
    '''prints game board given a certain gamestate'''
    collist = [[x[i] for x in GameState] for i in range(len(GameState[0]))]
    print('')
    for a in range(connectfour.BOARD_COLUMNS):
        print(a + 1, ' ', end = '')
    print('')
    for a in collist:
        for b in a:
            if b == 0:
                print('.  ', end = '')
            elif b == 1:
                print('R  ', end = '')
            elif b == 2:
                print('Y  ', end = '')
        print('')
        
def getturn(GameState) -> str:
    '''returns who's turn it is given a the number returned by the turn function'''
    if GameState.turn == 1:
        return 'RED'
    elif GameState.turn == 2:
        return 'YELLOW'
    else:
        return 'NONE'
    
def convert(num: int) -> str:
    '''converts a number to a player's turn'''
    if num == 1:
        return 'RED'
    elif num == 2:
        return 'YELLOW'
    else:
        return 'NONE'

def droporpop() -> list:
    '''asks user which move they want to make and repeats until the move is valid'''
    choices = ['DROP','POP']
    answer = input('\nChoose if you want to DROP or POP and a column between 1 and ' + str(connectfour.BOARD_COLUMNS)+'. (Ex. DROP 4)"\n')
    var = False
    answer = answer.split()
    while var == False:
        if answer[0] in choices and (len(answer) == 2):
            var = True
            return answer
        else:
            answer = input('You did not choose a valid choice! \nChoose if you want to DROP or POP and a column between 1 and ' + str(connectfour.BOARD_COLUMNS)+'. (Ex. DROP 4)\n')
            answer = answer.split()
            var = False
def doingmove(move: str, col: int, gamestate):
    '''given a move, a gamestate with that move done is returned'''
    if move == 'DROP':
        return connectfour.drop(gamestate, col)
    elif move == 'POP':
        return connectfour.pop(gamestate, col)
