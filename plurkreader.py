import requests

headers = {
    'authority': 'www.plurk.com',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'en-US,en;q=0.9,zh-TW;q=0.8,zh;q=0.7',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'dnt': '1',
    'origin': 'https://www.plurk.com',
    'referer': 'https://www.plurk.com/',
    'user-agent': 'Mozilla/5.0 (Linux; Android 5.1.1; 9022X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

data = {
    'user_id': '4546534',
    'offset': '2023-01-20T20:39:40.000Z',
}

response = requests.post('https://www.plurk.com/TimeLine/getPlurks', headers=headers, data=data)

rjson = response.json()

import pprint
#pprint.pprint(rjson)



from dateutil import parser
#parser.parse(datetime_string)


another_request_dt = None

for plurk in rjson['plurks']:
    dt = parser.parse(plurk['posted'])
    another_request_dt = dt
    print(dt)
    
# can then make another request with another_request_dt as 'offset'
