import sys
import os
import random
import time

base_board = {
    'top-l': ' ',
    'top-m': ' ',
    'top-r': ' ',
    'middle-l': ' ',
    'middle-m': ' ',
    'middle-r': ' ',
    'bottom-l': ' ',
    'bottom-m': ' ',
    'bottom-r': ' '
}
luck = ['X', 'O']
player_luck = ['C', 'P']


def help():
    print("""----- Help Desk -----
    In this game you can either play PvP or PvC
    You and your opponent will get choice to make turn by turn
    You will be assigned sign either X or O randownly
    When  3 of your sign makes either vertical, horizontal,diogonal line ---> You win
    But if your opponent makes it first ---> Opponent wins""")
    main()


def board(base_board):
    print(base_board['top-l'] + '|' +
          base_board['top-m'] + '|' + base_board['top-r'])
    print('-+-+-')
    print(base_board['middle-l'] + '|' +
          base_board['middle-m'] + '|' + base_board['middle-r'])
    print('-+-+-')
    print(base_board['bottom-l'] + '|' +
          base_board['bottom-m'] + '|' + base_board['bottom-r'])

def again():
    print('''Do you want to play again
    Press Y to  Play again
    Press N to Quit''')
    a = input()
    if a.lower()=='y':
        play()
    elif  a.lower()=='n':
        sys.exit()
    else:
        print("Please enter correct choice")
        again()

def  computer_win(base_board):
    os.system('cls')
    board(base_board)
    print("Computer wins")
    again()

def player_move():
    
    player_think = input()
    while player_think not in base_board.keys():
        print('Please enter correct choice:')
        player_think = input()
        
   
    return player_think
    
def  player_win(player=None , base_board=base_board):
    os.system('cls')
    board(base_board)
    if player ==None:
        print("Player wins")
    else:
        print('Hurry',player,"wins")
    again()

def draw():
    os.system('cls')
    print("Game Draw")
    again()



def computer(base_board, luck, player_luck):
    a = random.choice(luck)
    b = random.choice(player_luck)
    c = []

    for i in base_board.keys():
        c.append(i)
    luck.remove(a)
    if b == 'C':
        print('By the random draw first move will be played by computer and play with ' +
              a+' Similarly second move will be played by person and play with '+luck[0])
        comp = ['C', a]
        plays = ['P', luck[0]]
    elif b == 'P':
        print('By the random draw first move will be played by player and play with ' +
              a+' Similarly second move will be played by computer and play with '+luck[0])
        comp = ['C', luck[0]]
        plays = ['P', a]
    board(base_board)
    for i in range(9):
        if b == 'C':
            print("Please wait computer is thinking its move")
            time.sleep(1)
            os.system('cls')
            computer_think = random.choice(c)
            base_board[computer_think] = comp[1]
            b = 'P'
            c.remove(computer_think)
            board(base_board)
            if (base_board['top-l']==base_board['top-m']==base_board['top-r']==comp[1]) or (base_board['middle-l']==base_board['middle-m']==base_board['middle-r']==comp[1])or(base_board['bottom-l']==base_board['bottom-m']==base_board['bottom-r']==comp[1])or(base_board['top-l']==base_board['middle-l']==base_board['bottom-l']==comp[1])or(base_board['top-m']==base_board['middle-m']==base_board['bottom-m']==comp[1])or(base_board['top-r']==base_board['middle-r']==base_board['bottom-r']==comp[1])or(base_board['top-l']==base_board['middle-m']==base_board['bottom-r']==comp[1])or(base_board['top-r']== base_board['middle-m']==base_board['bottom-l']==comp[1]):
                computer_win(base_board)



        elif b == 'P':
            print("Its your choice. You either one  of the place")
            print(c)
            player_think = player_move()
            time.sleep(1)
            os.system('cls')
            base_board[player_think] = plays[1]
            b = 'C'
            c.remove(player_think)
            board(base_board)
            if (base_board['top-l']==base_board['top-m']==base_board['top-r']==plays[1]) or (base_board['middle-l']==base_board['middle-m']==base_board['middle-r']==plays[1])or(base_board['bottom-l']==base_board['bottom-m']==base_board['bottom-r']==plays[1])or(base_board['top-l']==base_board['middle-l']==base_board['bottom-l']==plays[1])or(base_board['top-m']==base_board['middle-m']==base_board['bottom-m']==plays[1])or(base_board['top-r']==base_board['middle-r']==base_board['bottom-r']==plays[1])or(base_board['top-l']==base_board['middle-m']==base_board['bottom-r']==plays[1])or(base_board['top-r']== base_board['middle-m']==base_board['bottom-l']==plays[1]):
                player_win(base_board=base_board)

    draw()



