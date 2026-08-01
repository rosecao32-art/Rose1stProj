info_count = 0
warning_count = 0
error_count = 0

with open("system_log.txt", "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip() #remove newline + spaces

        if line.startswith("[INFO]"):
            info_count += 1
        elif line.startswith("[WARNING]"):
            warning_count += 1
        elif line.startswith("[ERROR]"):
            error_count += 1

print("Summary:")
print("INFO:", info_count)
print("WARNING:", warning_count)
print("ERROR:", error_count)
