import random

def make_new_deck():
    # returns new deck
    return [
        (2, "diamonds"),
        (3, "diamonds"),
        (4, "diamonds"),
        (5, "diamonds"),
        (6, "diamonds"),
        (7, "diamonds"),
        (8, "diamonds"),
        (9, "diamonds"),
        (10, "diamonds"),
        ("jack", "diamonds"),
        ("queen", "diamonds"),
        ("king", "diamonds"),
        ("ace", "diamonds"),
        (2, "clubs"),
        (3, "clubs"),
        (4, "clubs"),
        (5, "clubs"),
        (6, "clubs"),
        (7, "clubs"),
        (8, "clubs"),
        (9, "clubs"),
        (10, "clubs"),
        ("jack", "clubs"),
        ("queen", "clubs"),
        ("king", "clubs"),
        ("ace", "clubs"),
        (2, "hearts"),
        (3, "hearts"),
        (4, "hearts"),
        (5, "hearts"),
        (6, "hearts"),
        (7, "hearts"),
        (8, "hearts"),
        (9, "hearts"),
        (10, "hearts"),
        ("jack", "hearts"),
        ("queen", "hearts"),
        ("king", "hearts"),
        ("ace", "hearts"),
        (2, "spades"),
        (3, "spades"),
        (4, "spades"),
        (5, "spades"),
        (6, "spades"),
        (7, "spades"),
        (8, "spades"),
        (9, "spades"),
        (10, "spades"),
        ("jack", "spades"),
        ("queen", "spades"),
        ("king", "spades"),
        ("ace", "spades")
    ]

def shuffle(deck):
    # shuffle the deck(list of tuples, each tuple has a rank, and a suit) -> returns None
    random.shuffle(deck)

def deal(deck, hand):
    # remove first four cards; one to player (list); one to dealer(list); repeat -> returns None
    hand.append(deck.pop(0))
    ## Orginial version below:
    # top_card = deck[0]
    # deck.remove(top_card)
    # hand.append(top_card)

def assess_score(hand):
    score = 0
    sorted_hand = sorted(hand, key=lambda card: determine_numeric_value(card, 0))
    for card in sorted_hand:
        score += determine_numeric_value(card, score)
    return score

def determine_numeric_value(card, score):
    #write a func that takes 1 card(tuple) as a parameter and returns numeric value
    rank = card[0]
    if rank == "jack" or rank == "queen" or rank == "king":
        return 10
    elif rank == "ace":
        return determine_ace_value(score)
    else:
        return rank

def determine_ace_value(score):
    if score <= 10:
        return 11
    else:
        return 1

def reveal_player_hand(player):
    for card in player:
        print "You have a " + str(card[0]) + " of " + card[1] + "."
    print "\nYour score is: " + str(assess_score(player)) + "."

def reveal_dealer_faceup_card(dealer):
    print "\nDealer has a " + str(dealer[0][0]) + " of " + str(dealer[0][1]) + "."

def hit_or_stand(player, deck):
    next_move = raw_input("\nDo you want to hit or stand? ").lower()
    if next_move == "hit":
        deal(deck, player)
        return determine_if_bust(player)
    elif next_move == "stand":
        return "stand"
    else:
        return "error"

def determine_if_bust(hand):
    if assess_score(hand) > 21:
        return "bust"
    elif assess_score(hand) == 21:
        return "win"
    else:
        return "hit"

def dealer_reveals_full_hand(dealer):
    print "Dealer's turn:"
    for card in dealer:
        print "Dealer has a " + str(card[0]) + " of " + card[1] + "."
    print "\nDealer's score is: " + str(assess_score(dealer)) + "."

def dealer_plays(dealer, deck):
    if assess_score(dealer) <= 16:
        deal(deck, dealer)
        return determine_if_bust(dealer)
    else:
        return "stand"

def get_menu_choice():
    """Print a menu and asks the user to make a choice.
    Arguments:
      None
    Returns:
      int: the user's menu choice
    """
    print '\n    0 - Main Menu'
    print '    1 - Start game'
    #print '    2 - Calculate player score'
    #print '    3 - Player hit or stand'
    #print '    4 - Dealer plays'
    #print '    5 - Determine winner'
    #print '    2 - Display high scores'
    #print '    3 - Add score to high scores'
    print '    6 - Exit the program.\n'

    choice = int(raw_input('Choose from the menu options: '))

    return choice

def execute_repl():
    """Execute the repl loop for the control structure of the program.
    (REPL stands for Read - Eval - Print Loop. For more info:
    https://en.wikipedia.org/wiki/Read%E2%80%93eval%E2%80%93print_loop)
    Arguments:
        deck: list of tuples representing 52 cards in a deck
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
            deck = make_new_deck()
            player = []
            dealer = []
            shuffle(deck)
            deal(deck, player)
            deal(deck, dealer)
            deal(deck, player)
            deal(deck, dealer)
            print "\nHello.\n"
            #answer = raw_input("Do you want to play a game? Yes or No? ")
            #if answer == "yes" or "Yes":
            reveal_player_hand(player)
            reveal_dealer_faceup_card(dealer)
            while True:
                answer = hit_or_stand(player, deck)
                if answer == "hit":
                    reveal_player_hand(player)
                elif answer == "stand":
                    break
                elif answer == "bust":
                    reveal_player_hand(player)
                    print "Awe, bust! You lose!"
                    break
                elif answer == "win":
                    reveal_player_hand(player)
                    print "Blackjack! You win!"
                    break
                elif answer == "error":
                    print "Does not compute. Please type hit or stand."
            dealer_reveals_full_hand(dealer)
            while True:
                house_score = dealer_plays(dealer, deck)
                if house_score == "hit":
                    dealer_reveals_full_hand(dealer)
                elif house_score == "stand":
                    break
                elif house_score == "bust":
                    dealer_reveals_full_hand(dealer)
                    print "Dealer busts! You win!"
                    break
                elif house_score == "win":
                    dealer_reveals_full_hand(dealer)
                    print "Dealer Blackjack! You lose!"
                    break


        # elif choice == 3:
        #     # dealer plays; must hit if under 17
        #     print assess_score(dealer)

        elif choice == 6:
            # quit
            break

#Main code here

execute_repl()
