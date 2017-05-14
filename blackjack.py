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

#def dealer_plays():
    #pass

def get_menu_choice():
    """Print a menu and asks the user to make a choice.
    Arguments:
      None
    Returns:
      int: the user's menu choice
    """
    print '\n  0 - Main Menu'
    print '    1 - Start game/Deal hand'
    print '    2 - Player hit or stand'
    print '    3 - Dealer plays'
    print '    4 - Determine winner'
    #print '    2 - Display high scores'
    #print '    3 - Add score to high scores'
    print '    5 - Exit the program.\n'

    choice = int(raw_input('Choose from the menu options: '))

    return choice

def execute_repl(deck):
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
            shuffle(deck)
            deal(deck, player)
            deal(deck, dealer)
            deal(deck, player)
            deal(deck, dealer)

            print assess_score(player)

        elif choice == 3:
            # dealer plays; must hit if under 17
            print assess_score(dealer)

        elif choice == 5:
            # quit
            break

        # else:
        #
        #     # all of the remaning choices require an existing list. First, run
        #     # code to get the list name from the user and verify it exists in
        #     # the dict
        #
        #     # determine which list
        #     list_name = raw_input('Which list would you like to see? ')
        #
        #     # test to see if the list is in the shopping list dict
        #     if list_name not in shopping_lists_by_name:
        #         # no list by this name :-(
        #         print 'There is no {} list.'.format(list_name)
        #         continue
        #
        #     # if the code reaches this point, it means the list exists in the
        #     # dictionary, so proceed according to which choice was chosen
        #
        #     if choice == 2:
        #         # show a specific list
        #
        #         display_shopping_list(shopping_lists_by_name, list_name)
        #
        #     elif choice == 4:
        #         # Add item(s) to a shopping list
        #
        #         # add items to the shopping list
        #         edit_shopping_list(shopping_lists_by_name, list_name, 'add')
        #
        #     elif choice == 5:
        #         # Remove an item from a shopping list
        #
        #         # add items to the shopping list
        #         edit_shopping_list(shopping_lists_by_name, list_name, 'remove')
        #
        #     elif choice == 6:
        #         # remove list
        #
        #         remove_shopping_list(shopping_lists_by_name, list_name)


#intial calls

# deck = make_new_deck()
# shuffle(deck)
# player = []
# dealer = []
# deal(deck, player)
# deal(deck, dealer)
# deal(deck, player)
# deal(deck, dealer)
# print assess_score(player)
#print assess_score(dealer)

deck = make_new_deck()
player = []
dealer = []
execute_repl(deck)
