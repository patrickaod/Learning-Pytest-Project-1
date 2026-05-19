# conftest.py
import pytest
from app.models.hand import Hand

@pytest.fixture
def hand_factory():
    def _create(dealer=False, cards=None):
        hand = Hand(dealer=dealer)
        if cards:
            hand.add_card(cards)
        return hand
    return _create