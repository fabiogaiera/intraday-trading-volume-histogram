import json
import os

import requests

from url_composer import URLComposer

headers = {

    "accept": "application/json",
    "APCA-API-KEY-ID": os.getenv("API-KEY"),
    "APCA-API-SECRET-KEY": os.getenv("API-SECRET")

}


def get_response(symbol, date, next_page_token=None):

    base_url = f"https://data.alpaca.markets/v2/stocks/{symbol}/trades"
    url_with_params = URLComposer(base_url, date)

    if next_page_token:

        response = requests.get(url_with_params.get_string_url_with_next_page_token(next_page_token), headers=headers)
        parsed_data = json.loads(response.text)
        next_page_token = parsed_data['next_page_token']

    else:

        response = requests.get(url_with_params.get_string_url(), headers=headers)
        parsed_data = json.loads(response.text)
        next_page_token = parsed_data['next_page_token']

    return parsed_data, next_page_token
