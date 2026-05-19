from app.engine.game import Game

# Game Display
class Cli:
    def game_start_screen(game_number, games_to_play):
            print()
            print("*" * 30)
            print(f"Game {game_number} of {games_to_play}")
            print("*" * 30)

    def show_game_state(game, show_all_dealer_cards=False):
        print(Cli.display(game.player_hand))
        print(Cli.display(game.dealer_hand, show_all_dealer_cards))

    def end_game_result_screen(game):
        print("Final Results")
        print("Your Hand:", game.player_hand.get_value())
        print("Dealer Hand:", game.dealer_hand.get_value())

    def final_message():
        print("\nThanks for Playing!")

    def display_result(game, result):
            Cli.end_game_result_screen(game)
            print()
            print(result)

    def handle_player_turn(game):
        while game.player_hand.get_value() < 21:

            choice = input("Hit (h) or Stand (s)? ").lower()

            if choice in ["h", "hit"]:
                game.player_hit()
                print(Cli.display(game.player_hand))

            elif choice in ["s", "stand"]:
                break

            else:
                print("Please enter Hit or Stand")

    def game_count():
        while True:
            try:
                games_to_play = int(input("How many games? "))

                if games_to_play > 0:
                    return games_to_play

                print("Please enter a number greater than 0")

            except ValueError:
                print("Please enter a valid number")

    def dealer_show_cards(game):
        print(Cli.display(game.dealer_hand, True))

    def display(game, show_all_dealer_cards=False):
        output = f'''{"Dealer's" if game.dealer else "Your"} Hand: \n'''

        for index, card in enumerate(game.cards):
            if index == 0 and game.dealer and not show_all_dealer_cards and not game.is_blackjack():
                output += "Hidden\n"
            else:
                output += f"{card}\n"

        if not game.dealer:
            output += f"Value: {game.get_value()}\n"

        return output
# --- Main Game Function ---
def play():
    game = Game()

    games_to_play = Cli.game_count()

    for game_number in range(1, games_to_play + 1):

        # --- Initialise Game ---

        game.reset_game()

        Cli.game_start_screen(game_number, games_to_play)

        game.initial_deal()

        Cli.show_game_state(game)

        result = game.check_initial_result()

        if game.evaluate_result(result):
            Cli.display_result(game, result)
            continue

        # --- Player Turn ---
        Cli.handle_player_turn(game)

        result = game.check_bust_condition()

        if game.evaluate_result(result):
            Cli.display_result(game, result)
            continue

        # --- Dealer Turn ---
        game.dealer_turn()

        Cli.dealer_show_cards(game)

        result = game.check_bust_condition()

        if game.evaluate_result(result):
            Cli.display_result(game, result)
            continue

        # --- Final Result ---
        result = game.check_final_condition()

        if game.evaluate_result(result):
            Cli.display_result(game, result)
            continue

    Cli.final_message()

if __name__ == "__main__":
    play()