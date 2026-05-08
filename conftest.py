# conftest.py
import pytest
from hand import Hand
from card import Card

@pytest.fixture
def player_low_hand():
    player_hand = Hand()
    player_hand.add_card([
    Card("Hearts", {"rank": "2", "value": 2}),
    Card("Diamonds", {"rank": "5", "value": 5})
    ])
    return player_hand

@pytest.fixture
def player_high_hand():
    player_hand = Hand()
    player_hand.add_card([
    Card("Clubs", {"rank": "K", "value": 10}),
    Card("Spades", {"rank": "J", "value": 10})
    ])
    return player_hand

@pytest.fixture
def player_bust_hand():
    player_hand = Hand()
    player_hand.add_card([
    Card("Clubs", {"rank": "K", "value": 10}),
    Card("Spades", {"rank": "J", "value": 10}),
    Card("Diamonds", {"rank": "10", "value": 10})
    ])
    return player_hand

@pytest.fixture
def dealer_low_hand():
    dealer_hand = Hand(dealer=True)
    dealer_hand.add_card([
    Card("Hearts", {"rank": "2", "value": 2}),
    Card("Diamonds", {"rank": "5", "value": 5})
    ])
    return dealer_hand

@pytest.fixture
def dealer_high_hand():
    dealer_hand = Hand(dealer=True)
    dealer_hand.add_card([
    Card("Clubs", {"rank": "K", "value": 10}),
    Card("Spades", {"rank": "10", "value": 10})
    ])
    return dealer_hand

@pytest.fixture
def dealer_bust_hand():
    dealer_hand = Hand(dealer=True)
    dealer_hand.add_card([
    Card("Clubs", {"rank": "K", "value": 10}),
    Card("Spades", {"rank": "Q", "value": 10}),
    Card("Diamonds", {"rank": "10", "value": 10})
    ])
    return dealer_hand

@pytest.fixture
def blackjack_hand():
    player_hand = Hand()
    player_hand.add_card([
        Card("Hearts", {"rank": "A", "value": 11}),
        Card("Spades", {"rank": "J", "value": 10})
    ])
    return player_hand

@pytest.fixture
def dealer_blackjack_hand():
    dealer_hand = Hand(dealer=True)
    dealer_hand.add_card([
        Card("Hearts", {"rank": "A", "value": 11}),
        Card("Spades", {"rank": "J", "value": 10})
    ])
    return dealer_hand