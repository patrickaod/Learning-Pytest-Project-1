from app.engine.game_logic import CheckLogic
from app.models import Hand, Deck

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

    #Game Evaluation
    def check_initial_result(self):
        return CheckLogic.check_initial_blackjack(
            self.player_hand,
            self.dealer_hand
        )

    def check_bust_condition(self):
        return CheckLogic.check_bust_result(
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

    #Player State

    def player_hit(self):
        self.player_hand.add_card(self.deck.deal(1))

    #Dealer State
    def dealer_turn(self):
        while self.dealer_hand.get_value() <= 17:
            self.dealer_hand.add_card(self.deck.deal(1))
    
    def dealer_show_cards(self):
        print(self.dealer_hand.display(True))