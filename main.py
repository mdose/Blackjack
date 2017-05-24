import blackjack

def get_menu_choice():
    """Print a menu and asks the user to make a choice.
    Arguments:
      None
    Returns:
      int: the user's menu choice
    """

    print '\n    0 - Main Menu'
    print '    1 - You play'
    print '    2 - Dealer plays'
    print '    3 - Determine Bust or Blackjack'
    print '    4 - Determine high score'
    print '    5 - Exit the program.\n'

    choice = int(raw_input('Choose from the menu options: '))

    return choice

def main():
    """Plays the game.
    Arguments:
        None
    Returns:
        None
    """

    while True:

        choice = get_menu_choice()

        if choice == 0:
            # main menu

            continue  # continue goes to the next loop iteration

        elif choice == 1:
            # start game

            # call function to make and shuffle deck; deal intital hand
            deck = blackjack.make_new_deck()
            player = []
            dealer = []
            blackjack.shuffle(deck)
            blackjack.deal(deck, player)
            blackjack.deal(deck, dealer)
            blackjack.deal(deck, player)
            blackjack.deal(deck, dealer)
            print "\nHello."
            #answer = raw_input("Do you want to play a game? Yes or No? ")
            #if answer == "yes" or "Yes":
            blackjack.reveal_player_hand(player)
            blackjack.reveal_dealer_faceup_card(dealer)
            while True:
                answer = blackjack.hit_or_stand(player, deck)
                if answer == "hit":
                    blackjack.reveal_player_hand(player)
                elif answer == "stand":
                    break
                elif answer == "bust":
                    blackjack.reveal_player_hand(player)
                    print "Awe, bust! You lose!"
                    break
                elif answer == "win":
                    blackjack.reveal_player_hand(player)
                    print "Blackjack! You win!"
                    break
                elif answer == "error":
                    print "Does not compute. Please type hit or stand."

        elif choice == 2:
             # dealer plays; must hit if under 17
             print "\nDealer's turn:\n"
             blackjack.reveal_dealer_full_hand(dealer)
             blackjack.reveal_if_natural_blackjack(player, dealer)
             while True:
                 house_score = blackjack.dealer_plays(dealer, deck)
                 if house_score == "hit":
                     print "Dealer takes another card.\n"
                     blackjack.reveal_dealer_full_hand(dealer)
                 elif house_score == "stand":
                     break
                 elif house_score == "bust":
                     blackjack.reveal_dealer_full_hand(dealer)
                     print "Dealer busts! You win!"
                     break
                 elif house_score == "win":
                     blackjack.reveal_dealer_full_hand(dealer)
                     print "Dealer Blackjack! You lose!"
                     break

        elif choice == 3:
            player_bust = blackjack.determine_if_bust(player)
            dealer_bust = blackjack.determine_if_bust(dealer)
            blackjack.reveal_player_hand(player)
            blackjack.reveal_dealer_full_hand(dealer)
            if player_bust == "bust":
                print "Awe, bust! You lose!"
            elif player_bust == "win":
                print "Blackjack! You win!"
            elif dealer_bust == "bust":
                print "Dealer busts! You win!"
            elif dealer_bust == "win":
                print "Dealer Blackjack! You lose!"

        elif choice == 4:
            while True:
                compare = blackjack.determine_winner(player, dealer)
                if compare == "player":
                    print "\nYour hand is higher. You win!"
                    break
                elif compare == "dealer":
                    print "\nAwe, dealer's hand is higher. Dealer wins."
                    break
                elif compare == "tie":
                    print "\nScores are the same. Tie!"
                    break

        elif choice == 5:
            # quit
            break

#Main code here

main()
