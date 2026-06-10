# Python Piscine - Module 00: Exercise 00 (Starting)

## Purpose of the Code
This script demonstrates the foundational concepts of **Data Types** and **Mutability** in Python 3.10. It modifies four distinct built-in collections (`list`, `tuple`, `set`, and `dict`) to output a standardized greeting matching a specific 42 Campus format.

---

## Core Concepts & Methods Learned

### 1. Lists (`list`) - Mutable & Ordered
* **Behavior:** Elements can be accessed and altered directly using their index.
* **Modification:** Direct assignment (`ft_list[1] = "World!"`).

### 2. Tuples (`tuple`) - Immutable & Ordered
* **Behavior:** Cannot be changed once created. Attempting to assign a value directly via index throws a `TypeError`.
* **Workaround:** Cast the tuple into a mutable object (`list`), apply changes via index, and cast it back into a `tuple`.

### 3. Sets (`set`) - Mutable & Unordered
* **Behavior:** Holds unique elements without an index or fixed position. 
* **Traps Avoided:** * Using `.update("String")` iterates through each character individually (e.g., `'B'`, `'a'`, `'r'`).
  * Using `.add("String")` correctly treats the string as a single cohesive element.
* **Modification:** Element removal with `.remove()` followed by `.add()`.

### 4. Dictionaries (`dict`) - Mutable Key-Value Pairs
* **Behavior:** Accessible through unique identifier keys rather than numbered positions.
* **Modification:** Modifying values can be performed cleanly via key assignment or using the `.update({"Key": "Value"})` method.

---

## Summary Checklist for Peer-Evaluations
- [ ] Ensure Python `3.10` is explicitly configured.
- [ ] No global variables or code outside explicit wrappers (applicable from Ex04+).
- [ ] Data structures must match the exact primitive output formats required by the subject.
