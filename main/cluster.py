import string


def dict_search(word, dictionary):
    if word in dictionary:
        dictionary[word] += 1
    else:
        dictionary.update({word: 1})
    return dictionary


def clean(text):
    for char in string.punctuation:
        text = text.replace(char, "")
    text = text.split()
    text = text.lower()
    return text


def cluster():
    source_text_path = str(input("Please input file path: "))
    source_text = open(source_text_path, encoding="utf8")
    source_text_content = source_text.read()
    source_text.close()
    proximity = int(input("Please input proximity: "))
    target_word = input("Please input target word: ")
    clean_text = clean(source_text_content)
    word_count = len(clean_text)
    data_dict = {}

    for i in range(0, word_count):
        # left edge case
        if clean_text[i] == target_word and i < proximity:
            for j in range(1, proximity + 1):
                data_dict = dict_search(clean_text[i + j], data_dict)
            for j in range(1, i + 1):
                dict_search(clean_text[i - j], data_dict)

        # right edge case
        elif clean_text[i] == target_word and word_count - i <= proximity:
            for j in range(1, proximity + 1):
                data_dict = dict_search(clean_text[i - j], data_dict)
            for j in range(1, word_count - i):
                data_dict = dict_search(clean_text[i + j], data_dict)

        # general case
        elif clean_text[i] == target_word:
            for j in range(1, proximity + 1):
                data_dict = dict_search(clean_text[i + j], data_dict)
                data_dict = dict_search(clean_text[i - j], data_dict)
    print(data_dict)


cluster()
