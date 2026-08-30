chelist = ["iron","copper","gold","silver","aluminum"]
chelist[2] = "tungsten"
chelist.append("gold")
chelist.append("neon")
chelist.remove("iron")
ele = 0
while ele < 6:
    print(chelist[ele])
    ele += 1

labs = (1,30,20)
#labs(0) = 2
#sid = labs(0)
#mgs = labs(1)
#ttc = labs(2)
#print(sid)
print(labs)
for lab in labs:
    print(lab)

srec = {"name":"Rose","major":"Biochemistry","year":2026}
srec["research_interest"]="Nanotechnology"
srec["major"]="Chemical Engineering"
for key in srec:
    print(f"{key}")
for key in srec:
    val=srec[key]
    print(f"{val}")
for key in srec:
    val=srec[key]
    print(f"{key}:{val}")

ctemp = [{"id":1,"mass":2.5,"temp":25},{"id":2,"mass":3.1,"temp":30},{"id":3,"mass":1.8,"temp":22}]
li=0
while li < 3:
    ctemp[li]["temp"]+=5
    if ctemp[li]["mass"]>2.0:
        print(ctemp[li])
    li+=1

samples = [
    {"id": 1, "temp": 25},
    {"id": 2, "temp": 30},
    {"id": 3, "temp": 22},
]
temps = [s["temp"] for s in samples]
avg_temp = sum(temps) / len(temps)
print(f"Average temperature: {avg_temp:.2f} °C")

inventory = {
    "acetone": 12,
    "ethanol": 5,
    "toluene": 0,
    "hexane": 3
}
chemical = input("Enter chemical name: ").lower()
if chemical in inventory:
    amount = inventory[chemical]
    if amount > 0:
        print(f"{chemical} is available ({amount} bottles).")
    else:
        print(f"{chemical} is out of stock.")
else:
    print("Chemical not found in inventory.")

coordinates = [
    (40.01, -105.27),
    (40.02, -105.25),
    (40.00, -105.30)
]
for lat, lon in coordinates:
    print(f"Location recorded at lat={lat}, lon={lon}")

                                                                      