def check_winner(player_hand, dealer_hand, game_over=False):
        if not game_over:      
            if player_hand.get_value() > 21:
                print("You bust dealer wins!")
                return True
            elif dealer_hand.get_value() > 21:
                print("Dealer bust player wins!")
                return True
            elif player_hand.is_blackjack() and dealer_hand.is_blackjack():
                print("It's a Tie!")
                return True
            elif player_hand.is_blackjack() and not dealer_hand.is_blackjack():
                print("You have a blackjack, you WIN!")
                return True
            elif dealer_hand.is_blackjack() and not player_hand.is_blackjack():
                print("Dealer has a blackjack, you Lose!")
                return True
        else:
            if player_hand.get_value() > dealer_hand.get_value():
                print("You Win!")
            elif player_hand.get_value() == dealer_hand.get_value():
                print("TIE!")
            else:
                print("Dealer Win!")
            return True
        return False