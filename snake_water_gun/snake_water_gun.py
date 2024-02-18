# Write python program to play Snake water gun with computer


import random


mat =[[0,1,-1], [-1,0,1], [1,-1,0]]


score=0
game = True
while game:
    choice= input("Enter your choice from snake, water,gun:  ")
    player_choice= 0 if (choice=="snake") else (1 if(choice=="water") else 2)
    random_choice = random.randint(0,2)
    
    comp_choice="snake" if (random_choice==0) else ("water" if(random_choice==1) else "gun")
    print(f"Computer choice is: {comp_choice}")
    score = score+ mat[player_choice][random_choice]
    winner = "Draw" if( mat[player_choice][random_choice]==0 ) else ("Player" if( mat[player_choice][random_choice]>0) else "Computer")
    print(f"Winner is:   {winner}")


    status= int(input("1 to continue or 0 to end the game: "))
    game = False if status == 0 else True

final_winner = "Draw" if( score==0 ) else ("Player" if( score>0) else "Computer")
print(f"\nFinal Winner is:   {final_winner}\n")