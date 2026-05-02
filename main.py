from game_logic import check_winner
from hand import Hand
from deck import Deck

class game:
    def play(self):
        game_number = 0
        games_to_play = 0

        while games_to_play <= 0:
            try:
                games_to_play = int(input("How many games do you want to play? "))
            except:
                print("You have to enter a number")

        while game_number < games_to_play:
            game_number += 1

            deck1 = Deck()
            deck1.shuffle()

            player_hand = Hand()
            dealer_hand = Hand(dealer=True)

            for i in range(2):
                player_hand.add_card(deck1.deal(1))
                dealer_hand.add_card(deck1.deal(1))

            print()
            print("*" * 30)
            print(f"Game {game_number} of {games_to_play}")
            print("*" * 30)
            print(player_hand.display())  
            print(dealer_hand.display())  
            

            if check_winner(player_hand, dealer_hand):
                continue

            choice = ""
            while player_hand.get_value() < 21 and choice not in ["s", "stand"]:
                choice = input("Please choice Hit or Stand? ").lower()
                print()
                while choice not in ["h", "hit", "s", "stand"]:
                    choice = input("Please choice Hit(h) or Stand(s)? ").lower()
                    print()
                if choice in ["h", "hit"]:
                    player_hand.add_card(deck1.deal(1))
                    print(player_hand.display())  

            if check_winner(player_hand, dealer_hand):
                continue

            player_hand_value = player_hand.get_value()
            dealer_hand_value = dealer_hand.get_value()

            while dealer_hand_value < 17:
                dealer_hand.add_card(deck1.deal(1))
                dealer_hand_value = dealer_hand.get_value()

            dealer_hand.display(show_all_dealer_cards=True)

            if check_winner(player_hand, dealer_hand):
                continue

            print("Final Results")
            print("Your Hand:", player_hand_value)
            print("Dealer Hand:", dealer_hand_value)

            check_winner(player_hand, dealer_hand, True)
        
        print("\n Thanks for Playing!")
        
g = game()
g.play()