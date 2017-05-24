import blackjack

def main():
    """Plays the game.
    Arguments:
        None
    Returns:
        None
    """

    while True:
        player_plays = True
        dealer_plays = True

        deck = blackjack.make_new_deck()
        player = []
        dealer = []
        blackjack.shuffle(deck)
        blackjack.deal(deck, player)
        blackjack.deal(deck, dealer)
        blackjack.deal(deck, player)
        blackjack.deal(deck, dealer)
        print "\nHello."

        if blackjack.assess_score(player) == 21:
            print "\nHooray! You have Instant Blackjack!"
            player_plays = False

        blackjack.reveal_player_hand(player)

        if blackjack.assess_score(dealer) == 21:
            print "Oh no! Dealer has Instant Blackjack!"
            blackjack.reveal_dealer_full_hand(dealer)
            dealer_plays = False
        else:
            blackjack.reveal_dealer_faceup_card(dealer)

        #Player plays
        if player_plays:
            while True:
                next_move = raw_input("Do you want to hit or stand? ").lower()
                answer = blackjack.hit_or_stand(player, deck, next_move)
                if answer == "hit":
                    blackjack.reveal_player_hand(player)
                elif answer == "stand":
                    break
                elif answer == "bust":
                    blackjack.reveal_player_hand(player)
                    print "Awe, bust!"
                    dealer_plays = False
                    break
                elif answer == "win":
                    blackjack.reveal_player_hand(player)
                    print "Blackjack!"
                    break
                elif answer == "error":
                    print "Does not compute. Please type hit or stand."

        #Dealer plays
        if dealer_plays:
            print "\nDealer's turn:\n"
            blackjack.reveal_dealer_full_hand(dealer)
            while True:
                house_move = blackjack.hit_or_stand_for_the_dealer(dealer, deck)
                if house_move == "hit" or house_move  == "bust" or house_move == "win":
                    print "Dealer takes another card.\n"
                    blackjack.reveal_dealer_full_hand(dealer)

                if house_move == "stand":
                    print "Dealer stands."
                    break
                elif house_move == "bust":
                    print "Woo hoo! Dealer busts!"
                    break
                elif house_move == "win":
                    print "Snap! Dealer Blackjack!"
                    break

        #Determine winner
        compare = blackjack.determine_winner(player, dealer)
        if compare == "player":
            print "Your hand is higher. You win!"
        elif compare == "dealer":
            print "Dealer's hand is higher. Dealer wins."
        elif compare == "tie":
            print "Scores are the same. Tie!"

        #Play again or quit
        choice = raw_input("\nDo you want to play again? ")
        if choice.lower() == "yes" or choice.lower() == "y":
            continue
        else:
            print "\nThanks for playing!\n"
            break

#Main code here

main()
