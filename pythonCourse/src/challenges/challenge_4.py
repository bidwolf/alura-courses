"""The fourth challenge module about lists and for loop"""


def challenge_4():
    """The fourth challenge"""

    # 1 . create a people based dictionary with name age and city

    people = {"name": "jon", "age": 13, "city": "belo horizonte"}
    print(people)

    # 2.1 update some item

    people["age"] = 20
    print(people)

    # 2.2 add some key/value

    people.setdefault("sex", "M")
    print(people)

    # 2.3 remove a item

    people.pop("age")
    print(people)

    # 3 . creates a dictionary with numbers and their squared numbers

    square_numbers_dictionary = {}
    for i in range(1, 6):
        square_numbers_dictionary.update({str(i): str(i**2)})
    print(square_numbers_dictionary)

    # 4 . create a dictionary and verify if a key exists in this dictionary

    dictionary_football_teams = {"1": "atlético", "2": "palmeiras", "3": "botafogo"}
    print(
        "the cruzeiro FC",
        "is" if "cruzeiro" in dictionary_football_teams.values() else "is not",
        "the best team in the world",
    )
    print(
        "the atlético",
        "is" if "atlético" in dictionary_football_teams.values() else "is not",
        "the best team in the world",
    )

    # 5 . word frequency in a dictionary

    phrase = (
        "Our deepest wishes are whispers of our authentic selves."
        + " We must learn to respect them. We must learn to listen."
    )
    word_list = list(phrase.replace(".", "").split(" "))
    word_occurrences = {}
    for word in word_list:
        if word_occurrences.get(word) is None:
            word_occurrences.setdefault(word, 1)
        else:
            word_occurrences.update({word: word_occurrences.get(word) + 1})
    print(word_occurrences)
