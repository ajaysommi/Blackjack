from p1_random import P1Random

rng = P1Random()

loop_active = True  # variable that determines whether the overall loop of the game continues running.
round_num = 0
user_wins = 0
dealer_wins = 0
tie_games = 0

while loop_active:  # loops the program until the user exits (loop_active becomes false)
    round_num += 1
    print(f"START GAME #{round_num} \n")  # prints round number for the game
    card = rng.next_int(13) + 1
    hand = 0
    if card == 1:
        print(f"Your card is a ACE!")  # prints the value of the card as ACE if "card" value equals 1.
        card = 1
    elif 2 <= card <= 10:
        print(f"Your card is a {card}!")
        pass
    elif card == 11:
        print(f"Your card is an JACK!")
        card = 10
    elif card == 12:
        print(f"Your card is an QUEEN!")
        card = 10
    elif card == 13:
        print(f"Your card is a KING!")
        card = 10
        pass
    hand += card  # adds the card value to the player hand
    print(f"Your hand is: {hand}\n")

    user_selection_loop = True  # initializes the inner while loop to print user menu.

    while user_selection_loop:  # continues looping menu for user
        print("1. Get another card")
        print("2. Hold hand")
        print("3. Print statistics")
        print("4. Exit\n")

        user_selection_value = int(input("Choose an option: "))  # prompts user to enter a menu option.
        print("")

        if user_selection_value == 1:
            card = rng.next_int(13) + 1
            if card == 1:
                print(f"Your card is a ACE!")  # prints the values of each card if they are not number values.
                card = 1
            elif 2 <= card <= 10:
                print(f"Your card is a {card}!")
                pass
            elif card == 11:
                print(f"Your card is a JACK!")  # prints the values of each card if they are not number values.
                card = 10
            elif card == 12:
                print(f"Your card is a QUEEN!")  # prints the values of each card if they are not number values.
                card = 10
            elif card == 13:
                print(f"Your card is a KING!")  # prints the values of each card if they are not number values.
                card = 10
                pass
            hand += card  # adds card value to total hand value
            print(f"Your hand is: {hand}\n")  # prints total hand value

            if hand == 21:
                print("BLACKJACK! You win!\n")
                user_wins += 1
                user_selection_loop = False  # exits inner loop whenever user user wins

            elif hand > 21:
                print("You exceeded 21! You lose.\n")
                dealer_wins += 1
                user_selection_loop = False  # exits inner loop whenever user exceeds 21

        elif user_selection_value == 2:  # enters second scenario whenever user selects 2
            dealer_hand = rng.next_int(11) + 16
            print(f"Dealer's hand: {dealer_hand}")
            print(f"Your hand is: {hand}\n")

            if dealer_hand < hand:
                print("You win!\n")
                user_selection_loop = False
                user_wins += 1  # user gets point whenever they win
            elif dealer_hand > 21:
                print("You win!\n")
                user_selection_loop = False
                user_wins += 1  # user gets point whenever they win
            elif dealer_hand == hand:
                print("It's a tie! No one wins!\n")
                tie_games += 1  # tie variable increases by 1 whenever a tie occurs
                user_selection_loop = False
            else:
                print("Dealer wins!\n")
                dealer_wins += 1
                user_selection_loop = False  # dealer gets 1 point whenever they win the round

        elif user_selection_value == 3:  # shows menu when user selects 3
            user_total = (user_wins + dealer_wins + tie_games)  # adds user wins, dealer wins, and total ties to
            # separate variable.
            user_wins_percentage = (user_wins / user_total) * 100  # percentage of user wins by dividing the user wins
            # by the user_total.
            if user_wins_percentage >= 100.0:
                user_wins_percentage = 100.0
            print(f"Number of Player wins: {user_wins}")
            print(f"Number of Dealer wins: {dealer_wins}")
            print(f"Number of tie games: {tie_games}")
            print(f"Total # of games played is: {round_num - 1}")
            print(f"Percentage of Player wins: {user_wins_percentage}%\n")
            # prints all statistics for user including the number of wins and percentage of wins

        elif user_selection_value == 4:
            loop_active = False
            break  # exits inner loop whenever user input 4 as the menu value

        elif user_selection_value < 1 or user_selection_value > 4:  # if user value is entered out of bounds
            print("Invalid input! \nPlease enter an integer value between 1 and 4.\n")  # displays error message
            # if user enters a value outside the bounds allowed
