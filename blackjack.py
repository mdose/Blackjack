import random

def make_new_deck():
    """Creates an unshuffled deck of cards.
    Arguments:
      None
    Returns:
      List of 52 tuples representing a deck of cards; each tuple has a rank and a suit.
    """

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
    """Shuffle the deck; each shuffle should be unqiue.
    Arguments:
      deck: list of 52 tuples
    Returns:
      None
    """

    random.shuffle(deck)

def deal(deck, hand):
    """Removes first card from the deck and adds card to a new list(hand).
    Arguments:
      deck: list of 52 tuples
      hand: new list belonging to the player or the dealer
    Returns:
      None
    """

    hand.append(deck.pop(0))

    ## Orginial version below:
    # top_card = deck[0]
    # deck.remove(top_card)
    # hand.append(top_card)

def assess_score(hand):
    """Calculates the score(int) of the "cards" (tuples) within a list(hand).
    Arguments:
      hand: list belonging to the player or the dealer
    Returns:
      int(score): the sum of all tuples in the list
    """

    score = 0
    sorted_hand = sorted(hand, key=lambda card: determine_numeric_value(card, 0))
    for card in sorted_hand:
        score += determine_numeric_value(card, score)
    return score

    # sorted_hand insures that the ace is always calucated last.
    # With sorted_hand, the correct score is calucated no matter how many cards are added to the list(hand).

def determine_numeric_value(card, score):
    """Finds numeric value of facecards and aces; called in the assess_score func.
    Arguments:
      card: a tuple that consists of a rank and a suit
      score: interger which is the value of the tuple's rank
    Returns:
      int: the numeric value of a card (index[0]), facecard (10) or an ace (1 or 11)
    """

    rank = card[0]
    if rank == "jack" or rank == "queen" or rank == "king":
        return 10
    elif rank == "ace":
        return determine_ace_value(score)
    else:
        return rank
    #may want the parameter of score to be called something else to avoid confusion

def determine_ace_value(score):
    """Finds numeric value of any aces; called in the determine_numeric_value func.
    Arguments:
      score: interger which is the sum of all tuples in the list
    Returns:
      int: the numeric value of an ace (1 or 11) based on the score(sum) of all cards in the hand.
    """

    if score <= 10:
        return 11
    else:
        return 1

def reveal_player_hand(player):
    for card in player:
        print "You have a " + str(card[0]) + " of " + card[1] + "."
    print "\nYour score is: " + str(assess_score(player)) + ".\n"

def reveal_if_natural_blackjack(player, dealer):
    if assess_score(player) == 21:
        print "Instant Blackjack! You win!"
    elif assess_score(dealer) == 21:
        print "Instant Blackjack. Dealer wins."

def reveal_dealer_faceup_card(dealer):
    print "Dealer has a " + str(dealer[0][0]) + " of " + str(dealer[0][1]) + ".\n"

def hit_or_stand(player, deck):
    next_move = raw_input("Do you want to hit or stand? ").lower()
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
    for card in dealer:
        print "Dealer has a " + str(card[0]) + " of " + card[1] + "."
    print "\nDealer's score is: " + str(assess_score(dealer)) + ".\n"

def dealer_plays(dealer, deck):
    if assess_score(dealer) <= 16:
        deal(deck, dealer)
        return determine_if_bust(dealer)
    else:
        return "stand"

def determine_winner(player, dealer):
    #Compare score of player with score of dealer
    player_final_score = assess_score(player)
    dealer_final_score = assess_score(dealer)
    if player_final_score > 21:
        return "dealer"
    elif dealer_final_score > 21:
        return "player"
    elif player_final_score > dealer_final_score:
        return "player"
    elif player_final_score < dealer_final_score:
        return "dealer"
    else:
        return "tie"

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

def execute_repl():
    """Execute the repl loop for the control structure of the program.
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

        elif choice == 2:
             # dealer plays; must hit if under 17
             print "\nDealer's turn:\n"
             dealer_reveals_full_hand(dealer)
             reveal_if_natural_blackjack(player, dealer)
             while True:
                 house_score = dealer_plays(dealer, deck)
                 if house_score == "hit":
                     print "Dealer takes another card.\n"
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

        elif choice == 3:
            player_bust = determine_if_bust(player)
            dealer_bust = determine_if_bust(dealer)
            reveal_player_hand(player)
            dealer_reveals_full_hand(dealer)
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
                compare = determine_winner(player, dealer)
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

execute_repl()
