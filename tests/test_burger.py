from unittest.mock import Mock

from ingredient_types import INGREDIENT_TYPE_FILLING


class TestBurger:
    def test_get_price(self, burger, burger_correct, bun_correct, ingredient):
        assert burger.get_price() == bun_correct.price * 2 + ingredient.price

    def test_get_price_without_ingredient(self, burger, burger_correct, bun_correct, ingredient):
        burger.remove_ingredient(0)
        assert burger.get_price() == bun_correct.price * 2

    def test_get_receipt(self, burger, burger_correct, bun_correct, ingredient):
        assert burger.get_receipt() == (f'(==== {bun_correct.get_name()} ====)\n'
                                        f'= {str(ingredient.get_type()).lower()} {ingredient.get_name()} =\n'
                                        f'(==== {bun_correct.get_name()} ====)\n\nPrice: {burger.get_price()}')

    def test_get_receipt_with_few_ingredients_move_mock_first(self, burger, burger_correct, bun_correct, ingredient):
        mock_ingredient = Mock()
        mock_ingredient.configure_mock(type=INGREDIENT_TYPE_FILLING, name='огурец')
        mock_ingredient.get_price.return_value = 56.2
        burger.add_ingredient(mock_ingredient)
        burger.move_ingredient(0, 1)
        assert burger.get_receipt() == (f'(==== {bun_correct.get_name()} ====)\n'
                                        f'= {str(mock_ingredient.get_type()).lower()} {mock_ingredient.get_name()} =\n'
                                        f'= {str(ingredient.get_type()).lower()} {ingredient.get_name()} =\n'
                                        f'(==== {bun_correct.get_name()} ====)\n\nPrice: {burger.get_price()}')
