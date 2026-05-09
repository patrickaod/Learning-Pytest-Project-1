from card import Card
from game_logic import check_winner

def test_player_bust(hand_factory):
    
    player = hand_factory(cards=[
        Card("Hearts", {"rank": "K", "value": 10}),
        Card("Diamonds", {"rank": "Q", "value": 10}),
        Card("Clubs", {"rank": "5", "value": 5}),
    ])

    dealer = hand_factory(dealer=True, cards=[
        Card("Spades", {"rank": "9", "value": 9})
    ])
    
    result = check_winner(player, dealer)

    assert result == "You bust dealer wins!"

def test_dealer_bust(hand_factory):
    player = hand_factory(cards=[
        Card("Hearts", {"rank": "2", "value": 2}),
        Card("Diamonds", {"rank": "5", "value": 5})
    ])

    dealer = hand_factory(dealer=True, cards=[
        Card("Clubs", {"rank": "K", "value": 10}),
        Card("Spades", {"rank": "Q", "value": 10}),
        Card("Diamonds", {"rank": "10", "value": 10})
    ])

    result = check_winner(player, dealer)

    assert result == "Dealer bust player wins!"

def test_tie_blackjack(hand_factory):
    player = hand_factory(cards=[
        Card("Hearts", {"rank": "A", "value": 11}),
        Card("Spades", {"rank": "J", "value": 10})
    ])

    dealer = hand_factory(dealer=True, cards=[
        Card("Clubs", {"rank": "A", "value": 11}),
        Card("Diamonds", {"rank": "J", "value": 10})
    ])

    result = check_winner(player, dealer)

    assert result == "It's a Tie!"

def test_player_blackjack(hand_factory):
    player = hand_factory(cards=[
        Card("Hearts", {"rank": "A", "value": 11}),
        Card("Spades", {"rank": "J", "value": 10})
    ])

    dealer = hand_factory(dealer=True, cards=[
        Card("Clubs", {"rank": "K", "value": 10}),
        Card("Diamonds", {"rank": "5", "value": 5})
    ])

    result = check_winner(player, dealer)

    assert result == "You have a blackjack, you WIN!"

def test_dealer_blackjack(hand_factory):
    player = hand_factory(cards=[
        Card("Hearts", {"rank": "K", "value": 10}),
        Card("Spades", {"rank": "5", "value": 5})
    ])

    dealer = hand_factory(dealer=True, cards=[
        Card("Clubs", {"rank": "A", "value": 11}),
        Card("Diamonds", {"rank": "J", "value": 10})
    ])

    result = check_winner(player, dealer)

    assert result == "Dealer has a blackjack, you Lose!"

def test_player_value_win(hand_factory):
    player = hand_factory(cards=[
        Card("Hearts", {"rank": "K", "value": 10}),
        Card("Spades", {"rank": "9", "value": 9})
    ])

    dealer = hand_factory(dealer=True, cards=[
        Card("Clubs", {"rank": "2", "value": 2}),
        Card("Diamonds", {"rank": "5", "value": 5})
    ])

    result = check_winner(player, dealer, True)

    assert result == "You Win!"

def test_tie_hand(hand_factory):
    player = hand_factory(cards=[
        Card("Hearts", {"rank": "K", "value": 10}),
        Card("Spades", {"rank": "5", "value": 5})
    ])

    dealer = hand_factory(dealer=True, cards=[
        Card("Clubs", {"rank": "K", "value": 10}),
        Card("Diamonds", {"rank": "5", "value": 5})
    ])

    result = check_winner(player, dealer, True)

    assert result == "TIE!"

def test_dealer_value_win(hand_factory):
    player = hand_factory(cards=[
        Card("Hearts", {"rank": "2", "value": 2}),
        Card("Diamonds", {"rank": "5", "value": 5})
    ])

    dealer = hand_factory(dealer=True, cards=[
        Card("Clubs", {"rank": "K", "value": 10}),
        Card("Spades", {"rank": "9", "value": 9})
    ])

    result = check_winner(player, dealer, True)

    assert result == "Dealer Win!"

def test_handle_result_outputs_message(hand_factory,capsys):
    player = hand_factory(cards=[
        Card("Hearts", {"rank": "2", "value": 2}),
        Card("Diamonds", {"rank": "5", "value": 5})
    ])

    dealer = hand_factory(dealer=True, cards=[
        Card("Clubs", {"rank": "K", "value": 10}),
        Card("Spades", {"rank": "9", "value": 9})
    ])

    result = handle_result(player, dealer, True)

    captured = capsys.readouterr()

    assert result is True
    assert "Dealer Win!" in captured.out