sentence = "Quick brown fox jumps over the lazy dog."

print(sentence)

word_to_remove = input("\nEnter the word to be removed: ").lower()

if word_to_remove in sentence.lower():
    start_index = sentence.lower().index(word_to_remove)
    print(sentence[: start_index] + sentence[start_index + len(word_to_remove) + 1 :])
