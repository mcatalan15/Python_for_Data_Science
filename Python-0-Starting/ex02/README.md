# Python Piscine - Module 00: Exercise 02 (First function python)

## Purpose of the Code

The goal of this exercise is to create a dynamic type-checking function (`all_thing_is_obj`) that identifies the data type of any incoming object, prints a formatted message specific to that type, and consistently returns the integer `42`.

---

## Core Concept: Structural Pattern Matching (`match / case`)

This solution leverages **Structural Pattern Matching**, a powerful feature introduced in **Python 3.10**.

Unlike a traditional chain of `if/elif/else` statements, `match/case` does not just check for equality; it evaluates the **structure** and **type** of the data.

### How the Type Cases Work

* **`case list():` / `case tuple():` / `case set():` / `case dict():**`
By appending parentheses `()` to the type name inside a `case`, Python checks if the object is an *instance* of that specific class. This is equivalent to checking `isinstance(object, list)`.
* **`case str():`**
Matches when the argument is a string. Following the 42 custom rule (a nod to the classic English-learning joke *"Brian is in the kitchen"*), it extracts the content of the string and prints it alongside its class type.
* **`case _:` (The Wildcard)**
The underscore `_` acts as a catch-all (similar to `default:` in a C `switch` statement). If the object doesn't match any of the explicitly listed data structures (like an integer `10`), it falls into this case and prints `"Type not found"`.

---

## 🛠️ Code Specifics & Refinements

```python
def all_thing_is_obj(object: any) -> int:
    match object:
        case list():
            print("List :", type(object))
        case tuple():
            print("Tuple :", type(object))
        case set():
            print("Set :", type(object))
        case dict():
            print("Dict :", type(object))
        case str():
            print(f"{object} is in the kitchen : {type(object)}")
        case _:
            print("Type not found")
    return (42)

```

### Key Highlights for Peer-Evaluation:

1. **No Global Scope execution:** The script only defines the function. If executed alone (`python find_ft_type.py`), it outputs nothing, as required.
2. **Explicit spacing:** Ensured that `"Dict :"` contains the colon inside the string to guarantee identical formatting across all native collections.
3. **Type Hinting:** Uses `object: any -> int` to explicitly document the function's expected input type and return behavior, aligned with modern Python best practices.
