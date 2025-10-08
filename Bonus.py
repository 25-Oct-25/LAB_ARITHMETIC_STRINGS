sentence = "Learning Python is fun and helps improve loqical thinking skills quickly."
word = "Python"

print("Length of sentence:", len(sentence))
print("Index of first occurrence of the word:", sentence.find(word))
print("Number of times the word appears:",sentence.count(word))
print("Uppercase:", sentence.upper())
print("Lowercase:", sentence.lower())

new_sentence = sentence.replace(word, "Coding")
print("After replacement:", new_sentence)
print("Last character:", sentence[-1])
