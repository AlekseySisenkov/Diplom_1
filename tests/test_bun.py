import pytest

from bun import Bun


class TestBun:
    def test_get_name(self, bun_correct):
        assert bun_correct.get_name() == bun_correct.name

    def test_get_price(self, bun_correct):
        assert bun_correct.get_price() == bun_correct.price
