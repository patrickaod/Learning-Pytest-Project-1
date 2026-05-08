from hand import Hand
from card import Card
from game_logic import check_winner, handle_result

def test_player_bust(player_bust_hand, dealer_low_hand):

    result = check_winner(player_bust_hand, dealer_low_hand)

    assert result == "You bust dealer wins!"

def test_dealer_bust(player_low_hand, dealer_bust_hand):

    result = check_winner(player_low_hand, dealer_bust_hand)

    assert result == "Dealer bust player wins!"

def test_tie_blackjack(blackjack_hand, dealer_blackjack_hand):

    result = check_winner(blackjack_hand, dealer_blackjack_hand)

    assert result == "It's a Tie!"

def test_player_blackjack(blackjack_hand, dealer_high_hand):

    result = check_winner(blackjack_hand, dealer_high_hand)

    assert result == "You have a blackjack, you WIN!"

def test_dealer_blackjack(player_high_hand, dealer_blackjack_hand):

    result = check_winner(player_high_hand, dealer_blackjack_hand)

    assert result == "Dealer has a blackjack, you Lose!"

def test_player_value_win(player_high_hand, dealer_low_hand):

    result = check_winner(player_high_hand, dealer_low_hand, True)

    assert result == "You Win!"

def test_tie_hand():
    player_hand = Hand()
    dealer_hand = Hand(dealer=True)

    player_hand.add_card([
        Card("Hearts", {"rank": "K", "value": 10}),
        Card("Hearts", {"rank": "5", "value": 5})
    ])

    dealer_hand.add_card([
        Card("Hearts", {"rank": "K", "value": 10}),
        Card("Hearts", {"rank": "5", "value": 5})
    ])

    result = check_winner(player_hand, dealer_hand, True)

    assert result == "TIE!"

def test_dealer_value_win(player_low_hand, dealer_high_hand):

    result = check_winner(player_low_hand, dealer_high_hand, True)

    assert result == "Dealer Win!"

def test_handle_result_outputs_message(player_low_hand, dealer_high_hand,capsys):

    print_test = handle_result(player_low_hand, dealer_high_hand, True)

    captured = capsys.readouterr()

    assert print_test is True
    assert "Dealer Win!" in captured.out or "You Win!" in captured.out