# Summary

| Method                          | In-place?  | Returns  | Key errors / corner cases                                 |
| ------------------------------- | ---------- | -------- | --------------------------------------------------------- |
| `append(x)`                     | ✅ modifies | `None`   | Wrong arg count → `TypeError`                             |
| `extend(iterable)`              | ✅          | `None`   | Non-iterable arg → `TypeError`                            |
| `insert(i, x)`                  | ✅          | `None`   | Non-int index → `TypeError`                               |
| `remove(x)`                     | ✅          | `None`   | Missing element → `ValueError`                            |
| `pop([i])`                      | ✅          | element  | Empty list or bad index → `IndexError`                    |
| `clear()`                       | ✅          | `None`   | Arguments not allowed → `TypeError`                       |
| `count(x)`                      | ❌          | `int`    | Only arg-count `TypeError`                                |
| `index(x[, s[, e]])`            | ❌          | `int`    | Not found → `ValueError`; bad indices → `TypeError`       |
| `reverse()`                     | ✅          | `None`   | Arguments not allowed → `TypeError`                       |
| `sort(key=None, reverse=False)` | ✅          | `None`   | Incomparable elements → `TypeError`; key errors propagate |
| `copy()`                        | ❌          | new list | Arguments not allowed → `TypeError`; shallow copy only    |

# Core mutating methods

## list.append(x)

| Item             | Description                                                                                                       |
| ---------------- | ----------------------------------------------------------------------------------------------------------------- |
| What it does     | Add a single element `x` to the end of the list.                                                                  |
| Example          | `lst.append(4)` → `lst` becomes `[1, 2, 3, 2, 4]`                                                                 |
| Return value     | `None`                                                                                                            |
| Important errors | `TypeError` if wrong number of arguments (e.g. `lst.append()` or `lst.append(1,2)`). No error for any value type. |

## list.extend(iterable)

| Item             | Description                                                                                                |
| ---------------- | ---------------------------------------------------------------------------------------------------------- |
| What it does     | Append all elements from an iterable to the list.                                                          |
| Example          | `lst.extend([5, 6])` → `lst` becomes `[1, 2, 3, 2, 5, 6]`                                                  |
| Return value     | `None`                                                                                                     |
| Important errors | `TypeError` if `iterable` is not actually iterable, e.g. `lst.extend(5)` → `'int' object is not iterable`. |

## list.insert(i, x)

| Item             | Description                                                                                                                                         |
| ---------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| What it does     | Insert `x` at position `i` (shifting elements to the right).                                                                                        |
| Example          | `lst.insert(1, 99)` → `[1, 99, 2, 3, 2]`                                                                                                            |
| Return value     | `None`                                                                                                                                              |
| Important errors | `TypeError` if `i` is not an integer-like value (e.g. `lst.insert("a", 10)`). Index out of range is **not** an error; it just inserts at start/end. |

## list.remove(x)

| Item             | Description                                                       |
| ---------------- | ----------------------------------------------------------------- |
| What it does     | Remove **first occurrence** of `x` from the list.                 |
| Example          | `lst.remove(2)` on `[1, 2, 3, 2]` → `[1, 3, 2]`                   |
| Return value     | `None`                                                            |
| Important errors | `ValueError: list.remove(x): x not in list` if `x` isn’t present. |


## list.pop([i])

| Item                 | Description                                                                                                                                 |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| What it does         | Remove and return element at index `i` (default last).                                                                                      |
| Example              | `lst.pop()` on `[1, 2, 3]` → returns `3`, list becomes `[1, 2]`                                                                             |
| Example (with index) | `lst.pop(0)` on `[1, 2, 3]` → returns `1`, list becomes `[2, 3]`                                                                            |
| Return value         | The removed element.                                                                                                                        |
| Important errors     | `IndexError: pop from empty list` if list is empty; `IndexError: pop index out of range` if index invalid; `TypeError` if `i` not int-like. |

## list.clear()

| Item             | Description                                                          |
| ---------------- | -------------------------------------------------------------------- |
| What it does     | Remove all elements; list becomes empty.                             |
| Example          | `lst.clear()` on `[1, 2, 3]` → `[]`                                  |
| Return value     | `None`                                                               |
| Important errors | `TypeError` if given any argument (must be called as `lst.clear()`). |

# Query & counting

## list.count(x)

| Item             | Description                                                             |
| ---------------- | ----------------------------------------------------------------------- |
| What it does     | Return number of times `x` appears in the list.                         |
| Example          | `[1, 2, 2, 3].count(2)` → `2`                                           |
| Return value     | `int`                                                                   |
| Important errors | `TypeError` only if wrong number of args, not for “uncomparable types”. |


## list.index(x[, start[, end]])

| Item                 | Description                                                                                          |
| -------------------- | ---------------------------------------------------------------------------------------------------- |
| What it does         | Return first index where `x` is found (within [start, end)).                                         |
| Example              | `[1, 2, 3, 2].index(2)` → `1`                                                                        |
| Example (with range) | `[1, 2, 3, 2].index(2, 2)` → `3`                                                                     |
| Return value         | `int`                                                                                                |
| Important errors     | `ValueError: x is not in list` if not found in the slice; `TypeError` if `start`/`end` not int-like. |

# Order & sorting
## list.reverse()

| Item             | Description                                                     |
| ---------------- | --------------------------------------------------------------- |
| What it does     | Reverse the list **in place**.                                  |
| Example          | `lst = [1, 2, 3]; lst.reverse()` → `lst` becomes `[3, 2, 1]`    |
| Return value     | `None`                                                          |
| Important errors | `TypeError` if called with arguments (must be `lst.reverse()`). |

## list.sort(*, key=None, reverse=False)

| Item                            | Description                                                              |
| ------------------------------- | ------------------------------------------------------------------------ |
| What it does                    | Sort the list in place (optionally using `key=` and `reverse=`).         |
| Example                         | `lst = [3, 1, 2]; lst.sort()` → `[1, 2, 3]`                              |
| Example (key)                   | `words = ["bbb", "a", "cc"]; words.sort(key=len)` → `['a', 'cc', 'bbb']` |
| Example (reverse)               | `lst.sort(reverse=True)` → sorted in descending order                    |
| Return value                    | `None`                                                                   |
| Important errors / corner cases |     TypeError if elements can’t be compared (e.g. [1, "a"].sort() in Python 3).

Any exception raised by the key function will propagate.

TypeError if you pass unsupported keyword arguments.                                                                     |

# Copying

## list.copy()

| Item             | Description                                                                                   |
| ---------------- | --------------------------------------------------------------------------------------------- |
| What it does     | Return a **shallow copy** of the list.                                                        |
| Example          | `lst2 = lst.copy()` → `lst2` is a new list with same elements.                                |
| Return value     | New list.                                                                                     |
| Important errors | `TypeError` if called with arguments. Remember: **shallow** copy – nested objects are shared. |

