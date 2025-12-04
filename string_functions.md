## Core transformation & formatting
| Method                                        | What it does                                | Example                                            | Special errors / corner cases                                                                                                                |
| --------------------------------------------- | ------------------------------------------- | -------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| `s.capitalize()`                              | First char uppercase, rest lowercase.       | `"hello world".capitalize()` → `'Hello world'`     | –                                                                                                                                            |
| `s.casefold()`                                | Lowercase aggressively (for comparisons).   | `"ß".casefold()` → `'ss'`                          | –                                                                                                                                            |
| `s.center(width, fillchar=' ')`               | Pad both sides to given width.              | `"hi".center(6, "-")` → `'--hi--'`                 | `TypeError` if `width` not int / `fillchar` not 1-char str.                                                                                  |
| `s.encode(encoding='utf-8', errors='strict')` | Encode to bytes.                            | `"hi".encode("utf-8")` → `b'hi'`                   | `LookupError` if encoding unknown; `UnicodeEncodeError` if chars can’t be encoded and `errors='strict'`.                                     |
| `s.expandtabs(tabsize=8)`                     | Replace `\t` with spaces.                   | `"a\tb".expandtabs(4)` → `'a   b'`                 | `TypeError` if `tabsize` not int.                                                                                                            |
| `s.format(*args, **kwargs)`                   | Advanced formatting with `{}` placeholders. | `"Hi {}".format("Bob")` → `'Hi Bob'`               | `IndexError` (positional index out of range), `KeyError` (missing named key), `ValueError` (bad format spec), `TypeError` (wrong arg types). |
| `s.format_map(mapping)`                       | Like `format`, but uses mapping directly.   | `"{x} {y}".format_map({"x": 1, "y": 2})` → `'1 2'` | `KeyError` if key missing; `ValueError` / `TypeError` similar to `format`.                                                                   |
| `s.lower()`                                   | Return lowercase copy.                      | `"Hi".lower()` → `'hi'`                            | –                                                                                                                                            |
| `s.swapcase()`                                | Swap case of each letter.                   | `"Hi".swapcase()` → `'hI'`                         | –                                                                                                                                            |
| `s.title()`                                   | Title-case (`Each Word Like This`).         | `"hello world".title()` → `'Hello World'`          | –                                                                                                                                            |
| `s.upper()`                                   | Return uppercase copy.                      | `"hi".upper()` → `'HI'`                            | –                                                                                                                                            |
| `s.zfill(width)`                              | Pad on the left with zeros.                 | `"42".zfill(5)` → `'00042'`                        | `TypeError` if `width` not int.                                                                                                              |

## Stripping and padding

Let t = " hi ".

| Method                         | What it does                                   | Example                          | Special errors                                              |
| ------------------------------ | ---------------------------------------------- | -------------------------------- | ----------------------------------------------------------- |
| `s.ljust(width, fillchar=' ')` | Pad on right (left-justify).                   | `"hi".ljust(5, ".")` → `'hi...'` | `TypeError` if `width` not int / `fillchar` not 1-char str. |
| `s.rjust(width, fillchar=' ')` | Pad on left (right-justify).                   | `"hi".rjust(5, ".")` → `'...hi'` | Same as `ljust`.                                            |
| `s.lstrip([chars])`            | Remove leading whitespace or given chars.      | `t.lstrip()` → `'hi  '`          | `TypeError` if `chars` not str/None.                        |
| `s.rstrip([chars])`            | Remove trailing whitespace or chars.           | `t.rstrip()` → `'   hi'`         | Same.                                                       |
| `s.strip([chars])`             | Remove leading & trailing whitespace or chars. | `t.strip()` → `'hi'`             | Same.                                                       |

## Searching & counting

Let s = "hello world".

| Method                                 | What it does                           | Example                             | Special errors                                                     |
| -------------------------------------- | -------------------------------------- | ----------------------------------- | ------------------------------------------------------------------ |
| `s.count(sub[, start[, end]])`         | Count occurrences of substring.        | `"hello".count("l")` → `2`          | – (empty `sub` is allowed).                                        |
| `s.find(sub[, start[, end]])`          | First index of `sub` or `-1`.          | `"hello".find("l")` → `2`           | – (never raises on “not found”).                                   |
| `s.rfind(sub[, start[, end]])`         | Last index of `sub` or `-1`.           | `"abcabc".rfind("abc")` → `3`       | –                                                                  |
| `s.index(sub[, start[, end]])`         | Like `find`, but raises if not found.  | `"hello".index("e")` → `1`          | `ValueError` if `sub` not found.                                   |
| `s.rindex(sub[, start[, end]])`        | Like `rfind`, but raises if not found. | `"abcabc".rindex("abc")` → `3`      | `ValueError` if `sub` not found.                                   |
| `s.startswith(prefix[, start[, end]])` | Test prefix.                           | `"hello".startswith("he")` → `True` | `TypeError` if prefix is wrong type (must be str or tuple of str). |
| `s.endswith(suffix[, start[, end]])`   | Test suffix.                           | `"hello".endswith("lo")` → `True`   | Same as `startswith`.                                              |

