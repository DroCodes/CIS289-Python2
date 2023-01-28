def returns_string_list_length(string_list):
    return len(string_list)

word_list = ["word1", "word2", "word3", "word4", "word5", "word6", "word7", "word8", "word9", "word10"]

result = map(returns_string_list_length, word_list)
result_to_list = list(result)

print(result_to_list)

for word in word_list:
    print(len(word))