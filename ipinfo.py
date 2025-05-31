import requests

def get_ip_info():
    # IP INFO
    # Fetch data from the ipinfo.io API
    response = requests.get("https://ipinfo.io")
    data = response.json()

    # Extract and display the basic information
    print(f"IP Address: {data.get('ip')}")
    print(f"City: {data.get('city')}")
    print(f"Region: {data.get('region')}")
    print(f"Country: {data.get('country')}")
    print(f"Location (Lat, Long): {data.get('loc')}")
    print(f"Organization: {data.get('org')}")
    print(f"Timezone: {data.get('timezone')}")

if __name__ == "__main__":
    get_ip_info()
