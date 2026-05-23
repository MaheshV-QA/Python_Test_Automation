"""
The requests library is one of an integral part of Python for making HTTP requests to a specified URL. 
Whether it be REST APIs or Web Scraping, requests are must be learned for proceeding further with these technologies.

"""


import requests

base_url = "https://reqres.in/"
endpoint = "api/users?page=2"

url = base_url + endpoint

response = requests.get(url)
# print the starus code
print(response) 

# check status code

if response.status_code==200:
    print("status code is ", response.status_code)
    print(response.json())
else :
    print("error code is ",response.status_code)

