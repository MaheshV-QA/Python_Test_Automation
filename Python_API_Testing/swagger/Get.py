import requests


def fetch_activities():
    url = "https://fakerestapi.azurewebsites.net/api/v1/Activities"
    headers = {'Accept': 'application/json'}
    response = requests.get(url, headers=headers, timeout=10)
    response.raise_for_status()
    return response.json()


def main():
    activities = fetch_activities()
    print(activities)


if __name__ == "__main__":
    try:
        main()
    except requests.RequestException as exc:
        print(f"API request failed: {exc}")
        raise


