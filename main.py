def main():
    # Open and read the file
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

        # Create empty dictionary
        letter_count = {}

        # Convert to lowercase
        file_contents = file_contents.lower()

        # Loop through each letter
        for l in file_contents:
            if l.isalpha():

                 # If letter exists in dictionary, add 1 to its count
                if l in letter_count:
                    letter_count[l] += 1

                    
                # If it doesn't exist, set its count to 1
                else:
                    letter_count[l] = 1

        # print "Frankenstein" text
        print(file_contents)

        # print empty line for readability
        print()

        # print the number of words
        wl = file_contents.split()
        print(len(wl))

        # print empty line for readability
        print()

        # print the dictionary
        print(letter_count)

        # print empty line for readability
        print()

        print("--- Begin a report of books/frankenstein.txt ---")
        print(f"{len(wl)} words found in the document.")
        print()

# Function to extract the value part of a tuple
    def get_value(item):
        return item[1]

    # create a variable, sorted_items, .items() creates a list of tuples
    # from the dictionary. sorted() sorts the dictionary using your function
    # get_value by passing the key=get_value() which means sort by using the
    # number in the dictionary's key-value pairs. reverse=True tells it to
    # do so in descending order.
    sorted_items = sorted(letter_count.items(), key=get_value, reverse=True)

    # now a for loop to iterate over your list of tuples
    for item in sorted_items:
        letter = item[0] # First element: the letter
        frequency = item[1] # Second element: the frequency
        print(f"The '{letter}' character was found {frequency} times")

main()

