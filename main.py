import blackjack
import time

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
            time.sleep(1)
            print "\nHooray! You have Instant Blackjack!"
            player_plays = False

        blackjack.reveal_player_hand(player)

        if blackjack.assess_score(dealer) == 21:
            time.sleep(1)
            print "Oh no! Dealer has Instant Blackjack!"
            blackjack.reveal_dealer_full_hand(dealer)
            dealer_plays = False
        else:
            blackjack.reveal_dealer_faceup_card(dealer)

        #Player plays
        if player_plays:
            while True:
                time.sleep(1)
                next_move = raw_input("Do you want to hit or stand? ").lower()
                answer = blackjack.hit_or_stand(player, deck, next_move)
                if answer == "hit":
                    time.sleep(1)
                    blackjack.reveal_player_hand(player)
                elif answer == "stand":
                    break
                elif answer == "bust":
                    time.sleep(1)
                    blackjack.reveal_player_hand(player)
                    print "Awe, bust!"
                    dealer_plays = False
                    break
                elif answer == "win":
                    time.sleep(1)
                    blackjack.reveal_player_hand(player)
                    print "Blackjack!"
                    break
                elif answer == "error":
                    print "Does not compute. Please type hit or stand."

        #Dealer plays
        if dealer_plays:
            time.sleep(1)
            print "\nDealer's turn:\n"
            time.sleep(.5)
            blackjack.reveal_dealer_full_hand(dealer)
            while True:
                house_move = blackjack.hit_or_stand_for_the_dealer(dealer, deck)
                if house_move == "hit" or house_move  == "bust" or house_move == "win":
                    time.sleep(1)
                    print "Dealer takes another card.\n"
                    time.sleep(1)
                    blackjack.reveal_dealer_full_hand(dealer)

                if house_move == "stand":
                    time.sleep(1)
                    print "Dealer stands."
                    break
                elif house_move == "bust":
                    time.sleep(1)
                    print "Woo hoo! Dealer busts!"
                    break
                elif house_move == "win":
                    time.sleep(1)
                    print "Snap! Dealer Blackjack!"
                    break

        #Determine winner
        compare = blackjack.determine_winner(player, dealer)
        if compare == "player":
            time.sleep(.7)
            print "Your hand is higher. You win!"
        elif compare == "dealer":
            time.sleep(.7)
            print "Dealer's hand is higher. Dealer wins."
        elif compare == "tie":
            time.sleep(.7)
            print "Scores are the same. Tie!"

        #Play again or quit
        choice = raw_input("\nDo you want to play again? ")
        if choice.lower() == "yes" or choice.lower() == "y":
            continue
        else:
            time.sleep(.5)
            print "\nThanks for playing!\n"
            break

#Main code here

main()
