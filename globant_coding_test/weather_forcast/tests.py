from django.test import TestCase
from unittest.mock import patch
from weather_forcast.views import \
    get_beaufort_scale, \
    normalize_angle, \
    get_directions_from_degrees, \
    generate_weather_information
from weather_forcast.test_values import \
    response_template, \
    forcast_template, \
    test_response


class Test_Weather_Information(TestCase):
    def setUp(self) -> None:
        self.maxDiff = None

    def test_get_beaufort_scale(self):
        values = {
            0: "Calm",
            0.5: "Calm",
            0.57: "Light Air",
            32.6: "Storm Force",
            32.75: "Hurricane Force",
            33: "Hurricane Force",
        }
        for key in values:
            self.assertEqual(get_beaufort_scale(key), values[key])

    def test_normalize_angle(self):
        values = {
            0: 0,
            290: 290,
            361: 1,
            -361: 359,
            -182: 178,
            182: 182,
        }
        for key in values:
            self.assertEqual(normalize_angle(key), values[key])

    def test_get_directions_from_degrees(self):
        values = {
            11.2: "North",
            33.741: "North-East",
            0: "North",
            348.745: "North",
        }
        for key in values:
            self.assertEqual(get_directions_from_degrees(key), values[key])

    @patch("weather_forcast.views.request_url_json")
    def test_generate_weather_information(self, mock_request):
        mock_request.side_effect = [response_template, forcast_template]
        response = generate_weather_information("Bogota", "co")
        for res in response:
            if (res != "requested_time"):
                self.assertEqual(response[res], test_response[res])
