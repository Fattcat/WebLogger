import requests
import os
import random
import string
import json

chars = string.ascii_letters + string.digits + '!@#$%^&*()'
random.seed = (os.urandom(1024))

url = "mojawebstrankapreprihlasenie.com"

names = json.loads(open('names.json').read())

for name in names:
    name_extra = ''.join(random.choice(string.digits))

    username = name.lower() + name_extra + '@gmail.com'
    password = ''.join(random.choice(chars) for i in range(8)

    response = requests.post(url, allow_redirects=False, data={
        'auid2yjauysd2uasdasdasd': username,
        'kjauysd6sAJSDhyui2yasd': password
    })

    if "Successfully" in response.text:
        print(f'Username {username} and password {password} Is Correct! SUCCESSFULLY Logged Into the website')
    else:
        print(f'Failed to log in with username {username} and password {password}')
