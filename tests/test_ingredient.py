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
