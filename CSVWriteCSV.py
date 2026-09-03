import csv
with open("out.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Age"])
    writer.writerow(["Alice", 30])
    writer.writerow(["Billy", 31])
    writer.writerow(["Cathy", 9])
    writer.writerow(["Dany", 7])        
    writer.writerow(["Ellen", 5])

    