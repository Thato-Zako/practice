import string


def count_words(inp):
    i = 0
    word_count = {}
    if inp == "":
        return print("No values inserted")
    else:
        words = inp.lower().split()
        for word in words:
            clean_word = word.strip(string.punctuation)
            if clean_word in word_count:
                word_count[clean_word] += 1
            else:
                word_count[clean_word] = 1

    return word_count


Test: str = " My day was a really really good. day!"
print(count_words(Test))