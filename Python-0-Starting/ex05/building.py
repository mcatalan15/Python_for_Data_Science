import sys
import string


def filter(text: str):

    """
    Counts character types using sum() and the for loop and the specific
    function for each type. Also used string.punctuation from string lib.
    """

    upper_count = sum(1 for c in text if c.isupper())
    lower_count = sum(1 for c in text if c.islower())
    digit_count = sum(1 for c in text if c.isdigit())
    space_count = sum(1 for c in text if c.isspace())

    punct_count = sum(1 for c in text if c in string.punctuation)

    total_chars = len(text)

    print(f"The text contains {total_chars} characters:")
    print(f"{upper_count} upper letters")
    print(f"{lower_count} lower letters")
    print(f"{punct_count} punctuation marks")
    print(f"{space_count} spaces")
    print(f"{digit_count} digits")


def main():

    """
    Main function to process the argv lenght and send to filter() or throw
    an error.
    """

    if len(sys.argv) > 2:
        raise AssertionError("more than one argument is provided")

    if len(sys.argv) == 2:
        filter(sys.argv[1])
    else:
        text = input("What is the text to count?\n")
        filter(text)


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print(f"AssertionError: {e}")
