#!/usr/bin/python3

import json
from urllib import request

try:
    data = json.load(request.urlopen('http://ipinfo.io/json'))
except Exception as e:
    print('An error ocurred: '+str(e))
else:
    print('You are currently located near: {city}, {region}, {country}'.format(**data))
    print('Latitude/Longitude: {}E'.format(data['loc'].replace(',','N, ')))