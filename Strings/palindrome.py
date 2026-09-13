sentence = input("Write the word: ")
sentence_lo = sentence.lower()

tam = len(sentence)
word_inverse = []

for i in range(tam-1,-1,-1):
    word_inverse.append(sentence_lo[i])


if sentence_lo == "".join(word_inverse):
    print("Palindrome")

else:
    print("Not Palindrome")