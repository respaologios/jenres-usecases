import pytest
from unittest.mock import Mock, patch
from flight_club_prj.flight_search import FlightSearch
from datetime import datetime


class TestFlightSearch:

    @patch('flight_club_prj.flight_search.requests.get')
    def test_get_destination_code(self, mock_get):
        # Setup
        mock_get.return_value.json.return_value = {
            "locations": [{"code": "TEST"}]
        }

        # Exercise
        flight_search = FlightSearch()
        destination_code = flight_search.get_destination_code("Test City")

        # Verify
        assert destination_code == "TEST"
        mock_get.assert_called_once()

    @patch('flight_club_prj.flight_search.requests.get')
    def test_check_flights(self, mock_get):
        # Setup
        mock_get.return_value.json.return_value = {
            "data": [{
                "price": 100,
                "route": [
                    {"cityFrom": "CityA", "flyFrom": "CITYA", "local_departure": "2023-04-01T10:00:00Z"},
                    {"cityTo": "CityB", "flyTo": "CITYB", "local_departure": "2023-04-08T10:00:00Z"}
                ]
            }]
        }

        # Exercise
        flight_search = FlightSearch()
        flight_data = flight_search.check_flights("CITYA", "CITYB", datetime.now(), datetime.now())

        # Verify
        assert flight_data.price == 100
        assert flight_data.origin_city == "CityA"
        assert flight_data.destination_city == "CityB"
        mock_get.assert_called()
