import requests
import urllib3

#Used to suppress the warning that Python gives when accessing the page without HTTPS
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

r = requests.get('http://www.weerindelft.nl/clientraw.txt', verify = False)
data_retrieved = r.text.split(' ')
current_temperature = round(float(data_retrieved[4]))

print(current_temperature, 'degrees Celsius')