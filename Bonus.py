sentence = "python is a high-level, general-purpose programming language designed by Guido van Rossum and first released in 1995"
word = "python"
print("Length of the sentence: " , len(sentence))
print("First occurrence of word: " , sentence.find(word))
print("Number of times the word appears: " , sentence.count(word))
print("Sentence in all uppercase letters: " , sentence.upper() )
print("Sentence in all lowercase letters: " , sentence.lower() )
print("Replace word: " , sentence.replace( "1995" , "1991" ))
print("The last character of the sentence.: " , sentence[-1] )