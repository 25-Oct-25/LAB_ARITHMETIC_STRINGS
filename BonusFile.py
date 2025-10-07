#sentence
sentence= "hello my name Abrar Alghamdi I graduated from Princess Norah University"
#word
word= "Abrar"

#Print the length of the sentence
print("length of sentence: ",len(sentence))

#Print the index of the first occurrence of the word in the sentence
print("first occurrence of the word: ",sentence.find(word))

#Print the number of times the word appears in the sentence
print("the word appears: ",sentence.count(word), "times")

#Print the sentence in all uppercase letters
print("uppercase: ",sentence.upper())

#Print the sentence in all lowercase letters.
print("lowercase: ",sentence.lower())

#Replace the word in the sentence with a new word wich is "hello"
print("Replace word: ",sentence.replace(word, "hello"))

#Print the last character of the sentence.
print("last character of the sentence: ",sentence[-1])

