sentence = "Python is a high-level, Python's syntax allows developers  makes it an excellent choice for beginners and experienced programmers alike"
word = "Python"
new_word = ("Java")



print(len(sentence))
print(sentence.index(word))
print(sentence.count(word))
print(word.upper())
print(word.lower())

word_replace = sentence.replace(word, new_word)
print(word_replace)
print(sentence[-1])