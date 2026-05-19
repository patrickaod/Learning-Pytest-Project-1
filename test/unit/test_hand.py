from app.models.hand import Hand
from app.models.card import Card

def test_hand_add_card():
    hand = Hand()

    hand.add_card([Card("Diamonds", {"rank": "J", "value": 10})])

    assert len(hand.cards) == 1
    assert hand.cards[0].suit == "Diamonds"
    assert hand.cards[0].rank["rank"] == "J"

def test_hand_value_simple():
    hand = Hand()

    hand.add_card([Card("Hearts", {"rank": "10", "value": 10})])
    hand.add_card([Card("Spades", {"rank": "9", "value": 9})])

    assert hand.get_value() == 19

def test_hand_value_with_ace():
    hand = Hand()

    hand.add_card([Card("Hearts", {"rank": "A", "value": 11})])
    hand.add_card([Card("Spades", {"rank": "9", "value": 9})])
    hand.add_card([Card("Clubs", {"rank": "5", "value": 5})])

    assert hand.get_value() == 15

def test_is_blackjack():
    hand = Hand()

    hand.add_card([Card("Hearts", {"rank": "A", "value": 11})])
    hand.add_card([Card("Spades", {"rank": "J", "value": 10})])

    assert hand.is_blackjack()

def test_not_is_blackjack():
    hand = Hand()

    hand.add_card([Card("Hearts", {"rank": "3", "value": 3})])
    hand.add_card([Card("Spades", {"rank": "Q", "value": 10})])
    hand.add_card([Card("Spades", {"rank": "7", "value": 7})])

    assert not hand.is_blackjack()

def test_dealer_first_card_hidden():
    hand = Hand(dealer=True)

    hand.add_card([
        Card("Hearts", {"rank": "10", "value": 10}),
        Card("Spades", {"rank": "9", "value": 9})
    ])

    output = hand.display()

    assert "Hidden" in output

def test_player_hand_shows_value():
    hand = Hand()

    hand.add_card([
        Card("Hearts", {"rank": "10", "value": 10})
    ])

    output = hand.display()

    assert "Value: 10" in output