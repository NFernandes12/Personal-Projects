import random 
#user guessing
def guess(x):
    random_num=random.randint(1,x)
    guess = 0 
    while guess != random_num:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess > random_num:
            print("Too high try again")
        else:print('Too low try again')

    print(f'nice job you got it the answer was {random_num}')

#computer guessing
def computer_guess(x):
    low= 1
    high=x
    feedback=''
    while feedback != 'c': #"correct"
        if low != high:
            guess = random.randint(low,high)
        else:guess=low
        feedback = input(f'is {guess} too high (h), low (l) or correct (c)').lower()
        if feedback == "h":
            high = guess - 1
        elif feedback== "l":
            low = guess + 1

    print(f'nice the computer guessed your number, {guess} correctly')
computer_guess(100)