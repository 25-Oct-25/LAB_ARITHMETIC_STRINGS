sentence = "Hello, My name is Ziad, i am 23 years old, and i love programming"
word = "Ziad"
index = sentence.find(word)
count = sentence.count(word)
upper_sentence = sentence.upper()
lower_sentence = sentence.lower()

replaced_sentence = sentence.replace("Ziad", "Saad")

print("The length of the sentence :",len(sentence))
print("The word", word, "starts at index", index)
print("The number of times the word", word, "appears is", count)
print("\n", upper_sentence)
print("\n", lower_sentence)
print("\n", replaced_sentence)
print("\n", sentence[-1])
