 #++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
 # _____            _          _____                             _____      _                           #
 #|  __ \          | |        |  __ \                           / ____|    (_)                          #
 #| |__) |___   ___| | __     | |__) |_ _ _ __   ___ _ __      | (___   ___ _ ___ ___  ___  _ __ ___    #
 #|  _  // _ \ / __| |/ /     |  ___/ _` | '_ \ / _ \ '__|      \___ \ / __| / __/ __|/ _ \| '__/ __|   #
 #| | \ \ (_) | (__|   <   _  | |  | (_| | |_) |  __/ |     _   ____) | (__| \__ \__ \ (_) | |  \__ \   #
 #|_|  \_\___/ \___|_|\_\ ( ) |_|   \__,_| .__/ \___|_|    ( ) |_____/ \___|_|___/___/\___/|_|  |___/   #
 #                        |/             | |               |/                                           #
 #                                       |_|                                                            #
 #++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

import random 


name = input('Please enter your name here -> ')

print(f'What\'s going to be your move {name}?')

print('1) Rock 🪨')
print('2) Paper 🗞️')
print('3) Scissors ✂️')

player = int(input('Your Move -> '))

computer = random.randint(1, 3)

def compare (player, computer ):
  if player == computer:
   print('Computer has picked the same move')
   print('it\'s a tie!')
  
  elif player == 1 and computer == 2:
   print('Computer has picked paper')
   print('Paper wins against Rock')
   print(f'{name} Loses!')

  elif player == 1 and computer == 3:
    print('Computer has picked Scissors')
    print('Rock wins against Scissors')
    print(f'{name} Wins!')

  elif player == 2 and computer == 3:
    print('Computer has picked Scissors')
    print('Paper loses against Scissors')
    print(f'{name} loses!')
  
  elif player == 2 and computer == 1:
    print('Computer has picked Rock')
    print('Paper wins against Rock')
    print(f'{name} wins!')

  elif player == 3 and computer ==1:
    print('Computer has picked Rock')
    print('Scissors loses against Rock')
    print(f'{name} loses!')

  elif player == 3 and computer == 2:
    print('Computer has picked Paper')
    print('Scissors wins against Paper')
    print(f'{name} wins!')

compare (player, computer)