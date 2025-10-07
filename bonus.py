sentence = "Ella Matcha is a delicious drink that keeps you calm and focused all day long."
word = "and"
print("Length of the sentence:", len(sentence))
print("Index of first occurrence of the word:", sentence.find(word))
print("Number of times the word appears:", sentence.count(word))

print("\nSentence in uppercase:", sentence.upper())

# Print the sentence in all lowercase letters
print("Sentence in lowercase:", sentence.lower())

# Replace the word in the sentence with a new word of your choice
new_sentence = sentence.replace(word, "plus")
print("\nSentence after replacement:", new_sentence)

# Print the last character of the sentence
print("Last character of the sentence:", sentence[-1])

