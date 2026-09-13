sentence = input("Write the sentence: ")

separete = list(sentence)
counter_vowel = 0

for lyric in separete:
    if (lyric == "a" or lyric == "e" or lyric == "i" or lyric == "o" or lyric == "u"):
        counter_vowel += 1


print(f"There is {counter_vowel} vowels in the sentence")