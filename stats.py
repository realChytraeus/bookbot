def count_words(text):
    # Split the text into words
    words = text.split()
    # Return the count of words
    return len(words)


def count_chars(text):
    # Create an empty dictionary to store character counts
    chars_dict = {}

    for char in text:
        # Convert to lower case
        char = char.lower()

        # If we've seen this character before, increment its count
        # If not, add it to the dictionary with a count of 1
        if char in chars_dict:
            chars_dict[char] += 1
        else:
            chars_dict[char] = 1

    # Return the dictionary of character counts
    return chars_dict


def sort_characters_by_count(char_counts):
    char_list = []
    for key, value in char_counts.items():
        char_list.append({"char": key, "count": value})

    # Sort the list by the "count" value in descending order
    char_list.sort(key=lambda d: d["count"], reverse=True)

    return char_list
