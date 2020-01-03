import datetime

import pytz

country = 'Asia/Tokyo'

time_zone = pytz.timezone(country)
my_timezone = datetime.datetime.now(time_zone)

print("Country : {0} Time: {1}".format(country, my_timezone))
print("UTC time: {}".format(datetime.datetime.utcnow()))

for country in pytz.country_timezones:
    print(country, pytz.country_timezones[country])