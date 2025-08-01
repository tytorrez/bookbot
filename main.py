from stats import *
import sys

def get_book_text(file_path):
    with open(file_path) as file:
        book_content = file.read()

    return book_content
    
def main():

    arg_list = sys.argv

    if len(arg_list) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = arg_list[1]
    book_text = get_book_text(book_path)
    book_words = get_book_words(book_text)
    character_dictionary = get_character_dictionary(book_text)
    sorted_list = get_sorted_list(character_dictionary)


    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {book_words} total words")
    print("--------- Character Count -------")

    for i in range(0, len(sorted_list)):
        print(sorted_list[i]["char"]+":", sorted_list[i]["num"])
    
    print("============= END ===============")


main()