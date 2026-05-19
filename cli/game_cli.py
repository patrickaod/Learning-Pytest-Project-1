# Game Display
class Cli:
    def game_start_screen(self, game_number, games_to_play):
            print()
            print("*" * 30)
            print(f"Game {game_number} of {games_to_play}")
            print("*" * 30)

    def show_game_state(self, game, show_all_dealer_cards=False):
        print(self.display(game.player_hand))
        print(self.display(game.dealer_hand, show_all_dealer_cards))

    def end_game_result_screen(self, game):
        print("Final Results")
        print("Your Hand:", game.player_hand.get_value())
        print("Dealer Hand:", game.dealer_hand.get_value())

    def final_message(self):
        print("\nThanks for Playing!")

    def display_result(self, game, result):
            self.end_game_result_screen(game)
            print()
            print(result)

    def handle_player_turn(self, game):
        while game.player_hand.get_value() < 21:

            choice = input("Hit (h) or Stand (s)? ").lower()

            if choice in ["h", "hit"]:
                game.player_hit()
                print(self.display(game.player_hand))

            elif choice in ["s", "stand"]:
                break

            else:
                print("Please enter Hit or Stand")

    def game_count(self):
        while True:
            try:
                games_to_play = int(input("How many games? "))

                if games_to_play > 0:
                    return games_to_play

                print("Please enter a number greater than 0")

            except ValueError:
                print("Please enter a valid number")

    def dealer_show_cards(self, game):
        print(self.display(game.dealer_hand, True))

    def display(self, hand, show_all_dealer_cards=False):

        output = f'''{"Dealer's" if hand.dealer else "Your"} Hand: \n'''

        for index, card in enumerate(hand.cards):

            if index == 0 and hand.dealer and not show_all_dealer_cards and not hand.is_blackjack():
                output += "Hidden\n"

            else:
                output += f"{card}\n"

        if not hand.dealer:
            output += f"Value: {hand.get_value()}\n"

        return output