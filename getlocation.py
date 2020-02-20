from locationsharinglib import Service
from spatial import vincenty_inverse as vi

with open("coordinates.txt", "r") as f:
    data = f.readlines()
home = [float(data[1].split(":", 1)[1]), float(data[2].split(":", 1)[1])]

cookies_file = 'cookies.txt'
google_email = 'ksetdekov@gmail.com'
service = Service(cookies_file=cookies_file, authenticating_account=google_email)
for person in service.get_all_people():
    print(person.full_name)
    pp = [person.latitude, person.longitude]
    print(vi(home, pp).km())
