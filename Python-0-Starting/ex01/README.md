# Python Piscine - Module 00: Exercise 01 (First use of package)

## Purpose of the Code

This script retrieves the current date and time to output it in two specific formats required by the subject:

1. The number of seconds elapsed since **January 1, 1970 (Unix Epoch)**, displayed both with thousands separators/fixed decimals and in scientific notation.
2. The current date formatted as `Mmm dd yyyy` (e.g., `Oct 21 2022`).

---

## Code Breakdown & Logic

1. **`datetime.now()`**: Captures the exact local date and time of execution.
2. **`current_time - start_date`**: In Python, subtracting two `datetime` objects returns a `timedelta` object representing the duration between them.
3. **`delta.total_seconds()`**: A built-in method of `timedelta` that computes the total duration strictly converted into seconds (including fractional milliseconds).
4. **`strftime("%b %d %Y")`**: Formats the date object into a string using specific directives:
* `%b`: Abbreviated month name (e.g., Jan, Oct, Jun).
* `%d`: Day of the month as a zero-padded decimal number.
* `%Y`: Year with century as a decimal number (4 digits).



---

## Deep Dive: String Formatting (`f-strings`)

The core of this exercise is mastering Python's **String Format Specification Mini-Language** inside `f-strings`. The syntax follows the structure `{variable:format_spec}`.

### Case 1: `{total_secs:,.4f}`

This format specifier is broken down into three distinct instructions applied in sequence:

* **`:`** -> Separator that signals the start of the formatting rules.
* **`,`** -> **The Thousands Separator.** Automatically places a comma every three digits to the left of the decimal point (e.g., turning `1666355857` into `1,666,355,857`).
* **`.4`** -> **Precision Control.** Tells Python exactly how many digits to display after the decimal point.
* **`f`** -> **Fixed-point notation.** Treats the value strictly as a standard decimal floating-point number rather than switching to shorthand notations.

### Case 2: `{total_secs:.2e}`

*(Note: To perfectly match the subject's `1.67e+09` output, ensure you add `.2` before the `e`)*

* **`.2`** -> **Precision Control.** Specifies that exactly 2 decimal places should be kept after the leading non-zero digit.
* **`e`** -> **Scientific Notation.** Converts the number into exponential notation (e.g., `1781094559` becomes `1.78e+09`). It automatically rounds the last visible digit based on the numbers dropped.

---

## 💡 Quick Cheat Sheet for Peer-Evaluations

| Syntax | Input Example | Output Result | Description |
| --- | --- | --- | --- |
| `{val}` | `12345.6789` | `12345.6789` | Raw unformatted string. |
| `{val:,}` | `12345.6789` | `12,345.6789` | Adds commas, keeps raw decimals. |
| `{val:.2f}` | `12345.6789` | `12345.68` | Limits to 2 decimals (rounds up). |
| `{val:,.4f}` | `12345.6789` | `12,345.6789` | Commas + exactly 4 decimals. |
| `{val:.2e}` | `12345.6789` | `1.23e+04` | Scientific notation with 2 decimals. |

---