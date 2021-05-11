from json import load, dump

with open("data.json", "r") as data:
    course = load(data)
    print(course)
    print(f'Nazwa kursu: "{course["name"]}"')
    print(f'Zapisani kursanci: {course["members"]}')
    for member in course["members"]:
        print(f' ({member["id"]}) - {member["first_name"]} {member["last_name"]}')
    for member in enumerate(course["members"]):
        print(member)

    first_name = input("Imię: ")
    last_name = input("Nazwisko: ")

    with open("data.json", "w") as data:
        course["members"].append({
            "id": len(course["members"]) + 1,
            "first_name": first_name,
            "last_name": last_name
        })

        dump(course, data)

