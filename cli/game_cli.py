from app.engine.game import Game

# Game Display
def game_start_screen(game_number, games_to_play):
        print()
        print("*" * 30)
        print(f"Game {game_number} of {games_to_play}")
        print("*" * 30)

def show_game_state(game, show_all_dealer_cards=False):
    print(game.player_hand.display())
    print(game.dealer_hand.display(show_all_dealer_cards))

def end_game_result_screen(game):
    print("Final Results")
    print("Your Hand:", game.player_hand.get_value())
    print("Dealer Hand:", game.dealer_hand.get_value())

def final_message():
    print("\nThanks for Playing!")

def display_result(game, result):
        end_game_result_screen(game)
        print()
        print(result)

def handle_player_turn(game):
    while game.player_hand.get_value() < 21:

        choice = input("Hit (h) or Stand (s)? ").lower()

        if choice in ["h", "hit"]:
            game.player_hit()
            print(game.player_hand.display())

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


def play():
    game = Game()

    games_to_play = game_count()

    for game_number in range(1, games_to_play + 1):

        # --- Initialise Game ---

        game.reset_game()

        game_start_screen(game_number, games_to_play)

        game.initial_deal()

        show_game_state(game)

        result = game.check_initial_result()

        if game.evaluate_result(result):
            display_result(game, result)
            continue

        # --- Player Turn ---
        handle_player_turn(game)

        result = game.check_bust_condition()

        if game.evaluate_result(result):
            continue

        # --- Dealer Turn ---
        game.dealer_turn()

        game.dealer_show_cards()

        result = game.check_bust_condition()

        if game.evaluate_result(result):
            display_result(game, result)
            continue

        # --- Final Result ---
        result = game.check_final_condition()

        if game.evaluate_result(result):
            display_result(game, result)
            continue

    final_message()

if __name__ == "__main__":
    play()