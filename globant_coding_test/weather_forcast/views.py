import requests
from datetime import datetime
from django.http import JsonResponse
from globant_coding_test.settings import OPEN_WEATHER_API, API_KEY, ROOT_URL
from django.views.decorators.cache import cache_page


def request_url_json(url):
    return request_url(url).json()


def request_url(url):
    return requests.get(url)


def get_beaufort_scale(speed):
    beaufort_scale = {
        (0, 0.5): "Calm",
        (0.5, 1.5): "Light Air",
        (1.5, 3.3): "Light Breeze",
        (3.3, 5.5): "Gentle Breeze",
        (5.5, 7.9): "Moderate Breeze",
        (7.9, 10.7): "Fresh Breeze",
        (10.7, 13.8): "Strong Breeze",
        (13.8, 17.1): "Near Gale",
        (17.1, 20.7): "Gale",
        (20.7, 24.4): "Strong Gale",
        (24.4, 28.4): "Whole Gale",
        (28.4, 32.6): "Storm Force",
    }
    for min, max in beaufort_scale:
        if min <= abs(speed) <= max:
            return beaufort_scale.get((min, max))
    return "Hurricane Force"


def normalize_angle(angle):
    while angle < 0: angle += 360
    while angle >= 360: angle -= 360
    return angle


def get_directions_from_degrees(degrees):
    degrees = normalize_angle(degrees)

    degrees_to_direction = {
        (11.25, 33.74): "North-NorthEast",
        (33.74, 56.24): "North-East",
        (56.24, 78.74): "East-NorthEast",
        (78.74, 101.24): "East",
        (101.24, 123.74): "East-SouthEast",
        (123.74, 146.24): "South-East",
        (146.24, 168.74): "South-SouthEast",
        (168.74, 191.24): "South",
        (191.24, 213.74): "South-SouthWest",
        (213.74, 236.24): "South-West",
        (236.24, 258.74): "West-SouthWest",
        (258.74, 281.24): "West",
        (281.24, 303.74): "West-NorthWest",
        (303.74, 326.24): "North-West",
        (326.24, 348.74): "North-NorthWest",
    }

    for min, max in degrees_to_direction:
        if min <= degrees <= max:
            return degrees_to_direction.get((min, max))
    return "North"


def get_time_from_UNIX_stamp(timestamp):
    return datetime.utcfromtimestamp(timestamp).strftime('%I:%M %p')


def get_data_for_city(city, country):
    URL = f"{ROOT_URL}/weather?q={city},{country}&units={OPEN_WEATHER_API['units']}&appid={API_KEY}"
    data = request_url_json(URL)
    if data['cod'] is not 200:
        return data, False
    try:
        wind_scale = get_beaufort_scale(data['wind']['speed'])
        wind_direction = get_directions_from_degrees(data['wind']['deg'])
        sunrise = get_time_from_UNIX_stamp(data['sys']['sunrise'])
        sunset = get_time_from_UNIX_stamp(data['sys']['sunset'])
        return {
                   "location_name": f"{data['name']}, {data['sys']['country']}",
                   "temperature": f"{data['main']['temp']} ??C",
                   "wind": f"{wind_scale}, {data['wind']['speed']} m/s, {wind_direction}",
                   "cloudiness": f"{data['weather'][0]['description']}",
                   "pressure": f"{data['main']['pressure']} hpa",
                   "humidity": f"{data['main']['humidity']}%",
                   "sunrise": f"{sunrise}",
                   "sunset": f"{sunset}",
                   "geo_coordinates": [data['coord']['lat'], data['coord']['lon']],
                   "requested_time": f"{datetime.now()}",
                   "forcast": [],
               }, True
    except KeyError as e:
        return {'message': f'Error while parsing{e}'}, False
    except Exception as e:
        return {'message': f'Exception: {e}'}, False


def get_data_for_forcast(lat, log):
    URL = f"{ROOT_URL}/onecall?lat={lat}&lon={log}&units={OPEN_WEATHER_API['units']}&appid={API_KEY}"
    data = request_url_json(URL)
    if 'cod' in data:
        return data, False
    response_forcast = []
    try:
        for d in data["hourly"]:
            wind_scale = get_beaufort_scale(d['wind_speed'])
            wind_direction = get_directions_from_degrees(d['wind_deg'])
            response_forcast.append(
                {
                    "time": get_time_from_UNIX_stamp(d['dt']),
                    "temperature": f"{d['temp']} ??C",
                    "wind": f"{wind_scale}, {d['wind_speed']} m/s, {wind_direction}",
                    "cloudiness": f"{d['clouds']} %",
                }
            )
        return response_forcast, True
    except KeyError as e:
        return {'message': f'Error while parsing{e}'}, False
    except Exception as e:
        return {'message': f'Exception: {e}'}, False


def generate_weather_information(city, country):
    response_template, flag = get_data_for_city(city, country)
    if flag:
        try:
            lat = response_template['geo_coordinates'][0]
            log = response_template['geo_coordinates'][1]
            response_forcast, f_flag = get_data_for_forcast(lat, log)
            if f_flag:
                response_template["forcast"] = response_forcast
        except KeyError as e:
            return {'message': f'Error while parsing: {e}'}, False
        except Exception as e:
            return {'message': f'Exception: {e}'}, False
    return response_template, flag


@cache_page(60 * 2)
def get_weather(request):
    city = request.GET.get('city')
    country = request.GET.get('country')
    if city is None or country is None:
        return JsonResponse({'message': 'City/Country cannot be empty'}, status=400)
    response, flag = generate_weather_information(city, country)
    if flag: return JsonResponse(response)
    return JsonResponse(response, status=500)
