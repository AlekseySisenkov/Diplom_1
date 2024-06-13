import pytest

from bun import Bun


class TestBun:
    def test_get_name(self, bun_correct):
        assert bun_correct.get_name() == bun_correct.name

    def test_get_price(self, bun_correct):
        assert bun_correct.get_price() == bun_correct.price

    @pytest.mark.parametrize("name, price",
                             [[1234, 52.34],
                              ["булочка", "52.34"]])
    def test_bun(self, name, price):
        try:
            Bun(name, price)
        except Exception as e:
            assert type(e).__name__ == TypeError
