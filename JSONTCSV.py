import csv, json

with open("out.json", encoding="utf-8") as f:
    data = json.load(f)

with open("data.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=data[0].keys())
    writer.writeheader()
    writer.writerows(data)
