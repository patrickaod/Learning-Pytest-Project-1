from card import Card 

def test_card_str():
    card = Card("Hearts", {"rank": "A", "value": 11})

    assert str(card) == "A of Hearts"

def test_card_attributes():
    card = Card("Spades", {"rank": "K", "value": 10})

    assert card.suit == "Spades"
    assert card.rank["rank"] == "K"