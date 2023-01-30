import re

old_word_Count = []
water_word_count = []
sentence_lengths = []

with open("Moby_Dick_Chapter_1.txt", "r", encoding="utf8") as input_file:
    for line in input_file:
        line = line.lower()
        old_word_Count.append(len(re.findall(r'old', line)))
        water_word_count.append(len(re.findall(r'water', line)))

        # determine average sentence length
        sentences = re.split(r'[.!?]', line)
        for sentence in sentences:
            words = re.split(r'\s+', sentence)
            sentence_lengths.append(len(words))

    print("The word 'old' appears", sum(old_word_Count), "times in the text.")
    print("The word 'water' appears", sum(water_word_count), "times in the text.")
    print("The average sentence length is", int(sum(sentence_lengths) / len(sentence_lengths)), "words.")

print("-----------------------------")

with open("Sense_And_Sensibility_Chapter_1.txt", "r", encoding="utf8") as input_file:
    for line in input_file:
        line = line.lower()
        old_word_Count.append(len(re.findall(r'old', line)))
        water_word_count.append(len(re.findall(r'water', line)))

        # determine average sentence length
        sentences = re.split(r'[.!?]', line)
        for sentence in sentences:
            words = re.split(r'\s+', sentence)
            sentence_lengths.append(len(words))

    print("The word 'old' appears", sum(old_word_Count), "times in the text.")
    print("The word 'water' appears", sum(water_word_count), "times in the text.")
    print("The average sentence length is", int(sum(sentence_lengths) / len(sentence_lengths)), "words.")