from hand import Hand
from card import Card
from game_logic import check_winner, handle_result

def test_player_bust():
    player_hand = Hand()
    dealer_hand = Hand(dealer=True)

    player_hand.add_card([
        Card("Hearts", {"rank": "K", "value": 10}),
        Card("Spades", {"rank": "Q", "value": 10}),
        Card("Clubs", {"rank": "5", "value": 5}),
    ])

    dealer_hand.add_card([
        Card("Diamonds", {"rank": "9", "value": 9})
    ])

    result = check_winner(player_hand, dealer_hand)

    assert result == "You bust dealer wins!"

def test_dealer_bust():
    player_hand = Hand()
    dealer_hand = Hand(dealer=True)

    player_hand.add_card([
        Card("Hearts", {"rank": "K", "value": 10}),
        Card("Hearts", {"rank": "5", "value": 5})
    ])

    dealer_hand.add_card([
        Card("Diamonds", {"rank": "9", "value": 9}),
        Card("Spades", {"rank": "Q", "value": 10}),
        Card("Clubs", {"rank": "5", "value": 5})
    ])

    result = check_winner(player_hand, dealer_hand)

    assert result == "Dealer bust player wins!"

def test_tie_blackjack():
    player_hand = Hand()
    dealer_hand = Hand(dealer=True)

    player_hand.add_card([
        Card("Hearts", {"rank": "K", "value": 10}),
        Card("Hearts", {"rank": "A", "value": 11})
    ])

    dealer_hand.add_card([
        Card("Hearts", {"rank": "K", "value": 10}),
        Card("Hearts", {"rank": "A", "value": 11})
    ])

    result = check_winner(player_hand, dealer_hand)

    assert result == "It's a Tie!"

def test_player_blackjack():
    player_hand = Hand()
    dealer_hand = Hand(dealer=True)

    player_hand.add_card([
        Card("Hearts", {"rank": "K", "value": 10}),
        Card("Hearts", {"rank": "A", "value": 11})
    ])

    dealer_hand.add_card([
        Card("Hearts", {"rank": "K", "value": 10}),
        Card("Hearts", {"rank": "1", "value": 1})
    ])

    result = check_winner(player_hand, dealer_hand)

    assert result == "You have a blackjack, you WIN!"

def test_dealer_blackjack():
    player_hand = Hand()
    dealer_hand = Hand(dealer=True)

    player_hand.add_card([
        Card("Hearts", {"rank": "K", "value": 10}),
        Card("Hearts", {"rank": "5", "value": 5})
    ])

    dealer_hand.add_card([
        Card("Hearts", {"rank": "K", "value": 10}),
        Card("Hearts", {"rank": "A", "value": 11})
    ])

    result = check_winner(player_hand, dealer_hand)

    assert result == "Dealer has a blackjack, you Lose!"

def test_player_value_win():
    player_hand = Hand()
    dealer_hand = Hand(dealer=True)

    player_hand.add_card([
        Card("Hearts", {"rank": "K", "value": 10}),
        Card("Hearts", {"rank": "9", "value": 9})
    ])

    dealer_hand.add_card([
        Card("Hearts", {"rank": "K", "value": 10}),
        Card("Hearts", {"rank": "8", "value": 8})
    ])

    result = check_winner(player_hand, dealer_hand, True)

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

def test_dealer_value_win():
    player_hand = Hand()
    dealer_hand = Hand(dealer=True)

    player_hand.add_card([
        Card("Hearts", {"rank": "K", "value": 10}),
        Card("Hearts", {"rank": "8", "value": 8})
    ])

    dealer_hand.add_card([
        Card("Hearts", {"rank": "K", "value": 10}),
        Card("Hearts", {"rank": "9", "value": 9})
    ])

    result = check_winner(player_hand, dealer_hand, True)

    assert result == "Dealer Win!"

def test_handle_result_outputs_message(capsys):
    player_hand = Hand()
    dealer_hand = Hand(dealer=True)

    player_hand.add_card([
        Card("Hearts", {"rank": "K", "value": 10}),
        Card("Hearts", {"rank": "8", "value": 8})
    ])

    dealer_hand.add_card([
        Card("Hearts", {"rank": "K", "value": 10}),
        Card("Hearts", {"rank": "9", "value": 9})
    ])

    print_test = handle_result(player_hand, dealer_hand, True)

    captured = capsys.readouterr()

    assert print_test is True
    assert "Dealer Win!" in captured.out or "You Win!" in captured.out