def main():
    name = input("""----- Welcome To Tic Tac Toe ------
    Enter Y to Play.
    Enter N to Quit 
    Enter H for help: """)
    if name.lower() == 'y':
        os.system('cls')
        play()
    elif name.lower() == 'n':
        os.system('cls')
        sys.exit()
    elif name.lower() == 'h':
        os.system('cls')
        help()
    else:
        os.system('cls')
        print('Oops, you entered wrong choice. Please recheck your choice and enter again')
        main()


def choice_2(base_board, luck):
    names= []
    name1 = input('Enter Player 1: ')
    names.append(name1)
    name2 = input('Enter Player 2: ')
    names.append(name2)
    print(names)
    a = random.choice(luck)
    b = random.choice(names)
    c = []

    for i in base_board.keys():
        c.append(i)
    luck.remove(a)
    if b == names[0]:
        print('By the random draw first move will be played by' ,names[0], 'and play with ' +
              a+' Similarly second move will be played by', names[1] ,'and play with '+luck[0])
        Player_first = [names[0], a]
        Player_second = [names[1], luck[0]]
    elif b == names[1]:
        print('By the random draw first move will be played by',names[1],' and play with ' +
              a+' Similarly second move will be played by' ,names[0], 'and play with '+luck[0])
        Player_first = [names[0], luck[0]]
        Player_second = [names[1], a]
    board(base_board)


    for i in range(9):
        if b == names[0]:
            print("Its",names[0]+ "'s turn. Choose either one  of the place")
            print(c)
            player_think = player_move()
            time.sleep(1)
            os.system('cls')
            base_board[player_think] = Player_first[1]
            b = names[1]
            c.remove(player_think)
            board(base_board)
            if (base_board['top-l']==base_board['top-m']==base_board['top-r']==Player_first[1]) or (base_board['middle-l']==base_board['middle-m']==base_board['middle-r']==Player_first[1])or(base_board['bottom-l']==base_board['bottom-m']==base_board['bottom-r']==Player_first[1])or(base_board['top-l']==base_board['middle-l']==base_board['bottom-l']==Player_first[1])or(base_board['top-m']==base_board['middle-m']==base_board['bottom-m']==Player_first[1])or(base_board['top-r']==base_board['middle-r']==base_board['bottom-r']==Player_first[1])or(base_board['top-l']==base_board['middle-m']==base_board['bottom-r']==Player_first[1])or(base_board['top-r']== base_board['middle-m']==base_board['bottom-l']==Player_first[1]):
                player_win(player=names[0])



        elif b == names[1]:
            print("Its",names[1]+ "'s turn. Choose either one  of the place")
            print(c)
            player_think = player_move()
            time.sleep(1)
            os.system('cls')
            base_board[player_think] = Player_second[1]
            b = names[0]
            c.remove(player_think)
            board(base_board)
            if (base_board['top-l']==base_board['top-m']==base_board['top-r']==Player_second[1]) or (base_board['middle-l']==base_board['middle-m']==base_board['middle-r']==Player_second[1])or(base_board['bottom-l']==base_board['bottom-m']==base_board['bottom-r']==Player_second[1])or(base_board['top-l']==base_board['middle-l']==base_board['bottom-l']==Player_second[1])or(base_board['top-m']==base_board['middle-m']==base_board['bottom-m']==Player_second[1])or(base_board['top-r']==base_board['middle-r']==base_board['bottom-r']==Player_second[1])or(base_board['top-l']==base_board['middle-m']==base_board['bottom-r']==Player_second[1])or(base_board['top-r']== base_board['middle-m']==base_board['bottom-l']==Player_second[1]):
                player_win(player=names[1])

    draw()



def play():
    os.system('cls')
    name = int(input("""You can either play with computer or your friend
    Press 1 to play with computer
    Press 2 to play with your friend """))
    if name == 1:
        os.system('cls')
        computer(base_board, luck, player_luck)
    elif name == 2:
        os.system('cls')
        choice_2(base_board, luck)
    else:
        os.system('cls')
        print('Oops, you entered wrong choice. Please recheck your choice and enter again')
        play()


main()
