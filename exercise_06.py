import random

card_number = random.randrange(13)

if card_number == 0:
    card = "As"
elif card_number == 1:
    card = 2
elif card_number == 2:
    card = 3
elif card_number == 3:
    card = 4
elif card_number == 4:
    card = 5
elif card_number == 5:
    card = 6
elif card_number == 6:
    card = 7
elif card_number == 7:
    card = 8
elif card_number == 8:
    card = 9
elif card_number == 9:
    card = 10
elif card_number == 10:
    card = "Jack"
elif card_number == 11:
    card = "Queen"
else:
    card = "King"

type_card = random.randrange(4)

if type_card == 0:
    hand = "Clubs"
if type_card == 0:
    hand = "Diamonds"
if type_card == 0:
    hand = "Hearts"
else:
    hand = "Spades"

print("The card you picked is the", card, "of", hand)
