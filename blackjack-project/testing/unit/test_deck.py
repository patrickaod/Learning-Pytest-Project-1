from app.models.deck import Deck

def test_deck_initial_size():
    deck = Deck()
    assert len(deck.cards) == 52

def test_deal_reduces_deck_size():
    deck = Deck()

    deck.deal(2)

    assert len(deck.cards) == 50

def test_deal_returns_cards():
    deck = Deck()

    dealt = deck.deal(3)

    assert len(dealt) == 3

def test_deal_more_than_available():
    deck = Deck()

    dealt = deck.deal(100)

    assert isinstance(dealt, list)

def test_shuffle_changes_order():
    deck1 = Deck()
    deck2 = Deck()

    original = deck1.cards.copy()

    deck2.shuffle()

    assert deck2.cards != original