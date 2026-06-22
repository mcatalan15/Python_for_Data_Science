# Python Piscine - Module 00: Exercise 06 (Recode filter)

## Purpose of the Code

This exercise introduces a advanced structural breakdown split into two interconnected files:

1. `ft_filter.py`: A precise functional replicate of Python's built-in `filter()` iterator, constructed strictly using list comprehensions.
2. `filterstring.py`: A terminal executable that tokenizes a user-provided string $S$ into unique word elements, then cleanses and retains only the components whose lengths are strictly greater than an integer $N$.

---

## 🧠 Core Concepts & Advanced Logic

### 1. Recreating the Iterator Pattern (`ft_filter.py`)

The native `filter()` mechanism in Python is highly optimized because it does not allocate memory for a complete array immediately upon execution. Instead, it creates a **filter object** (an iterator).

* To ensure `ft_filter.py` behaves identically, the code structures a conditional list comprehension to capture matching or truthy elements and subsequently returns `iter(result)`.
* This yields items sequentially when unpacked or iterated elsewhere, conserving RAM footprint.

### 2. Complying with PEP 8 Lambda Constraints (`E731`)

The Python styling standard (PEP 8) strongly advises against assigning lambda symbols to local named variables (e.g., `func = lambda x: x`). Doing so destroys the primary benefit of lambdas: being anonymous.

* To appease the validator `flake8` while obeying the project mandate to incorporate a lambda statement, the anonymous expression is mapped **inline** inside the parameters of the execution engine:
```python
result = [word for word in ft_filter(lambda w: len(w) > n_size, words)]

```



### 3. Structural Word Breakdown

* **`str.split()`**: Efficiently parses sentences by whitespace blocks while natively sanitizing duplicate spacing bugs.
* **`str.isdigit()` Guard**: Essential validation metric ensuring that strings composed entirely of numeric characters (e.g., `"123"`) do not pass into word evaluation logic as valid text parameters.
