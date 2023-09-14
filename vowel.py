
text = "Hello, World!"

text = text.lower()

vowels = ""

for char in text:
    if char in "aeiou":
        vowels += char

print("Vowels:", vowels)
