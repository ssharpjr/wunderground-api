#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# grovetown-weather.py - Weather Underground API

import requests

location_city = "Grovetown"
location_state = "GA"
api_key = "5a2e368ba8fe7d8b"
api_url_root = "http://api.wunderground.com/api/"
api_features = '/conditions/forecast/q/'
url = api_url_root + api_key + api_features +\
      location_state + '/' + location_city + '.json'

r = requests.get(url)

r_parsed = r.json()

city = r_parsed['current_observation']['display_location']['city']
state = r_parsed['current_observation']['display_location']['state']
weather = r_parsed['current_observation']['weather']
temp = r_parsed['current_observation']['temperature_string']
wind = r_parsed['current_observation']['wind_string']
ob_time = r_parsed['current_observation']['observation_time']

print()
print('Current Weather for ' + city + ', ' + state)
print(weather)
print('Temp: ' + temp)
print('Winds ' + wind)
print(ob_time)
print()
