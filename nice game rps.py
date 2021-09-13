import random
#choices
def Player_Choice():
    player = input('Enter your choice: rock, paper, scissors\n')
    if player not in [r,s,p]: 
        print("idiot check spelling and try again")
        player = Player_Choice()
    return player

def Computer_Choice():
    computer = random.choice([r,p,s])
    return computer

def Result():
    print("You: ",player_score,"Computer: ", comp_score)
    if player_score > comp_score:
        print ('YOU WON')
    elif player_score < comp_score:
        print('YOU LOST')
    elif player_score == comp_score:
        print('TIE')
    print("Thanks 4 Playing")
     

#mainblock
r = "rock"
s = 'scissors'
p = 'paper'
player_score = 0
comp_score = 0
n = int(input("how many rounds you want?:\n"))
for i in range(n):
    player = Player_Choice()
    computer = Computer_Choice()
    print("You: ",player,"Computer: ", computer)
    if player > computer:
        player_score +=1
    elif player < computer:
        comp_score +=1
Result()
   

