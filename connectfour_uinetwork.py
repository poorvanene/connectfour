import connectfour_network
import connectfour
import connectfour_common

'''module that implements the user interface for the networked version'''

def start() -> None:
    '''asks user input for host & port and tries to connect'''
    host = connectfour_network.gethost()
    port = connectfour_network.getport()
    print('Connecting...')
    try:
        connection = connectfour_network.connect(host,port)
        print('Connected!')
        game(connection)

    except:
        print('Error. Connection Unsuccesful')
    
def game(connection: 'connection') -> None:
        '''goes through server version of connect four'''
        intromessage(connection)
        print('Welcome to Connect 4!')
        print('You are the RED player!')
        gamestate = connectfour.new_game()
        connectfour_common.print_game_board(gamestate.board)
        connectfour_network.send_message(connection, ('AI_GAME'))


        
        while True:
            a = connectfour_network.read_message(connection)
            if (a) == 'READY':
                print('\nIt is the', connectfour_common.getturn(gamestate), 'players turn!')
                answer = input('Choose if you want to DROP or POP and a column between 1 and ' + str(connectfour.BOARD_COLUMNS)+'. (Ex. DROP 4)"\n')
                answer = isvalid(answer)
                anslist = answer.split()
                connectfour_network.send_message(connection, answer)
                try:
                    c = (int(anslist[1]) - 1)
                    gamestate = connectfour_common.doingmove(anslist[0],c,gamestate)
                    connectfour_common.print_game_board(gamestate.board)
                except:
                    pass                
            elif a == 'OKAY':
                print('\nIt is the', connectfour_common.getturn(gamestate), 'players turn!\n')
                output = connectfour_network.read_message(connection)
                move = printturn(output,gamestate,connection)
                col = (int(move[1]) - 1)
                gamestate = connectfour_common.doingmove(move[0],col,gamestate)
                connectfour_common.print_game_board(gamestate.board)                
            elif a == 'INVALID':
                print('Invalid choice choose again.')
                
            elif a == "WINNER_RED":
                print('GAME OVER! You are the winner!')
                connectfour_network.close(connection)
                break
    
            elif a == "WINNER_YELLOW":
                print('GAME OVER! YOU LOST! Yellow player is the winner!')
                connectfour_network.close(connection)
                break
            elif a == ('ERROR'):
                print('Invalid choice choose again')
                pass

        
def isvalid(mover: str) -> str:
    '''decides whether client's move choice is valid.'''
    options = ['DROP','POP']
    move = mover.split()
    if (len(move) == 2) and (move[0] in options):
        return mover
    else:
        sample = 'DROP 10000'
        return sample
    


        
def printturn(move,gamestate,connection) -> list:
    '''given the server's move, this function decides whether the move is valid. If not, connection is closed'''
    options = ['DROP','POP']
    move = move.split()
    if (len(move) == 2) and (move[0] in options) and (0 <= int(move[1]) <= connectfour.BOARD_COLUMNS):
        return move
    else:
        print('The yellow player made an invalid move. Connection is closing.')
        connectfour_network.close(connection)

        
def intromessage(connection: 'connection') -> None:
    '''sends intro message to server'''
    connectfour_network.send_message(connection, ('I32CFSP_HELLO ' + getusername()))
    print(connectfour_network.read_message(connection))


    
    
def getusername() -> str:
    '''asks for a username from client. It keeps asking until username is valid'''
    var = False
    username = input('Specify a username: there must be no whitespaces\n')
    while var == False:
        if ' ' in username:
            var = False
            username = input('Your username had whitespaces. Specify another username:\n')
        
        else:
            var = True
            return username


if __name__ == "__main__":
    start()
