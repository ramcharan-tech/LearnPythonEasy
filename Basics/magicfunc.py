import re, requests
set(re.findall('__\w+__', requests.get('https://docs.python.org/3/reference/datamodel.html').text))