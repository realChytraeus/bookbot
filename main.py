import sys, stats


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents


def main():
    # Load the text of "frankenstein.txt"
    # book_text = get_book_text("books/frankenstein.txt")

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    book_text = get_book_text(book_path)

    # Count the words and characters
    word_count = stats.count_words(book_text)
    # Add this line to call your count_chars function
    char_count = stats.count_chars(book_text)

    # print(book_text)

    # print(f"{word_count} words found in the document")

    # print("\nCharacter Counts:")
    # for char, count in char_count.items():
    #    print(f"'{char}': {count}")

    sorted_char_count = stats.sort_characters_by_count(char_count)

    # Print the report
    print("============ BOOKBOT ============")
    print(f"Analyzing book found a books/frankenstein.txt...")
    print("------------ Word Count ------------")
    print(f"Found {word_count} total words")
    print(f"------------ Character Count ------------")

    # Filter and print only alphabetical character counts
    for entry in sorted_char_count:
        char = entry["char"]
        count = entry["count"]
        if char.isalpha():  # Skip non-alphabet characters
            print(f"{char}: {count}")

    print("============ END ============")


main()
