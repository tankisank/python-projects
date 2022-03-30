logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

print(logo)
import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
    return random.choice(cards)
def calculate_score(cards):
    x= sum(cards)
    for item in cards:
        if item==11 and x>21:
            cards.remove(item)
            cards.append(1)
    if(cards==[11,10] or cards==[10,11]):
        return 0
    else:
        return x
def compare(user_score,computer_score):
    if user_score==computer_score:
        print("game is drawn")
    elif user_score>21:
        print("dealer wins")
    elif computer_score>21:
        print("you win")
    else:
        if(user_score>computer_score):
            print("you win")
        else:
            print("dealer wins")
def showcards(user_cards,computer_cards):
    print("1st computer card",computer_cards[0])
    print("user card",user_cards)
cond=True
while cond:
    game=False
    user_cards = []
    computer_cards = []
    user_cards.append(random.choice(cards))
    user_cards.append(random.choice((cards)))
    computer_cards.append(random.choice(cards))
    computer_cards.append(random.choice((cards)))
    showcards(user_cards,computer_cards)
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    while game==False:
        if user_score == 0:
            showcards(user_cards, computer_cards)
            print("you win")
            game = True
            x = input("wanna play again?y/n")
            if (x == 'y'):
                cond = True
            else:
                cond = False
        elif computer_score == 0:
            showcards(user_cards, computer_cards)
            print("dealer wins")
            game = True
            x = input("wanna play again?y/n")
            if (x == 'y'):
                cond = True
            else:
                cond = False
        z = input("want another card?y/n")
        if (z == 'y'):
            user_cards.append(deal_card())
        else:
            game = True
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        while(computer_score<17):
            computer_cards.append(deal_card())
            computer_score = calculate_score(computer_cards)
        compare(user_score, computer_score)
    game = True
    x = input("wanna play again?y/n")
    if (x == 'y'):
        cond = True
    else:
        cond = False












