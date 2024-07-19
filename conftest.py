import pytest

from bun import Bun
from burger import Burger
from ingredient import Ingredient
from ingredient_types import INGREDIENT_TYPE_FILLING
from database import Database


@pytest.fixture(scope='function')
def bun_correct():
    return Bun("булочка", 52.34)


@pytest.fixture(scope='function')
def ingredient():
    return Ingredient(INGREDIENT_TYPE_FILLING, "котлета", 126.3)


@pytest.fixture(scope='function')
def database():
    return Database()


@pytest.fixture(scope='function')
def burger():
    return Burger()


@pytest.fixture(scope='function')
def burger_correct(burger, bun_correct, ingredient):
    burger.set_buns(bun_correct)
    burger.add_ingredient(ingredient)
