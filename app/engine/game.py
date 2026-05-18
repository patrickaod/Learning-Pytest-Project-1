from app.engine.game_logic import CheckLogic
from app.models.hand import Hand
from app.models.deck import Deck

class Game:
    # Game State
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

    def game_count(self):
        while True:
            try:
                games_to_play = int(input("How many games? "))

                if games_to_play > 0:
                    return games_to_play

                print("Please enter a number greater than 0")

            except ValueError:
                print("Please enter a valid number")

    #Game Evaluation
    def check_initial_result(self):
        return CheckLogic.check_initial_dealt_hand_result(
            self.player_hand,
            self.dealer_hand
        )

    def check_bust_condition(self):
        return CheckLogic.check_immediate_result(
            self.player_hand,
            self.dealer_hand
        )

    def check_final_condition(self):
        return CheckLogic.check_final_result(
            self.player_hand,
            self.dealer_hand
        )
    
    def evaluate_result(self, result):
        if result:
            self.display_result(result)
            return True
        return False

    # Game Display
    def game_start_screen(self, game_number, games_to_play):
            print()
            print("*" * 30)
            print(f"Game {game_number} of {games_to_play}")
            print("*" * 30)

    def show_game_state(self, show_all_dealer_cards=False):
        print(self.player_hand.display())
        print(self.dealer_hand.display(show_all_dealer_cards))

    def end_game_result_screen(self):
        print("Final Results")
        print("Your Hand:", self.player_hand.get_value())
        print("Dealer Hand:", self.dealer_hand.get_value())
    
    def final_message(self):
        print("\nThanks for Playing!")

    def display_result(self, result):
            self.end_game_result_screen()
            print()
            print(result)

    #Player State
    def handle_player_turn(self):
        while self.player_hand.get_value() < 21:

            choice = input("Hit or Stand? ").lower()

            if choice in ["h", "hit"]:
                self.player_hit()
                print(self.player_hand.display())

            elif choice in ["s", "stand"]:
                break

            else:
                print("Please enter Hit or Stand")

    def player_hit(self):
        self.player_hand.add_card(self.deck.deal(1))

    #Dealer State
    def dealer_turn(self):
        while self.dealer_hand.get_value() <= 17:
            self.dealer_hand.add_card(self.deck.deal(1))
    
    def dealer_show_cards(self):
        print(self.dealer_hand.display(True))

    #Game Engine
    def play(self):

        games_to_play = self.game_count()
        game_number = 0

        while game_number < games_to_play:
            game_number += 1

            # reset state
            self.reset_game()

            self.game_start_screen(game_number, games_to_play)

            self.initial_deal()

            self.show_game_state()

            result = self.check_initial_result()

            if self.evaluate_result(result):
                continue

            # --- player turn ---
            self.handle_player_turn()

            result = self.check_bust_condition()

            if self.evaluate_result(result):
                continue

            # --- dealer turn ---
            self.dealer_turn()

            self.dealer_show_cards()

            result = self.check_bust_condition()

            if self.evaluate_result(result):
                continue

            # --- final result ---
            result = self.check_final_condition()

            if self.evaluate_result(result):
                continue

        self.final_message()

g = Game()
g.play()