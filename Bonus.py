# Bonus Assignment
sentence = "Python programming is fun and helps develop problem solving skills"

word = "Python"

print("Length of the sentence:", len(sentence))

print("Index of the first occurrence of the word:", sentence.find(word))

print("Number of times the word appears:", sentence.count(word))

print("Sentence in uppercase:", sentence.upper())

print("Sentence in lowercase:", sentence.lower())

new_sentence = sentence.replace(word, "Programming")
print("Sentence after replacement:", new_sentence)

print("Last character of the sentence:", sentence[-1])
