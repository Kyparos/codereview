"""
Написати функцію яка знаходить найменьш використовуємоє слово у тексті(слова з дефісом – це два слова)
"""
import re


def find_text(text: str) -> list:
    """
    return least used words in text
    :param text: str : 'Ha-ha, ur funny!'
    :return: list of str : ['ur','funny']
    """
    raw_words = re.findall('\w+', text)
    for i in range(len(raw_words)):
        temp = str(raw_words[i])
        raw_words[i] = temp.lower()
    least = 0
    words = []
    for word in raw_words:
        temp_least = 0
        for word_t in raw_words:
            if word == word_t:
                temp_least += 1
        if temp_least < least:
            words.clear()
            words.append(word)
            least = temp_least
        elif least == 0:
            words.append(word)
            least = temp_least
        elif temp_least == least:
            words.append(word)
    words.sort()
    return words

