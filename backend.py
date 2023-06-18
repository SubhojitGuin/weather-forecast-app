import pandas as pd
import requests

# API key can be obtained from https://api.openweathermap.org
API_KEY = "bf6634cd1bd0a75e3adf144ced74368b"


def get_city_id(place):
    df = pd.read_json("city.list.json")
    city_id = df[df["name"] == place]["id"].squeeze()
    return city_id


def get_data(place, forecast_days):
    city_id = get_city_id(place)
    url = f"https://api.openweathermap.org/data/2.5/forecast?id={city_id}&appid={API_KEY}"
    response = requests.get(url=url)
    data = response.json()
    filtered_data = data["list"]
    nr_values = 8 * forecast_days
    filtered_data = filtered_data[:nr_values]
    return filtered_data


if __name__ == "__main__":
    get_data("Kolkata", 5)
