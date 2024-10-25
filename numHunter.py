import requests

def get_phone_info(phone_number):
    access_key = 'YOUR_API_KEY'  # Put your API key here
    url = f"http://apilayer.net/api/validate?access_key={'5487129a5cb1dae231aa70b82feef861'}&number={phone_number}"

    response = requests.get(url)
    data = response.json()

    if data['valid']:
        return {
            'number': data['number'],
            'country_code': data['country_code'],
            'country_name': data['country_name'],
            'location': data['location'],
            'carrier': data['carrier'],
            'line_type': data['line_type'],
        }
    else:
        return None

if __name__ == '__main__':
    phone_number = input("Enter the phone number: ")
    info = get_phone_info(phone_number)
    
    if info:
        print("Phone number information:")
        for key, value in info.items():
            print(f"{key}: {value}")
    else:
        print("No information found for this number.")
