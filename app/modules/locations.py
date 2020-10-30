import requests


def get_all_locations_to_country():
    all_locations_to_country = {}
    headers = {"X-Client": "code.kiwi.com/medium"}
    resp = requests.get(
        """
        https://api.skypicker.com/locations/v2/graphql?query={
                locations(options:
                {   
                    active_only: "false", limit: 150000, location_types: ["airport","bus_station","station"]
                }
            ) {id int_id country_name}
        }"""
        , headers=headers
    )
    locations_data = resp.json()["locations"]

    for location in locations_data:
        location_code = location["id"]
        country_name = location["country_name"]
        all_locations_to_country[location_code] = country_name

    return all_locations_to_country
