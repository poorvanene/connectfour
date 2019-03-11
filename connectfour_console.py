import connectfour
import connectfour_common

'''module that implements the console-only user interface'''

    
def startgame() -> None:
    '''goes through console version of Connect Four'''
    print('Welcome to Connect 4!')
    gamestate = connectfour.new_game()
    connectfour_common.print_game_board(gamestate.board)
    while connectfour.winner(gamestate) == 0:
        print('It is the', connectfour_common.getturn(gamestate), 'players turn!\n')
        choice = connectfour_common.droporpop()
        var = False
        while var == False:
            try:
                a = (int(choice[1]) - 1)
                gamestate = connectfour_common.doingmove(choice[0],a,gamestate)
                connectfour_common.print_game_board(gamestate.board)
                var = True
            except connectfour.GameOverError:
                print('GAME OVER!')
                var = True
            except:
                print('Invalid move')
                choice = connectfour_common.droporpop()
    ending(gamestate)

                
        

    
                   
                
def ending(GameState):
    '''prints the winner and asks the player if they want to play again'''
    winner = connectfour_common.convert(connectfour.winner(GameState))
    print('GAME OVER!', winner, 'player won the game!')
    playagain = input('Do you want to play again? (Y/N)\n')
    var = False
    while var == False:
        if playagain is 'Y':
            var = True
            startgame()
        elif playagain is 'N':
            print('Thanks for playing! See you again!')
            var = True
        else:
            var = False
            playagain = input('Choose a valid choice - either Y or N\n')
    
    
 
    
if __name__ == '__main__':
    startgame()
    
