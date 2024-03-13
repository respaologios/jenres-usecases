import logging
import requests

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

SHEETY_PRICES_ENDPOINT = YOUR SHEETY PRICES ENDPOINT
SHEETY_USERS_ENDPOINT = YOUR SHEETY USERS ENDPOINT

class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response =  requests.get(url=SHEETY_PRICES_ENDPOINT)
        if response.status_code != 200:
            logging.error(f'GET request to SHEETY_PRICES_ENDPOINT failed with status: {response.status_code}')
        else:
            logging.info('GET request to SHEETY_PRICES_ENDPOINT successful')
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data
            )
            if response.status_code != 200:
                logging.error(f'PUT request to SHEETY_PRICES_ENDPOINT for city {city["iataCode"]} failed with status: {response.status_code}')
            else:
                logging.info(f'Destination codes updated for city {city["iataCode"]}')

    def get_customer_emails(self):
        customers_endpoint = SHEETY_USERS_ENDPOINT
        response = requests.get(url=customers_endpoint)
        if response.status_code != 200:
            logging.error(f'GET request to SHEETY_USERS_ENDPOINT failed with status: {response.status_code}')
        else:
            logging.info('GET request to SHEETY_USERS_ENDPOINT successful')
        data = response.json()
        self.customer_data = data["users"]
        return self.customer_data
