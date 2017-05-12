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
    # remove first four cards; one to player (list); one to dealer(list); repeat
    hand.append(deck.pop(0))
    ## Orginial version below:
    # top_card = deck[0]
    # deck.remove(top_card)
    # hand.append(top_card)

def assess_score(hand):
    score = 0
    for card in hand:
        score += determine_numeric_value_of_card(card)
    return score

def determine_numeric_value_of_card(card):
    #write a func that takes 1 card(tuple) as a parameter and returns numeric value
    rank = card[0]
    if rank == "jack" or rank == "queen" or rank == "king":
        return 10
    elif rank == "ace":
        return 11
    #TODO fix fluxatating ace value
    else:
        return rank

#def hit():
    #pass

#def dealer_plays():
    #pass

def execute_repl(deck):
    #user interface (menu choices)
    pass

deck = make_new_deck()
shuffle(deck)
player = []
dealer = []
deal(deck, player)
deal(deck, dealer)
deal(deck, player)
deal(deck, dealer)
print assess_score(player)
print assess_score(dealer)



# execute_repl(deck)


# deck -> list, player -> list, dealer -> list; move itmes from one list to another
