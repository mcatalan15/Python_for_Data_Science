# Python Piscine - Module 00: Exercise 04 (The Even and the Odd)

## Purpose of the Code

This exercise transitions from creating isolated function modules into building an autonomous, executable command-line script (`whatis.py`). It parses an input argument from the terminal, determines if it is an even or odd integer, and handles execution anomalies using specific structural criteria defined in **Chapter VII**.

---

## 🧠 Core Concepts & Module Evolution

This exercise is heavily gatekept by strict architectural constraints that did not apply to previous exercises:

### 1. Command Line Arguments (`sys.argv`)

In Python, the `sys.argv` list allows programs to capture user input directly from the terminal string.

* `sys.argv[0]` always holds the path/name of the executing script (`whatis.py`).
* `sys.argv[1]` contains the user's explicit parameter.

### 2. Standardizing Scripts via `__main__` Scope

To fulfill the requirement *"No code in the global scope. Use functions!"*, we encapsulate the logical flow entirely within a `main()` function. The application is bootstrapped using:

```python
if __name__ == "__main__":
    main()

```

This protects the script from executing its operational commands automatically if it is imported as a module elsewhere.

### 3. Graceful Error Suppression vs. Explicit Assertions

* **The Empty Flag:** When no argument is given (`len(sys.argv) < 2`), the application must silently succeed with an exit code of 0 without raising text to stdout or stderr.
* **The Typification Check:** Arguments from the terminal always default to the `str` type. Using a `try/except` block attempting an explicit `int()` conversion ensures we accurately intercept formatting faults (like alphanumeric values `Hi!`).

---

## 💻 Structure of the Solution

```python
import sys

def main():
    """
    Parses a single command line argument and prints whether it is even or odd.
    Raises AssertionError for type mismatches or excessive arguments.
    """
    if len(sys.argv) < 2:
        return

    if len(sys.argv) > 2:
        raise AssertionError("more than one argument is provided")

    try:
        number = int(sys.argv[1])
    except ValueError:
        raise AssertionError("argument is not an integer")

    if number % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print(f"AssertionError: {e}")

```

---

## 📋 Peer-Evaluation Assessment Matrix

| Command | Expected Behavior | Operational Output | Status |
| --- | --- | --- | --- |
| `python whatis.py 14` | Matches Even numbers | `I'm Even.` | Success |
| `python whatis.py -5` | Handles negative integers | `I'm Odd.` | Success |
| `python whatis.py` | No arguments provided | *(Blank / Clean Exit)* | Success |
| `python whatis.py Hi!` | Non-numeric input character | `AssertionError: argument is not an integer` | Assert Managed |
| `python whatis.py 13 5` | Multiple inputs given | `AssertionError: more than one argument is provided` | Assert Managed |
