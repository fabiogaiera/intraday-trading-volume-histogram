import csv
import sys
from pathlib import Path

from api_client import get_response
from dict_parser import fetch_csv_rows_from_dict


def retrieve_trades_data(ticker, date, destination_folder):

    file_name = "{}_{}.csv".format(ticker, date)
    full_path = Path(destination_folder) / file_name
    str_full_path = str(full_path)

    with open(str_full_path, 'w', newline='') as file:

        writer = csv.writer(file)
        first_row = ["datetime", "sym", "price", "size"]
        writer.writerow(first_row)

        next_page_token = None
        first_iteration = True

        while next_page_token or first_iteration:

            if first_iteration:

                parsed_data, next_page_token = get_response(ticker, date)
                rows = fetch_csv_rows_from_dict(parsed_data)
                writer.writerows(rows)
                next_page_token = parsed_data['next_page_token']
                first_iteration = False

            else:

                parsed_data, next_page_token = get_response(ticker, date, next_page_token)
                rows = fetch_csv_rows_from_dict(parsed_data)
                writer.writerows(rows)
                next_page_token = parsed_data['next_page_token']


"""

To use this script, you must setup both environment variables in your OS:
API-KEY
API-SECRET
See https://alpaca.markets to get an API key and its corresponding secret

"""

if __name__ == "__main__":

    if len(sys.argv) != 4:
        print("Usage: python trades_data_retriever.py <ticker> <yyyy-MM-dd> </path/to/folder>")
        sys.exit(1)
    retrieve_trades_data(sys.argv[1], sys.argv[2], sys.argv[3])
