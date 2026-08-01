import re

# Regex to capture log levels like [INFO], [WARNING], [ERROR]
pattern = re.compile(r"""

\[(INFO|WARNING|ERROR)\]

""")

info_count = 0
warning_count = 0
error_count = 0

chunk_size = 4096  # 4 KB chunks
buffer = ""        # holds incomplete lines between chunks

with open("system_log.txt", "r", encoding="utf-8") as f:
    while True:
        chunk = f.read(chunk_size)
        if not chunk:
            break

        buffer += chunk

        # Split into lines — last line may be incomplete
        lines = buffer.split("\n")

        # Keep the incomplete last line in buffer
        buffer = lines.pop()

        for line in lines:
            match = pattern.search(line)
            if match:
                level = match.group(1)
                if level == "INFO":
                    info_count += 1
                elif level == "WARNING":
                    warning_count += 1
                elif level == "ERROR":
                    error_count += 1

# Process any leftover line in buffer
if buffer:
    match = pattern.search(buffer)
    if match:
        level = match.group(1)
        if level == "INFO":
            info_count += 1
        elif level == "WARNING":
            warning_count += 1
        elif level == "ERROR":
            error_count += 1

print("Summary:")
print("INFO:", info_count)
print("WARNING:", warning_count)
print("ERROR:", error_count)
