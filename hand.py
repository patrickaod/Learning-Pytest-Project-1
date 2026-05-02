class Hand:
    def __init__(self, dealer=False):
        self.cards = []
        self.valve = 0
        self.dealer = dealer

    def add_card(self, card_list):
        self.cards.extend(card_list)

    def calculate_value(self):
        self.value = 0
        has_ace = False

        for card in self.cards:
            card_value = int(card.rank["value"])
            self.value += card_value
            if card.rank["rank"] == "A":
                has_ace = True

        if has_ace and self.value > 21:
            self.value -= 10

    def get_value(self):
        self.calculate_value()
        return self.value

    def is_blackjack(self):
        return self.get_value()==21

    def display(self, show_all_dealer_cards=False):
        output = f'''{"Dealer's" if self.dealer else "Your"} Hand: \n'''

        for index, card in enumerate(self.cards):
            if index == 0 and self.dealer and not show_all_dealer_cards and not self.is_blackjack():
                output += "Hidden\n"
            else:
                output += f"{card}\n"

        if not self.dealer:
            output += f"Value: {self.get_value()}\n"

        return output