## Splitting & joining

| Method                            | What it does                                | Example                                       | Special errors                                                                                                              |
| --------------------------------- | ------------------------------------------- | --------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| `s.split(sep=None, maxsplit=-1)`  | Split into list from the left.              | `"a,b,c".split(",")` → `['a','b','c']`        | `TypeError` if `sep` not str/None or `maxsplit` not int.                                                                    |
| `s.rsplit(sep=None, maxsplit=-1)` | Split into list from the right.             | `"a,b,c".rsplit(",", 1)` → `['a,b','c']`      | Same.                                                                                                                       |
| `s.splitlines(keepends=False)`    | Split at line boundaries.                   | `"a\nb".splitlines()` → `['a','b']`           | `TypeError` if `keepends` not bool.                                                                                         |
| `s.partition(sep)`                | 3-tuple `(head, sep, tail)` at first `sep`. | `"a b c".partition(" ")` → `('a',' ','b c')`  | – (never raises; if not found, returns `(s, '', '')`).                                                                      |
| `s.rpartition(sep)`               | 3-tuple at last `sep`.                      | `"a b c".rpartition(" ")` → `('a b',' ','c')` | Same behavior for “not found”.                                                                                              |
| `sep.join(iterable)`              | Join strings with separator.                | `",".join(["a","b","c"])` → `'a,b,c'`         | `TypeError` if any element of iterable is not str (or convertible through `__str__` is *not* used; must actually be `str`). |

## Character classification (is* methods)

Return True or False only; they don’t raise exceptions unless the string object itself is invalid (which won’t happen in normal code).

Let s = "abc123".

| Method             | What it checks                                      | Example                            |
| ------------------ | --------------------------------------------------- | ---------------------------------- |
| `s.isalnum()`      | All chars alphanumeric, string not empty.           | `"abc123".isalnum()` → `True`      |
| `s.isalpha()`      | All chars alphabetic, not empty.                    | `"abc".isalpha()` → `True`         |
| `s.isascii()`      | All chars ASCII.                                    | `"abc".isascii()` → `True`         |
| `s.isdecimal()`    | All chars are decimal digits.                       | `"123".isdecimal()` → `True`       |
| `s.isdigit()`      | All chars are digits (includes superscripts etc.).  | `"²3".isdigit()` → `True`          |
| `s.isidentifier()` | Valid Python identifier.                            | `"my_var".isidentifier()` → `True` |
| `s.islower()`      | At least one cased char, all cased chars lowercase. | `"abc".islower()` → `True`         |
| `s.isnumeric()`    | All chars numeric (includes fractions, etc.).       | `"¾".isnumeric()` → `True`         |
| `s.isprintable()`  | All chars printable or string empty.                | `"abc\n".isprintable()` → `False`  |
| `s.isspace()`      | All chars whitespace, not empty.                    | `"   ".isspace()` → `True`         |
| `s.istitle()`      | Titlecase (`Each Word Like This`).                  | `"Hello World".istitle()` → `True` |
| `s.isupper()`      | At least one cased char, all cased chars uppercase. | `"ABC".isupper()` → `True`         |

Note: These never raise errors for “content” (e.g. weird Unicode) – they just return True/False

## Prefix / suffix helpers (Python 3.9+)

| Method                   | What it does              | Example                                          | Special errors                   |
| ------------------------ | ------------------------- | ------------------------------------------------ | -------------------------------- |
| `s.removeprefix(prefix)` | Remove prefix if present. | `"HelloWorld".removeprefix("Hello")` → `'World'` | `TypeError` if `prefix` not str. |
| `s.removesuffix(suffix)` | Remove suffix if present. | `"HelloWorld".removesuffix("World")` → `'Hello'` | Same.                            |

## Translation / replacement

| Method                             | What it does                                         | Example                                               | Special errors / corner cases                                                                                                     |
| ---------------------------------- | ---------------------------------------------------- | ----------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| `s.replace(old, new[, count])`     | Replace `old` with `new` (optionally limit `count`). | `"aabb".replace("a","x")` → `'xxbb'`                  | `TypeError` if `old`/`new` not str or `count` not int.                                                                            |
| `str.maketrans(x, y=None, z=None)` | Build translation table for `translate()`.           | `tbl = str.maketrans("ab","xy")`                      | `ValueError` if `x` and `y` have different lengths; `TypeError` for invalid types (e.g. non-str keys that can’t be converted).    |
| `s.translate(table)`               | Map chars via translation table.                     | `"abc".translate(str.maketrans("ab","xy"))` → `'xyc'` | `TypeError` if `table` isn’t a mapping/sequence with `__getitem__`; `ValueError` if mapping gives codepoint out of Unicode range. |

## Miscellaneous

| Method             | What it does                                   | Example | Special errors |
| ------------------ | ---------------------------------------------- | ------- | -------------- |
| `s.join(iterable)` | Already covered above under splitting/joining. | –       | –              |
| `s.encode(...)`    | Already covered above.                         | –       | –              |
