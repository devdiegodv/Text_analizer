text = input('Write something: ')
letters = []

text = text.lower()

letters.append(input("Write the first letter: ").lower())
letters.append(input("Write the second letter: ").lower())
letters.append(input("Write the three letter: ").lower())

print("\n")
print("AMOUNT OF LETTERS")
letters_quantity = text.count(letters[0])
letters_quantity2 = text.count(letters[1])
letters_quantity3 = text.count(letters[2])

print(f"We have found the letter '{letters[0]}' repeated '{letters_quantity}' times")
print(f"We have found the letter '{letters[1]}' repeated '{letters_quantity2}' times")
print(f"We have found the letter '{letters[2]}' repeated '{letters_quantity3}' times")

print("\n")
print("QUANTITY OF WORDS")
words = text.split()
print(f"We have found {len(words)} words in your text")

print("\n")
print("LETTERS FROM START TO END")
letter_start = text[0]
letter_end = text[-1]
print(f"The start letter is '{letter_start}' and the final letter is '{letter_end}'")

print("\n")
print("INVERTED TEXT")
words.reverse()
inverted_text = ' '.join(words)
print(f"If we order your inverted text it would say: '{inverted_text}'")