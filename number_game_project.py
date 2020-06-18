import random  

def start_game():
    random_num = random.randint(1,10)
    score_count = 0
    print("Hello, welcome Alexandria's Number Guessing Game!")
    
    while  True:
        player_guess = input("\nWhat number from 1-10 would you like to guess?  ")
        
        player_guess = int(player_guess)
        if player_guess > 10 or player_guess < 1:
            score_count += 1
            print("\nYour guess must be between 1 and 10, please try again:   ")
        if player_guess == random_num:
            score_count += 1
            next_game = input("\nGreat job! Your score was {}. Would you like to play again?\nYes or No   ".format(score_count))
            if next_game.lower() == 'yes':
                print("\nThe score to beat is {}.".format(score_count))
                continue
            elif next_game.lower() == 'no':
                print("\nThanks for playing. See you next time!")
                break
        elif player_guess > random_num and player_guess < 11:
            score_count += 1
            print("It's lower")
            continue
        elif player_guess < random_num and player_guess > 0:
            score_count += 1
            print("It's higher")
            continue
        
start_game()