from locationsharinglib import Service
cookies_file = 'cookies.txt'
google_email = 'ksetdekov@gmail.com'
service = Service(cookies_file=cookies_file, authenticating_account=google_email)
for person in service.get_all_people():
    print(person)
