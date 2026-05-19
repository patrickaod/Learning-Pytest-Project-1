from app.engine.game import Game
from cli import Cli

class GameRunner:

    def __init__(self):
        self.cli = Cli()
        self.game = Game()

    # --- Main Game Function ---
    def run(self):

        games_to_play = self.cli.game_count()

        for game_number in range(1, games_to_play + 1):

            # --- Initialise Game ---

            self.game.reset_game()

            self.cli.game_start_screen(game_number, games_to_play)

            self.game.initial_deal()

            self.cli.show_game_state(self.game)

            result = self.game.check_initial_result()

            if self.game.evaluate_result(result):
                self.cli.display_result(self.game, result)
                continue

            # --- Player Turn ---
            self.cli.handle_player_turn(self.game)

            result = self.game.check_bust_condition()

            if self.game.evaluate_result(result):
                self.cli.display_result(self.game, result)
                continue

            # --- Dealer Turn ---
            self.game.dealer_turn()

            self.cli.dealer_show_cards(self.game)

            result = self.game.check_bust_condition()

            if self.game.evaluate_result(result):
                self.cli.display_result(self.game, result)
                continue

            # --- Final Result ---
            result = self.game.check_final_condition()

            if self.game.evaluate_result(result):
                self.cli.display_result(self.game, result)
                continue

        self.cli.final_message()