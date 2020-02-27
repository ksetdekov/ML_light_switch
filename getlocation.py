def string_distances():
    from locationsharinglib import Service
    from spatial import vincenty_inverse as vi
    with open("coordinates.txt", "r") as f:
        data = f.readlines()
    home = [float(data[1].split(":", 1)[1]), float(data[2].split(":", 1)[1])]
    cookies_file = 'cookies.txt'
    google_email = 'ksetdekov@gmail.com'
    service = Service(cookies_file=cookies_file, authenticating_account=google_email)
    names = []
    distances = []
    for person in service.get_all_people():
        names.append(person.nickname)
        pp = [person.latitude, person.longitude]
        distances.append(vi(home, pp).km())
    dictionary = dict(zip(names, distances))
    sortednames = []
    sorteddists = []
    for elem in sorted(dictionary.items()):
        sortednames.append(elem[0])
        sorteddists.append(str(elem[1]))
    allnames = str(",".join(sortednames))
    alldistances = str(",".join(sorteddists))
    return str(",".join([alldistances, allnames]))
