from app.modules.locations import get_all_locations_to_country


def find_country(given_location_code):
    location_to_country = get_all_locations_to_country()
    country_name = location_to_country.get(given_location_code)
    return country_name


def main():
    input_location = input("Enter location code, which country you want to know:")
    country_name = find_country(input_location)

    if country_name:
        print(f"Location {input_location} is in country {country_name}")
    else:
        print(f"There is no record of country for location {input_location}")


if __name__ == "__main__":
    main()
