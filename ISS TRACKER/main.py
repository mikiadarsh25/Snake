import requests
import datetime as datetime
import smtplib
import time

My_LAT = 22.804565
My_lon = 86.259155
my_email = ""
password = ""


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    longitude = float(data["iss_position"]["longitude"])
    latitude = float(data["iss_position"]["latitude"])
    if My_LAT - 5 <= longitude <= My_LAT + 5 and My_lon - 5 <= latitude <= My_lon + 5:
        return True


def is_night():
    parameter = {
        "lat": My_LAT,
        "lng": My_lon,
        "formatted": 0
    }

    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameter)

    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]['sunset'].split("T")[1].split(":")[0])
    time_now = datetime.now().hour
    if time_now >= sunset or time_now <= sunrise:
        return True


while True:
    time.sleep(60)
    if is_night() and is_iss_overhead():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs="mikiadarsh25@gmail.com",
                                msg="Subject:Look Up \n\n The ISS is above you in the sky"
                                )
