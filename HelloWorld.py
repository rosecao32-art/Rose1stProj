def main():
    print("Hello World!!! It is great.")

main()

text = "HELLO Word 123!"
result = text.lower()
print(result)

p1 = "AbC123"
p2 = "abc123"
print(p1.lower() == p2.lower())

txt = "Machine Learning with PYTHON"
keyword = "python"
print(keyword.lower() in txt.lower())

import sys
for p in sys.path:
    print(p)