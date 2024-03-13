import unittest
from unittest.mock import patch
import logging
from flight_club_prj.data_manager import DataManager


class TestDataManager(unittest.TestCase):

    @patch('flight_club_prj.data_manager.requests.get')
    def test_get_destination_data_logging(self, mock_get):
        # Setup the mock to return a successful response
        mock_get.return_value.status_code = 200

        # Capture the logs
        with self.assertLogs(level='INFO') as log:
            manager = DataManager()
            manager.get_destination_data()

        # Check that the log message contains the expected text
        self.assertIn('GET request to SHEETY_PRICES_ENDPOINT successful', log.output[0])

    @patch('flight_club_prj.data_manager.requests.put')
    def test_update_destination_codes_logging(self, mock_put):
        # Setup the mock to return a successful response
        mock_put.return_value.status_code = 200

        # Capture the logs
        with self.assertLogs(level='INFO') as log:
            manager = DataManager()
            manager.destination_data = [{'id': '1', 'iataCode': 'LON'}]
            manager.update_destination_codes()

        # Check that the log message contains the expected text
        self.assertIn('Destination codes updated for city LON', log.output[0])

    @patch('flight_club_prj.data_manager.requests.get')
    def test_get_customer_emails_logging(self, mock_get):
        # Setup the mock to return a successful response
        mock_get.return_value.status_code = 200

        # Capture the logs
        with self.assertLogs(level='INFO') as log:
            manager = DataManager()
            manager.get_customer_emails()

        # Check that the log message contains the expected text
        self.assertIn('GET request to SHEETY_USERS_ENDPOINT successful', log.output[0])


if __name__ == '__main__':
    unittest.main()
