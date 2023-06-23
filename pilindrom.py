word = input("Напишите слово: ")


def polindrom(word):
    if word.lower() == word.lower()[::-1]:
        print(True)
    else:
        print(False)

polindrom(word=word)