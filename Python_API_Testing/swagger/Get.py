import requests

head = {

    'Accept' : 'text/plain'
}

response  = requests.get("https://fakerestapi.azurewebsites.net/api/v1/Activities",headers=head)

status = response.status_code

if status == 200:
    print(response.json())

else:
    print("error status code",status)

# check with asserts 

assert status==200  #True


