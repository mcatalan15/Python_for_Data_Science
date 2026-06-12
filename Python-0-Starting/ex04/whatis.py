import sys


def main():

    """
    1. Checks if the argv are less than 2 (return empty)
        or more than 2 (AssertionError).
    2. Try/except to check if the argv given is an int.
    4. Inside the try (is a number) uses the module to check
        if its even or odd.
    """

    if len(sys.argv) < 2:
        return

    if len(sys.argv) > 2:
        raise AssertionError("more than one argument is provided")

    try:
        number = int(sys.argv[1])
        # 5. Calcular si es par o impar.
        if number % 2 == 0:
            print("I'm Even.")
        else:
            print("I'm Odd.")
    except ValueError:
        raise AssertionError("argument is not an integer")


if __name__ == "__main__":

    """
    Used a try/except to capture any exaption that could invalidate the
    exercices. This way we can send the AssertionError.
    """

    try:
        main()
    except AssertionError as e:
        print(f"AssertionError: {e}")
