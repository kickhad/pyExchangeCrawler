import requests

url = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
txt = 'Si vous plez'
params = dict(key='trnsl.1.1.20190603T185607Z.d5f8270a6abdda7a.2c1c0d646da6415e2fc567509f94f98fd95a2b24' , text=txt , lang='fr-en',    format='plain',options=0)