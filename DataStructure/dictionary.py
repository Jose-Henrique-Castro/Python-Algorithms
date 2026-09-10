sentence = input("Read the sentence: ")

words = sentence.split()

words_count = {}

for word in words:

    word = word.lower()

    if(word in words_count):
        words_count[word] += 1
    else:
        words_count[word] = 1


for word , count in words_count.items():
    print(f"{word} appears: {count}")