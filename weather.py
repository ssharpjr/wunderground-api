#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# weather.py - Weather Underground API Report
#              based on your current IP location

import requests

api_key = "5a2e368ba8fe7d8b"
api_url_root = "http://api.wunderground.com/api/"
api_features = '/astronomy/conditions/forecast/q/'

url = api_url_root + api_key + api_features + 'autoip.json'

r = requests.get(url)
rp = r.json()

# API assignments
current = 'current_observation'
location = rp[current]['display_location']['full']
weather = rp[current]['weather']
temp = rp[current]['temperature_string']
wind = rp[current]['wind_string']
humidity = rp[current]['relative_humidity']
pressure = rp[current]['pressure_in']
pressure_trend = rp[current]['pressure_trend']
dew_point = rp[current]['dewpoint_f']
ob_time = rp[current]['observation_time']


# Custom Formatting
if pressure_trend == '-':
    pressure_trend = ' Steady'


# Current Weather
print('\n==============================')
print('Current Weather for ' + location)
print()
print(weather)
print('Temp: ' + temp)
print('Winds ' + wind)
print('Humidity: ' + humidity)
print('Pressure: ' + pressure + pressure_trend)
print('Dew Point: ' + str(dew_point) + ' F')
print(ob_time)
print('\n------------------------------')

# Forecast
print()
print("3-Day Forecast")

print('\n==============================')
