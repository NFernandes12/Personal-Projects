import random

def play():
    usr_choice = input('Select "r" for rock "p" for paper or "s" for scissors: ').lower()
    cpu_choice = random.choice(['r','p','s'])
    print(f'Opponent picked {cpu_choice}')

    #paper > rock. scissor > paper, rock > scissor
    if who_win(usr_choice,cpu_choice):
        return "You win"
    
    if usr_choice == cpu_choice:
        return 'It is a tie'
    
    return 'You lose'
    
def who_win(player,opponent):
    if player == 'r' and opponent == 's' or player == 'p' and opponent == 'r' or player == 's' and opponent == 'p':
        return True
    
print(play())