import requests

base_url = "https://reqres.in/"
endpoint = "api/users"
# actual link ==>https://reqres.in/api/users?page=2
#  with adding parametres in url using params
url = base_url + endpoint

parameters = {

    "page" : "2"
}
response = requests.get(url,params=parameters)


# check status code

if response.status_code==200:
    print("status code is ", response.status_code)
    print(response.json())
else :
    print("error code is ",response.status_code)

