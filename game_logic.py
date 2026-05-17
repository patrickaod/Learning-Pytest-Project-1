class Check_Logic:
    def check_intial_dealt_hand_result(player_hand, dealer_hand):   
        if player_hand.is_blackjack() and dealer_hand.is_blackjack():
            return "It's a Tie!"

        if player_hand.is_blackjack() and not dealer_hand.is_blackjack():
            return "You have a blackjack, you WIN!"

        if dealer_hand.is_blackjack() and not player_hand.is_blackjack():
            return "Dealer has a blackjack, you Lose!"

    def check_immediate_result(player_hand, dealer_hand):
        if player_hand.get_value() > 21:
            return "You bust dealer wins!"
        
        if dealer_hand.get_value() > 21:
            return "Dealer bust player wins!"

    def check_final_result(player_hand, dealer_hand):     
        if player_hand.get_value() > dealer_hand.get_value():
            return "You Win!"
        if player_hand.get_value() == dealer_hand.get_value():
            return "TIE!"
        if dealer_hand.get_value() > player_hand.get_value():
            return "Dealer Win!"