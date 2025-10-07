full_name = "Hind Abdullah"
first_name = "Hind"

print(f"Length of the sentence: {len(full_name)} \n")

print("Index of the first occurrence of the word:", full_name.find(first_name) ,"\n")

print("Number of times the word appears:", full_name.count(first_name),"\n")

print("Sentence in uppercase:", full_name.upper(),"\n")

print("Sentence in lowercase:", full_name.lower(),"\n")

new_name = full_name.replace(first_name, "Haya")
print("Sentence after replacement:", new_name,"\n")

print("Last character of the sentence:", full_name[-1])

