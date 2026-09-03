import csv, json

rows = []
with open("data2.csv", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    rows = list(reader)

with open("data2.json", "w", encoding="utf-8") as f:
    json.dump(rows, f, indent=4)
