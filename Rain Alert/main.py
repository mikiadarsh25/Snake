import requests
from twilio.rest import Client
import os

api_key = os.environ["API_KEY"]
owm_endpoint = "https://api.openweathermap.org/data/2.5/onecall"
account_sid = os.environ['ACCOUNT_SID']
auth_token = os.environ['AUTH_TOKEN']
parameters = {
    "lat": 22.804565,
    "lon": 86.202873,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(owm_endpoint, params=parameters)
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]
for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
    if will_rain:
        client = Client(account_sid, auth_token)
        message = client.messages \
            .create(
            body="It's going to rain So, bring up Umbrella.",
            from_=os.environ['TWILIO_NO'],
            to=os.environ['PERSONAL_NO>']
        )
        print(message.sid)


