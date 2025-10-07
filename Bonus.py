sentence =  "i am a big fan to Liverpool and Liverpool is better than Manchester United"
print(sentence)


word = "Liverpool"
print(word)

print(len(sentence))

first_index = sentence.find(word)
print(first_index)

print(sentence.upper())

print(sentence.lower())

new_word = "Reds"
replaced_sentence = sentence.replace(word,new_word)
print(replaced_sentence[-1])
