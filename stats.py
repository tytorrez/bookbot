def get_book_words(book_content):
    book_words = book_content.split()
    num_words = len(book_words)

    return num_words

def get_character_dictionary(book_content):
    character_dictionary = {}
    book_characters = list(book_content.lower())

    for character in book_characters:

        if character in character_dictionary:
            character_dictionary[character] += 1
        else:
            character_dictionary[character] = 1

    return character_dictionary

def get_sorted_list(character_dictionary):

    dictionary_list = []
    for key in character_dictionary:

        if key.isalpha():

            new_character_dictionary = {}
            new_character_dictionary["char"] = key
            new_character_dictionary["num"] = character_dictionary[key]
            dictionary_list.append(new_character_dictionary)

    dictionary_list.sort(reverse=True, key=sort_on)
    
    return dictionary_list

def sort_on(items):
    return items["num"]


