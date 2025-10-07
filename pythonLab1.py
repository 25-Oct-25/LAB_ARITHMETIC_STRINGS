sent = "Hello my name is Norah and i'm excited because i joined this bootcamp"
word = "excited"

print(f"length of the sentence is: {len(sent)}")

print(f"{word} is in the index: {sent.find(word)}")

print(f"{word} appeared {sent.count(word)} time")

print(sent.upper())

print(sent.lower())

new_sent = sent.replace(word, "thrilled")
print(new_sent)

print(f"last character: {sent[-1]}")
