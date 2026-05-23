# ====================================================
# 200 OK: Successful request, but no new resource is necessarily created.

# 201 Created: Successful request where a new resource has been created

# ==========================================================


import requests

base_url = "https://reqres.in/"
endpoint = "api/users"

url = base_url + endpoint



json_payload = {
    "name": "morpheus",
    "job": "leader"
}

response = requests.post(url, data=json_payload)

# check status code

if response.status_code==201:
    print("status code is ", response.status_code)
    print(response.json())
else :
    print("error code is ",response.status_code)

