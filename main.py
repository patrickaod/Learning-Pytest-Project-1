from game_logic import check_winner
from hand import Hand
from deck import Deck

class Game:
    def play(self):

        while True:
            try:
                games_to_play = int(input("How many games? "))
                if games_to_play > 0:
                    break
            except ValueError:
                print("Please enter a valid number")

        game_number = 0

        while game_number < games_to_play:
            game_number += 1

            deck = Deck()
            deck.shuffle()

            player_hand = Hand()
            dealer_hand = Hand(dealer_hand=True)

            for _ in range(2):
                player_hand.add_card(deck.deal(1))
                dealer_hand.add_card(deck.deal(1))

            print()
            print("*" * 30)
            print(f"Game {game_number} of {games_to_play}")
            print("*" * 30)
            print(player_hand.display())
            print(dealer_hand.display())

            # --- early check ---
            result = check_winner(player_hand, dealer_hand)
            if result:
                print(result)
                continue

            # --- player_hand turn ---
            
            while player_hand.get_value() < 21:
                choice = input("Hit or Stand? ").lower()

                if choice in ["h", "hit"]:
                    player_hand.add_card(deck.deal(1))
                    print(player_hand.display())

                elif choice in ["s", "stand"]:
                    break

                else:
                    print("Please enter Hit or Stand")

            result = check_winner(player_hand, dealer_hand)
            if result:
                print(result)
                continue

            # --- dealer turn ---
            while dealer_hand.get_value() <= 17:
                dealer_hand.add_card(deck.deal(1))

            print(dealer_hand.display(True))

            # --- final result ---
            player_hand_value = player_hand.get_value()
            dealer_hand_value = dealer_hand.get_value()
            print("Final Results")
            print("Your Hand:", player_hand_value)
            print("Dealer Hand:", dealer_hand_value)
            result = check_winner(player_hand, dealer_hand, True)
            print(result)

        print("\n Thanks for Playing!")
        
g = Game()
g.play()