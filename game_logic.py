def check_winner(player_hand, dealer_hand, game_over=False):
        if not game_over:      
            if player_hand.get_value() > 21:
                return "You bust dealer wins!"

            elif dealer_hand.get_value() > 21:
                return "Dealer bust player wins!"

            elif player_hand.is_blackjack() and dealer_hand.is_blackjack():
                return "It's a Tie!"

            elif player_hand.is_blackjack() and not dealer_hand.is_blackjack():
                return "You have a blackjack, you WIN!"

            elif dealer_hand.is_blackjack() and not player_hand.is_blackjack():
                return "Dealer has a blackjack, you Lose!"

        else:
            if player_hand.get_value() > dealer_hand.get_value():
                return "You Win!"
            elif player_hand.get_value() == dealer_hand.get_value():
                return "TIE!"
            else:
                return "Dealer Win!"
        return False