import random
import time

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
    """Removes first tuple(card) from the list(deck) and adds tuple(card) to the provided list(hand).
    Arguments:
      deck: list of 52 tuples
      hand: list belonging to the player or the dealer
    Returns:
      None
    """

    hand.append(deck.pop(0))

    ## Orginial version below:
    # top_card = deck[0]
    # deck.remove(top_card)
    # hand.append(top_card)

def assess_score(hand):
    """Calculates the sum(score) of the tuples(cards) within a list(hand).
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

def determine_numeric_value(card, current_score):
    """Finds numeric value of any card, including facecards and aces; called in the assess_score func.
    Arguments:
      card: a tuple that consists of a rank and a suit
      current_score: current sum of all tuples seen so far
    Returns:
      int: the numeric value of a tuple(card)
    """

    rank = card[0]
    if rank == "jack" or rank == "queen" or rank == "king":
        return 10
    elif rank == "ace":
        return determine_ace_value(current_score)
    else:
        return rank

def determine_ace_value(current_score):
    """Assures the correct numeric value of any ace given the current_score; called in the determine_numeric_value func.
    Arguments:
      current_score: current sum of all tuples seen so far
    Returns:
      int: the numeric value of an ace (1 or 11) based on the sum(current_score) of all cards in the list(hand).
    """

    if current_score <= 10:
        return 11
    else:
        return 1

def reveal_player_hand(player):
    """Loops through the player's list(hand) and prints each tuple(card) and the sum(score) in an easy to read format.
    Arguments:
        player: list of all tuples(cards) held by the player
    Returns:
        None; func only prints.
    """

    print ""
    for card in player:
        time.sleep(.5)
        print "You have a " + str(card[0]) + " of " + card[1] + "."
    time.sleep(1)
    print "\nYour score is: " + str(assess_score(player)) + ".\n"

def reveal_dealer_faceup_card(dealer):
    """Prints the first tuple(card) of the dealer's list(hand) in an easy to read format.
    Arguments:
        dealer: list of all tuples(cards) held by the dealer
    Returns:
        None; func only prints.
    """
    time.sleep(1)
    print "Dealer has a " + str(dealer[0][0]) + " of " + str(dealer[0][1]) + ".\n"

def reveal_dealer_full_hand(dealer):
    """Loops through the dealer's list(hand) and prints each tuple(card) and the sum(score) in an easy to read format.
    Arguments:
        dealer: list of all tuples(cards) held by the dealer
    Returns:
        None; func only prints.
    """

    for card in dealer:
        time.sleep(.5)
        print "Dealer has a " + str(card[0]) + " of " + card[1] + "."
    time.sleep(1)
    print "\nDealer's score is: " + str(assess_score(dealer)) + ".\n"

def hit_or_stand(player, deck, next_move):
    """Takes raw input from the player and parses the response to determine their next move, peforms the move, and returns the move taken.
    Arguments:
        player: list of all tuples(cards) held by the player
        deck: list of tuples(card) left to choose from
        next_move: string; user's raw_input
    Returns:
        str: the next move taken
    """

    if next_move == "hit":
        deal(deck, player)
        return determine_if_bust_or_blackjack(player)
    elif next_move == "stand":
        return "stand"
    else:
        return "error"

def determine_if_bust_or_blackjack(hand):
    """Calucalates the sum(score) of a list(hand), determines if the next move is affected by the sum(score), and returns the next move taken.
    Arguments:
        hand: list belonging to the player or the dealer
    Returns:
        str: the next move taken
    """

    if assess_score(hand) > 21:
        return "bust"
    elif assess_score(hand) == 21:
        return "win"
    else:
        return "hit"

def hit_or_stand_for_the_dealer(dealer, deck):
    """ Calucalates the sum(score) of the list(dealer).
        Dealer must hit if the sum(score) is below 17.
        Func determines which move the dealer has to take, performs the move, and returns the move taken.
    Arguments:
        dealer: list of all tuples(cards) held by the dealer
        deck: list of tuples(card) left to choose from
    Returns:
        str: the next move taken
    """

    if assess_score(dealer) <= 16:
        deal(deck, dealer)
        return determine_if_bust_or_blackjack(dealer)
    else:
        return "stand"

def determine_winner(player, dealer):
    """Compares final sum(score) of player with final sum(score) of dealer, determines winner or if game is a tie.
    Arguments:
        player: list of all tuples(cards) held by the player
        dealer: list of all tuples(cards) held by the dealer
    Returns:
        str: the named winner or tie declared
    """

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
