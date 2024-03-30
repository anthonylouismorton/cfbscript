import json

school_json = 'schoolData.json'

with open('conferenceData.json') as f:
  data = json.load(f)

schoolArray = []

for conference in data:
    for school in conference["schools"]:
        obj = {"school": school["school"], "logo": school["logo"], "abbreviation": school["abbreviation"], "nickName": school["nickName"], "lon": school["lon"], "lat": school["lat"], "conferences": [{"conference": conference["conference"], "years": school["years"], "names":conference["names"]}]}
        if obj["school"] not in [entry["school"] for entry in schoolArray]:
            schoolArray.append(obj)
        else:
            for entry in schoolArray:
                if entry["school"] == obj["school"]:
                    entry["conferences"].append({"conference": conference["conference"], "years": school["years"]})

with open(school_json, 'w') as handle:
  json.dump(schoolArray, handle, indent=2)
