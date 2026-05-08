from game_logic import check_winner
from hand import Hand
from deck import Deck

class Game:
    def play(self):

        games_to_play = int(input("How many games? "))
        game_number = 0

        while game_number < games_to_play:
            game_number += 1

            deck = Deck()
            deck.shuffle()

            player = Hand()
            dealer = Hand(dealer=True)

            for _ in range(2):
                player.add_card(deck.deal(1))
                dealer.add_card(deck.deal(1))

            print()
            print("*" * 30)
            print(f"Game {game_number} of {games_to_play}")
            print("*" * 30)
            print(player.display())
            print(dealer.display())

            # --- early check ---
            result = check_winner(player, dealer)
            if result:
                print(result)
                continue

            # --- player turn ---
            while player.get_value() < 21:
                choice = input("Hit or Stand? ").lower()

                if choice in ["h", "hit"]:
                    player.add_card(deck.deal(1))
                    print(player.display())
                else:
                    break

            result = check_winner(player, dealer)
            if result:
                print(result)
                continue

            # --- dealer turn ---
            while dealer.get_value() < 17:
                dealer.add_card(deck.deal(1))

            print(dealer.display(True))

            # --- final result ---
            player_hand_value = player.get_value()
            dealer_hand_value = dealer.get_value()
            print("Final Results")
            print("Your Hand:", player_hand_value)
            print("Dealer Hand:", dealer_hand_value)
            result = check_winner(player, dealer, True)
            print(result)

        print("\n Thanks for Playing!")
        
g = Game()
g.play()