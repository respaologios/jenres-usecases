import pytest
from unittest.mock import Mock, patch
from flight_club_prj.main import *
from datetime import datetime, timedelta


class TestMain:
    @patch('flight_club_prj.main.DataManager')
    @patch('flight_club_prj.main.FlightSearch')
    @patch('flight_club_prj.main.NotificationManager')
    def test_main_flow(self, mock_notification_manager, mock_flight_search, mock_data_manager):
        # Setup
        mock_data_manager_instance = mock_data_manager.return_value
        mock_data_manager_instance.get_destination_data.return_value = [
            {"iataCode": "", "city": "Test City", "lowestPrice": 200}
        ]
        mock_flight_search_instance = mock_flight_search.return_value
        mock_flight_search_instance.get_destination_codes.return_value = "TST"
        mock_flight_search_instance.check_flights.return_value = None

        # Exercise
        # Assuming main.py has a function called 'run_main_flow' to encapsulate the main logic
        run_main_flow()

        # Verify
        mock_data_manager_instance.get_destination_data.assert_called()
        mock_flight_search_instance.get_destination_codes.assert_called_with(['Test City'])
        mock_data_manager_instance.update_destination_codes.assert_called()
        mock_flight_search_instance.check_flights.assert_called()
