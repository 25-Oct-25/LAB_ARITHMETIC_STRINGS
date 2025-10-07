# Define a string variable containing a sentence with at least 10 words.
sentence = "Abdulrahman Turki Al-harbi is a computer science graduate who loves coding and design"

# Define a string variable containing a word that appears in the sentence.
word = "coding"

# Print the length of the sentence.
print(f"The length of the sentence is: {len(sentence)}",'\n')

# Print the index of the first occurrence of the word in the sentence.
print(f"The index of the first occurrence of '{word}' is: {sentence.find(word)}",'\n')

# Print the number of times the word appears in the sentence.
print(f"The word '{word}' appears {sentence.count(word)} time in the sentence.",'\n')

# Print the sentence in all uppercase letters.
print("Sentence in uppercase:", sentence.upper(),'\n')

# Print the sentence in all lowercase letters.
print("Sentence in lowercase:", sentence.lower(),'\n')

# Replace the word in the sentence with a new word of your choice.
new_sentence = sentence.replace(word, "development")
print("After replacing the word:", new_sentence,'\n')

# Print the last character of the sentence.
print("The last character of the sentence is:", sentence[-1])