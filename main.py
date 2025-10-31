import sys
from stats import *

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
book_path = sys.argv[1]

def get_book_text(book_path):
    with open(book_path, 'r', encoding='utf-8') as file:
        return file.read()

def main():
    book_text = get_book_text(book_path)
    num_words = count_words(book_text)
    print("============ BOOKBOT ============\n")
    print(f'Analyzing book found at {book_path}...\n')
    print("----------- Word Count ----------\n")
    print(f"Found {num_words} total words\n")
    print("--------- Character Count -------\n")
    char_counts = count_characters(book_text)
    sorted_char_counts = sort_character_counts(char_counts)
    for char_info in sorted_char_counts:
        print(f"{char_info['character']}: {char_info['count']}")
    print("============= END ===============")
main()