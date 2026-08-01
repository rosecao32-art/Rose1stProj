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

number = 7
for i in range(1, 11):
    if i == number:
        print("Found your number:", i)
        break
    else:
        print("Checking", i)    

programming_languages = ['Rust', 'Java', 'Python', 'C++']

for language in programming_languages:
    print(language)

for char in "code":
    print(char)

categories = ['Fruit', 'Vegetable']
foods = ['Apple', 'Carrot', 'Banana']
for category in categories:
    for food in foods:
        print(category, food)

