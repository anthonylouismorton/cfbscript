import json

with open('conferenceData.json') as f:
  data = json.load(f)

for conference in data:
  print(conference["conference"])