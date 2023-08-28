import random
deck_of_cards = []
suites = ["Diamonds", "Hearts", "Clubs", "Spades"]
card_value = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]

for x in card_value:
    for y in suites:
        deck_of_cards.append(x + " of " + y)

random.shuffle(deck_of_cards)

def card_value(card):
    color = ""
    num_value = 0
    suite = ""
    if "Hearts" in card:
        color = "Red"
        suite = "Hearts"
    elif "Diamonds" in card:
        color = "Red"
        suite = "Diamonds"
    elif "Spades" in card:
        color = "Black"
        suite = "Spades"
    elif "Clubs" in card:
        color = "Black"
        suite = "Clubs"
    else:
        "Card is not recognized"
    if "King" in card:
        num_value = 13
    elif "Queen" in card:
        num_value = 12
    elif "Jack" in card:
        num_value = 11
    elif "Ace" in card:
        num_value = 1
    else:
        num_value = int(card[0])
    return color, num_value, suite

card_index = 0
card_in_play = deck_of_cards[card_index]
card_des = card_value(card_in_play)

first_guess = input("Red or Black")

if first_guess == card_des[0]:
    print("Correct!")
    print(card_in_play)
    card_index += 1
else:
   print("Incorrect")
   print(card_in_play)
   card_index += 1

print(card_in_play)
print(card_index)    