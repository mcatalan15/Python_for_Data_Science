# Python Piscine - Module 00: Exercise 03 (NULL not found)

## Purpose of the Code

The goal of this exercise is to write a function `NULL_not_found` that identifies various falsy, empty, or null-like values in Python, prints a specific formatted message for each, and manages strict returns (`0` for success, `1` for unrecognized types).

---

## 🧠 Core Concepts & The Hidden Traps

This exercise is designed by 42 to test your knowledge of edge cases in Python's type system, focusing on three major traps:

### 1. The Unique Behavior of `NaN` (Not a Number)

In Python (and IEEE 754 floating-point math), `float("NaN")` represents an undefined numerical value. It has a unique logical characteristic: **it is never equal to itself.**

```python
>>> float("NaN") == float("NaN")
False

```

* **Solution:** To detect `NaN` within a `match/case` statement without importing external libraries, we use the guard `if object != object`. Since `NaN` is the only object in Python that fails an identity check against itself, this condition matches it perfectly.

### 2. Strict Type Ordering (`bool` vs `int`)

In Python, the `bool` class is an exact subclass of `int`. Internally, `False` is represented as `0`.
If an explicit type check or `match/case` evaluates `int` before `bool`, the value `False` will be mistakenly caught by the integer case.

* **Solution:** We place `case bool():` strictly **before** `case int():` to ensure boolean objects are intercepted first.

### 3. Variable Names vs Static Output (The "Garlic" Trick)

The provided `tester.py` names its `NaN` variable `Garlic`. However, the exercise manual states that the output text must explicitly print `Cheese:`. Hardcoding the name checks based on the data type, rather than dynamic variable inspection, is mandatory to pass.

---

## 💻 Structure of the Solution

```python
def NULL_not_found(object: any) -> int:
    match object:
        case bool() if object is False:
            print(f"Fake: {object} {type(object)}")
        case int() if object == 0:
            print(f"Zero: {object} {type(object)}")
        case None:
            print(f"Nothing: {object} {type(object)}")
        case str() if object == "":
            print(f"Empty: {type(object)}")
        case float() if object != object:
            print(f"Cheese: {object} {type(object)}")
        case _:
            print("Type not Found")
            return 1
    return 0

```

---

## 📋 Summary Table for Peer-Evaluations

| Input Value | Detected Case | Printed Label | Return Value | Notes |
| --- | --- | --- | --- | --- |
| `None` | `None` | `Nothing:` | `0` | Standard Null pointer in Python. |
| `float("NaN")` | `float` (`NaN`) | `Cheese:` | `0` | Evaluated via `object != object`. |
| `0` | `int` | `Zero:` | `0` | Only matches if it didn't pass `bool` first. |
| `""` | `str` | `Empty:` | `0` | Does not print the empty string value inside. |
| `False` | `bool` | `Fake:` | `0` | Caught first to prevent entering the `int` case. |
| `"Brian"` | Wildcard (`_`) | `Type not Found` | `1` | Fallback case for any valid/non-null data. |
