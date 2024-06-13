import pytest

from ingredient import Ingredient
from ingredient_types import INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE


class TestIngredient:
    def test_get_name(self, ingredient):
        assert ingredient.get_name() == ingredient.name

    def test_get_price(self, ingredient):
        assert ingredient.get_price() == ingredient.price

    def test_get_type(self, ingredient):
        assert ingredient.get_type() == ingredient.type

    @pytest.mark.parametrize("ingredient_type, name, price",
                             [[INGREDIENT_TYPE_FILLING, 1234, 126.3],
                              [1234, "котлета", 126.3],
                              [INGREDIENT_TYPE_SAUCE, "котлета", "126.3"]])
    def test_bun(self, ingredient_type, name, price):
        try:
            Ingredient(ingredient_type, name, price)
        except Exception as e:
            assert type(e).__name__ == TypeError
