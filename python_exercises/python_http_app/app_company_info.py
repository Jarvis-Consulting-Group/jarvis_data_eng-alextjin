import pandas as pd
import os
import sys
import requests
import json

status_dict = {
    200: "OK. The requested action was successful.",
    201: "Created. A new resource was created.",
    202: "Accepted. The request was received, but no modification has been made yet.",
    204: "No Content. The request was successful, but the response has no content.",
    400: "Bad Request. The request was malformed.",
    401: "Unauthorized. The client is not authorized to perform the requested action.",
    404: "Not Found. The requested resource was not found.",
    415: "Unsupported Media Type. The request data format is not supported by the server.",
    422: "Unprocessable Entity. The request data was properly formatted but contained invalid or missing data.",
    500: "Internal Server Error. The server threw an error when processing the request.",
}
def find_company_info(ticker):
    querystring = {"function": "GLOBAL_QUOTE", "symbol": ticker}
    headers = {
        "X-RapidAPI-Key": "c1d302c45amsh4e9631273747c36p1732c6jsnd89f23b0d7b0",
        "X-RapidAPI-Host": "alpha-vantage.p.rapidapi.com",
    }
    r = requests.get(
        "https://alpha-vantage.p.rapidapi.com/query", headers=headers, params=querystring
    )

    print(f"Status code = {r.status_code}. {status_dict[r.status_code]}")

    if r.status_code == 200:
        print(f'Data is exporting to file: \n {os.getcwd()}/ticker.json')
        r_content = r.json()
        with open("ticker.json", "w") as f:
            for item in r_content.values():
                for v in item.values():
                    f.write(f"{v}\n")

find_company_info(sys.argv[1])
