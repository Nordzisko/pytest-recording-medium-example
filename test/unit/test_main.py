from app.main import find_country


def test_find_country():
    input_location = "BTS"
    country_name = find_country(input_location)
    assert country_name == "Slovakia"
