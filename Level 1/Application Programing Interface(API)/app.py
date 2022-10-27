
import requests

# HW 1 make it interactive
query = input("Enter a domanian or IP asdress: ")
url = f"http://ip-api.com/json/{query}"
res = requests.get(url)
data = res.json()
if data['status'] == 'success':
    # print(type(data))
    #print(data)
    print(data['country'] )
    print(data['isp'])
else:
    print("Not found!")

