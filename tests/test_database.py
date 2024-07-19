class TestDatabase:
    def test_available_buns(self, database):
        for i in range(len(database.buns)):
            assert database.available_buns()[i] == database.buns[i]

    def test_available_ingredients(self, database):
        for i in range(len(database.ingredients)):
            assert database.available_ingredients()[i] == database.ingredients[i]
