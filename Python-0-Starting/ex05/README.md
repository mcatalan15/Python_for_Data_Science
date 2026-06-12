# Python Piscine - Module 00: Exercise 05 (First standalone program python)

## Purpose of the Code

This application, `building.py`, evaluates an incoming or interactively prompted text block. It processes the total character count and isolates them into five granular classifications: upper-case letters, lower-case letters, digits, spaces (including carriage returns), and system punctuation Marks.

---

## 🧠 Core Concepts & Advanced Logic Explained

### 1. Generator Expressions (The Inline `for` loop)

Instead of allocating space in memory for an entire list using traditional list comprehensions `[1 for c in text ...]`, this code utilizes **Generator Expressions** `(1 for c in text ...)`.

A generator expression evaluates items **lazily** (one by one) on demand, rather than creating the whole array in RAM at once. This makes it highly efficient for processing massive text strings.

### 2. The `sum()` Operator Trick

The standard syntax used here is:

```python
upper_count = sum(1 for c in text if c.isupper())

```

#### How it works step-by-step:

1. The generator loops through the string character by character (`for c in text`).
2. It evaluates the filtering condition (e.g., `if c.isupper()`).
3. If the character is indeed an upper-case letter, the generator yields a `1`. If it's false, it yields nothing.
4. The `sum()` function takes this stream of `1`s and adds them up in real-time, effectively giving you the total count.

---

## 💻 Structure of the Solution

```python
import sys
import string


def filter(text: str):
    """
    Counts character types using sum() generator expressions and built-in methods.
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
    Validates terminal inputs. Prompts for dynamic input using input()
    if no argument is found.
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

```

---

## 📋 Peer-Evaluation Verification Matrix

* **Interactive Trigger:** Executing `python building.py` without arguments should actively trigger the console input question (`What is the text to count?`).
* **Multi-argument Safeguard:** Giving two separate quoted strings will actively raise the `AssertionError: more than one argument is provided` code string.
* **White-spaces Count:** Escape markers like `\n` or `\t` must safely register inside the `space_count` tally.
