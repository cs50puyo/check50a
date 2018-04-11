import random

# generate a number betwen 1 and 13 inclusive for the rank
random_rank = random.randrange(1, 14)
# generate a number betwen 0 and 3 inclusive for the suit
random_suit = random.randrange(4)

if random_rank == 1:
    rank = 'Ace'
elif 2 <= random_rank <= 10:
    rank = str(random_rank)
elif random_rank == 11:
    rank = 'Jack'
elif random_rank == 12:
    rank = 'Queen'
else:
    rank = 'King'

if random_suit == 0:
    suit = 'Clubs'
elif random_suit == 1:
    suit  = 'Diamonds'
elif random_suit == 2:
    suit = 'Hearts'
else:
    suit = 'Spades'

print('The card you picked is the {} of {}'.format(rank, suit))
