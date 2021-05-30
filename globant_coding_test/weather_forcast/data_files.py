response_template = {
    "coord": {
        "lon": -74.0817,
        "lat": 4.6097
    },
    "weather": [
        {
            "id": 803,
            "main": "Clouds",
            "description": "broken clouds",
            "icon": "04d"
        }
    ],
    "base": "stations",
    "main": {
        "temp": 284.88,
        "feels_like": 284.56,
        "temp_min": 284.88,
        "temp_max": 284.88,
        "pressure": 1017,
        "humidity": 94,
        "sea_level": 1017,
        "grnd_level": 753
    },
    "visibility": 10000,
    "wind": {
        "speed": 0.52,
        "deg": 96,
        "gust": 1.07
    },
    "clouds": {
        "all": 75
    },
    "dt": 1622373413,
    "sys": {
        "type": 1,
        "id": 8582,
        "country": "CO",
        "sunrise": 1622371385,
        "sunset": 1622415905
    },
    "timezone": -18000,
    "id": 3688689,
    "name": "Bogotá",
    "cod": 200
}
response_template_city_not_found={
    "cod": "404",
    "message": "city not found"
}
forcast_template={
        "lat": 4.6097,
        "lon": -74.0817,
        "timezone": "America/Bogota",
        "timezone_offset": -18000,
        "current": {
            "dt": 1622373505,
            "sunrise": 1622371385,
            "sunset": 1622415905,
            "temp": 11.73,
            "feels_like": 11.41,
            "pressure": 1017,
            "humidity": 94,
            "dew_point": 10.8,
            "uvi": 0,
            "clouds": 75,
            "visibility": 10000,
            "wind_speed": 0.52,
            "wind_deg": 96,
            "wind_gust": 1.07,
            "weather": [
                {
                    "id": 803,
                    "main": "Clouds",
                    "description": "broken clouds",
                    "icon": "04d"
                }
            ]
        },
        "hourly": [
            {
                "dt": 1622372400,
                "temp": 11.73,
                "feels_like": 11.41,
                "pressure": 1017,
                "humidity": 94,
                "dew_point": 10.8,
                "uvi": 0,
                "clouds": 75,
                "visibility": 10000,
                "wind_speed": 0.52,
                "wind_deg": 96,
                "wind_gust": 1.07,
                "weather": [
                    {
                        "id": 500,
                        "main": "Rain",
                        "description": "light rain",
                        "icon": "10d"
                    }
                ],
                "pop": 0.69,
                "rain": {
                    "1h": 0.73
                }
            },
            {
                "dt": 1622376000,
                "temp": 11.8,
                "feels_like": 11.52,
                "pressure": 1017,
                "humidity": 95,
                "dew_point": 11.03,
                "uvi": 0.34,
                "clouds": 80,
                "visibility": 10000,
                "wind_speed": 0.45,
                "wind_deg": 121,
                "wind_gust": 1.13,
                "weather": [
                    {
                        "id": 803,
                        "main": "Clouds",
                        "description": "broken clouds",
                        "icon": "04d"
                    }
                ],
                "pop": 0.69
            }
        ]
}
forcast_wrong_lat={
    "cod": "400",
    "message": "wrong longitude"
}

test_response={
    'location_name': 'Bogotá, CO',
    'temperature': '284.88 °C',
    'wind': 'Light Air, 0.52 m/s, East',
    'cloudiness': 'broken clouds',
    'pressure': '1017 hpa',
    'humidity': '94%',
    'sunrise': '10:43 AM',
    'sunset': '11:05 PM',
    'geo_coordinates': [4.6097, -74.0817],
    'requested_time': '2021-05-30 17:05:05.386077',
    'forcast': [
        {
            'time': '11:00 AM',
            'temperature': '11.73 °C',
            'wind': 'Light Air, 0.52 m/s, East',
            'cloudiness': '75 %'
        }, {
            'time': '12:00 PM',
            'temperature': '11.8 °C',
            'wind': 'Calm, 0.45 m/s, East-SouthEast',
            'cloudiness': '80 %'
        }
    ]
}