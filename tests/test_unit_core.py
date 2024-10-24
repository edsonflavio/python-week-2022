from beerlog.core import get_beers_from_database, add_beer_to_database


def test_add_beer_to_database():
    """
    setar a variável BEERLOG_DATABASE__url="sqlite:///testing.db"
    antes de executar os testes - caso não use as fixture
    """
    assert add_beer_to_database("Blue Moon", "Witbier", 10, 3, 6)


def test_get_beer_from_database():
    # Arrange
    add_beer_to_database("Blue Moon", "Witbier", 10, 3, 6)
    # Act
    results = get_beers_from_database()
    # Assert
    assert len(results) > 0
