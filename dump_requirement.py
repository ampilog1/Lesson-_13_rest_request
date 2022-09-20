import requests
from pickle import dump, load
from json import dump as jdump



url = 'https://api.hh.ru/vacancies'
params = {'text': 'machine learning', 'area': '1'}
res = requests.get(url, params=params).json()
with open('res.pkl', mode='wb') as f:
    dump(res, f)