from game_logic import check_winner
from hand import Hand
from deck import Deck

class Game:

    def __init__(self):
        self.reset_game()

    def reset_game(self):
        self.deck = Deck()
        self.deck.shuffle()
        self.player_hand = Hand()
        self.dealer_hand = Hand(dealer=True)
        self.game_over = False
    
    def initial_deal(self):
        for _ in range(2):
            self.player_hand.add_card(self.deck.deal(1))
            self.dealer_hand.add_card(self.deck.deal(1))

    def player_hit(self):
        self.player_hand.add_card(self.deck.deal(1))

    def dealer_turn(self):
        while self.dealer_hand.get_value() <= 17:
            self.dealer_hand.add_card(self.deck.deal(1))

    def check_result(self, game_over=False):
        return check_winner(
            self.player_hand,
            self.dealer_hand,
            game_over
        )

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

            # reset state
            self.__init__()

            print()
            print("*" * 30)
            print(f"Game {game_number} of {games_to_play}")
            print("*" * 30)

            self.initial_deal()

            print(self.player_hand.display())
            print(self.dealer_hand.display())

            result = self.check_result()

            if result:
                print(result)
                continue

            # --- player turn ---
            while self.player_hand.get_value() < 21:

                choice = input("Hit or Stand? ").lower()

                if choice in ["h", "hit"]:
                    self.player_hit()
                    print(self.player_hand.display())

                elif choice in ["s", "stand"]:
                    break

                else:
                    print("Please enter Hit or Stand")

            result = self.check_result()

            if result:
                print(result)
                continue

            # --- dealer turn ---
            self.dealer_turn()

            print(self.dealer_hand.display(True))

            # --- final result ---
            print("Final Results")
            print("Your Hand:", self.player_hand.get_value())
            print("Dealer Hand:", self.dealer_hand.get_value())

            result = self.check_result(True)

            print(result)

        print("\nThanks for Playing!")
        
g = Game()
g.play()