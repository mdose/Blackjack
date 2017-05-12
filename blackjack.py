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
    #convert face cards to 10 in NEW tuples-->b/c tuples can't be altered! (immutable!)
    #add first part of card tuples together
    #hand -> list of tuples [tuple_1, tuple_2]
        #tuple_1[0] + tuple_2[0] == score
    #have ace be either 1 or 11 depending on total score
    # if card[0] == "jack" or card[0] == "queen" or card[0] == "king":
    #     "jack" = 10
    #     "queen" = 10
    #     "king" = 10
    #face cards = {"jack" : 10, "queen" : 10, "king" :10}
        # ace ->
        # if score <= 10:
        #     {"ace" : 11}
        # else:
        #     {"ace" : 1}
    score = 0
    for card in hand:
        rank = card[0]
        score += rank
    return score

    #score = player[0][0] + player[1][0]

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
#assess_score(player)
#assess_score(dealer)



# execute_repl(deck)


# deck -> list, player -> list, dealer -> list; move itmes from one list to another
