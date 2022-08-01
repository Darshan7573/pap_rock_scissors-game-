import random
rock=('''
                _    
               | |   
 _ __ ___   ___| | __
| '__/ _ \ / __| |/ /
| | | (_) | (__|   < 
|_|  \___/ \___|_|\_\
''')

paper=('''
 _ __   __ _ _ __   ___ _ __ 
| '_ \ / _` | '_ \ / _ \ '__|
| |_) | (_| | |_) |  __/ |   
| .__/ \__,_| .__/ \___|_|   
| |         | |              
|_|         |_|              ''')

scissors=('''
   ____
  / __ \
 ( (__) |___ ___
  \________,'   """""----....____
   _______<  () dd       ____----'
  / __   __`.___-----""""
 ( (__) |
  \____/

''')


game_images=[rock,paper,scissors]

user_choice=int(input("Choose the number?,0 for rock,1 for paper,2 for scissors\n"))
if user_choice >=3 or user_choice < 0:
	print("You choose invalid number!you loose")
else:
    print(game_images[user_choice])

    computer_choice = random.randint(0,2)
    print("computer choose:")
    print(game_images[computer_choice])
    if computer_choice == 0 and user_choice == 1:
    	print("You Win")
    elif computer_choice == 2 and user_choice == 0:
    	print("You Win")
    elif computer_choice > user_choice:
    	print("You loose!")
    elif user_choice > computer_choice:
    	print("You Win")
    elif  computer_choice == user_choice:
    	print("Draw")