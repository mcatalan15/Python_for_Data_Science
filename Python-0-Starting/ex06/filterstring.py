import sys

from ft_filter import ft_filter


def main():
    """
    Main function to filter words from a string based on lenght N.
    """

    # 1. Validate argv quantity (Must be equal to 3)
    if len(sys.argv) != 3:
        raise AssertionError("the arguments are bad")

    # 2. Validate if sys.argv[2] is an entero
    try:
        text = sys.argv[1]
        n_size = int(sys.argv[2])
    except ValueError:
        raise AssertionError("the arguments are bad")

    # 2.2 Check if text contains just numbers
    if text.isdigit():
        raise AssertionError("the arguments are bad")

    # 3. Split the text in a list of words
    words = text.split()

    # 4. Use the ft_filter, a lambda and list comprehension together
    # Save in a list comprehension result from 'words' filter uwing
    # a lambda function that compares len(word) > n_size
    # Apply the ft_filter. Because ft_filter returns an index, we transform the
    # list with list comprehension or making list()
    result = [
        word for word in ft_filter(lambda word: len(word) > n_size, words)
    ]

    print(result)


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print(f"AssertionError: {e}")
