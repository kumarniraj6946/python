
text = "Hello, World!"

text = text.lower()

consonants = ""

for char in text:
    if char.isalpha() and char not in "aeiou":
        consonants += char

print("Consonants:", consonants)
