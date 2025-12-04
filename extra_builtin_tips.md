## 1️⃣ Extra built-ins & language tricks

These are tiny but show up *everywhere* in competitive programming / DSA code.

### `any`, `all`, and generator expressions

* `any(cond(x) for x in arr)` – “does *any* element satisfy this?”
* `all(cond(x) for x in arr)` – “do *all* elements satisfy this?”
* Great for quick checks like “is array sorted?”, “is graph bipartite?”, etc.

### Slices and extended slices

* `a[::-1]` – reversed copy of list/string
* `a[i:j]` – subarray / substring
* `a[::2]` – every second element (parity indices, etc.)

### Tuple unpacking and swapping

* `a, b = b, a` – swap without temp
* `x, y, z = arr` – unpack, nice for coords / edges

### Comprehensions

* List: `[f(x) for x in arr if cond(x)]`
* Set: `{x for x in arr}`
* Dict: `{k: f(k) for k in keys}`
* Very handy to transform/filter input in O(n) with minimal code.

### `__slots__` in custom classes

If you *do* write custom Node/State classes, adding:

```python
class Node:
    __slots__ = ('val', 'left', 'right')
```

saves memory & can speed up attribute access (helpful in large trees/graphs).

---

## 2️⃣ Extra standard modules that are useful

### `statistics`

Not for algorithm logic itself, but for **benchmarking / tuning** heuristics:

* `statistics.mean`, `median`, `stdev`, `median_low`, etc.
* Can help analyze distributions of runtimes, sample inputs, etc.

### `fractions.Fraction`

For exact rational arithmetic:

```python
from fractions import Fraction
x = Fraction(1, 3) + Fraction(1, 6)  # 1/2
```

Good when:

* You care about exact comparisons (no floating error) in geometry / probability.
* Inputs are small enough that numerators/denominators don’t explode.

### `decimal.Decimal`

For controlled precision floats:

```python
from decimal import Decimal, getcontext
getcontext().prec = 50
x = Decimal(1) / Decimal(7)
```

Mostly useful when:

* Problem requires a certain precision guarantee beyond normal double.
* But for most DSA/CP tasks, `float` + `math` is enough.

### `re` (regular expressions)

Good for **parsing weird input** or solving string problems where:

* You need to match specific patterns, split by complex delimiters, etc.
* However, for high-performance string DSA (like KMP, Z-algorithm), you usually implement algorithms explicitly rather than rely on `re`.

### `sys` and `io` (fast I/O)

For big inputs/outputs:

```python
import sys
data = sys.stdin.read().split()
# or
readline = sys.stdin.readline
```

* In some online judges, `input()` is too slow; `sys.stdin` can save you.
* Similarly, writing to `sys.stdout.write` in bulk can be faster than `print()` in a tight loop.

### `collections.abc`

For type hints and checking interfaces of your custom structures:

* `Mapping`, `MutableMapping`, `Sequence`, `MutableSequence`, `Set`, etc.
* Helpful when you want your own structure (like a custom Tree or Graph) to behave like a standard container.

### `enum.Enum`

For readable states:

```python
from enum import Enum, auto
class Color(Enum):
    WHITE = auto()
    GRAY = auto()
    BLACK = auto()
```

Useful in graph algorithms (visit states) or DP states where magic numbers get confusing.

### `hashlib`

For hashing strings / sequences:

* Sometimes used for rolling-hash style tricks, or verifying data integrity.
* In CP, people often implement custom polynomial hashes instead, but `hashlib` gives you SHA, MD5, etc.

---

## 3️⃣ Common 3rd-party helpers (if your environment allows them)

You’ve already looked at things like `intervaltree`, `pygtrie`, `treelib`. A few more worth knowing conceptually (not always allowed in contests, but great for learning / tooling):

* **`sortedcontainers`** (third-party): balanced-tree-like sorted list / dict / set; near-optimal `O(log n)` insert/remove and `O(log n)` searches without writing your own tree.
* **`networkx`**: heavyweight, but good for **learning** graph algorithms / prototyping (BFS/DFS, shortest paths, flows), though usually banned in contests.
* **`numpy`**: more for numeric / scientific stuff, but can be overkill for classic DSA; still useful if you do matrix exponentiation or big DP on arrays.

---

## 4️⃣ If you want a minimal “DSA must-know” subset

If you just want to **prioritize** what to truly *internalize*:

**Absolutely worth memorizing:**

* `list`, `dict`, `set`, `heapq`, `bisect`, `collections.deque`
* `itertools` basics: `product`, `permutations`, `combinations`, `accumulate`, `groupby`, `islice`
* `collections`: `Counter`, `defaultdict`, `namedtuple`
* `functools.lru_cache` / `cache`
* Built-ins: `range`, `sorted`, `enumerate`, `zip`, `min/max/sum`, `any/all`

**Nice to know but lower priority:**

* `dataclasses`, `copy`, `timeit`, `random`
* `fractions`, `decimal`, `statistics`, `re`, `enum`, `collections.abc`

Nice, let’s build out your DSA toolbox even more. I’ll **avoid repeating** stuff we already talked about and instead give you a **long, curated list** of *additional* things that are genuinely useful for data structures & algorithms in Python.

I’ll group them as:

1. Extra **built-ins & language tricks**
2. Extra **standard modules / features**
3. A few **3rd-party helpers** (if allowed)

You can skim the headings and cherry-pick what looks interesting.

---

## 1️⃣ Extra built-ins & language tricks (not covered before)

### 1.1 `iter` and `next` (manual iteration, sentinel tricks)

**Why useful:** Let you control iteration manually and use nice patterns for reading input or streaming data.

* `iter(obj)` – get iterator from any iterable (list, set, string, file, etc.).
* `next(it, default)` – get next element or `default` if iterator is exhausted.

**DSA tips:**

```python
it = iter(arr)
while True:
    x = next(it, None)
    if x is None:
        break
    ...
```

And the **sentinel pattern**:

```python
# Keep calling f() until it returns '' (EOF-style)
for line in iter(sys.stdin.readline, ''):
    ...
```

This avoids writing a `while True` with manual breaks.

---

### 1.2 `ord`, `chr`, `bin`, `oct`, `hex`, `format` (bit / char tricks)

**Why useful:** String/bit problems, hashing, encoding states.

* `ord('a')` → 97, `chr(97)` → `'a'`
  Use to convert chars to indices (`ord(c) - ord('a')`) in Trie / freq arrays.
* `bin(x)`, `oct(x)`, `hex(x)` – string forms of integers in different bases.
* `format(x, 'b')`, `format(x, '08b')` – formatted binary, padded, etc.

Example:

```python
mask = int('10101', 2)
bits = format(mask, 'b')  # '10101'
```

Great for **bitmask DP**.

---

### 1.3 `slice` objects (reuse slicing logic)

You can build a `slice` once and apply it multiple times:

```python
s = slice(1, 5, 2)
a[s]  # same as a[1:5:2]
b[s]
```

Useful when you want to parameterize your slicing logic (e.g. windows, segments).

---

### 1.4 Argument unpacking: `*` and `**`

We used unpacking implicitly, but there are some DSA-style idioms you can lean on:

* `a, b = b, a` – swap.
* `max(range(n), key=lambda i: arr[i])` – index of max element in `arr`.
* `fn(*args)` – pass a list/tuple as positional args.
* `fn(**kwargs)` – pass dict as keyword args.

For example, building edges:

```python
u, v, w = map(int, input().split())
edges.append((w, u, v))
```

Later:

```python
for w, u, v in edges:
    ...
```

---

### 1.5 Walrus operator `:=` (Python 3.8+)

Inline assignment in expressions:

```python
while (line := sys.stdin.readline().strip()):
    ...
```

Or:

```python
if (p := parent[x]) != -1:
    ...
```

Saves lines and sometimes repeated lookups — nice in BFS/DFS or parsing loops.

---

### 1.6 `for ... else` and `while ... else`

These are *weird* but very handy:

```python
for x in arr:
    if x == target:
        print("Found")
        break
else:
    print("Not found")
```

The `else` only runs if the loop wasn’t broken — great for search/failure logic.

---

### 1.7 F-strings with `=` (debugging DSA quickly)

Python 3.8+:

```python
print(f"{dist=}, {queue=}")
```

Expands to something like `dist=[...], queue=deque([...])`. Fast debugging in contests.

---

### 1.8 `memoryview` (for bytes / array slicing without copies)

If you’re dealing with **large byte arrays** (e.g. custom I/O, some DP on binary data):

```python
b = bytearray(b"abcdefgh")
view = memoryview(b)[2:5]  # no copy
```

Mutating `view` mutates the original buffer. Nice when you must avoid copying big slices.

---

## 2️⃣ Extra standard modules / features

These are *additional* things we haven’t really talked about, but which can help DSA.

---

### 2.1 `sys.setrecursionlimit` (deep recursion in DFS)

For recursive DFS on big trees/graphs:

```python
import sys
sys.setrecursionlimit(10**7)
```

Without this, you can easily hit `RecursionError` around depth 1000.

> ⚠ Still, iterative DFS/BFS is often safer and more portable.

---

### 2.2 `contextlib` (clean resource management)

Safe handling of resources (files, locks, etc.):

```python
from contextlib import contextmanager

@contextmanager
def timer():
    start = time.perf_counter()
    try:
        yield
    finally:
        print("elapsed:", time.perf_counter() - start)
```

Can be helpful when benchmarking multiple implementations.

---

### 2.3 `logging` (better than spamming `print`)

For debugging complex algorithms:

```python
import logging
logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)

log.debug("visiting node %s", u)
```

Then you can switch between silent and verbose modes without removing prints.

---

### 2.4 `re` patterns beyond basics

We already name-dropped `re`, but some **specific tricks** are useful:

* `re.split` for splitting by multiple delimiters.
* `re.finditer` to iterate over matches in order (useful for parsing).
* Non-greedy quantifiers (`.*?`) when parsing nested patterns.

For many DSA problems, you still hand-write parsers, but for messy input this can save a ton of time.

---

### 2.5 `bisect`’s pattern + `key` (custom binary search)

We already covered `bisect` itself, but a **useful pattern** is storing `(key, payload)` pairs in a sorted list, then doing binary search on the key.

```python
import bisect

arr = [(key1, value1), (key2, value2), ...]  # sorted by key
keys = [k for k,_ in arr]
i = bisect.bisect_left(keys, target)
```

This is a nice workaround when you don’t have `sortedcontainers` available.

---

### 2.6 `fractions` & `decimal` pro-tips (already mentioned, but one trick each)

**Fraction for geometry:** store slopes / ratios exactly:

```python
from fractions import Fraction
slope = Fraction(y2 - y1, x2 - x1)
```

**Decimal for required precision:** when a problem demands exactly 50 decimal places, not just approximate:

```python
from decimal import Decimal, getcontext
getcontext().prec = 60
```

---

### 2.7 `statistics` (lightweight profiling)

If you run multiple timings of algorithms:

```python
from statistics import mean, stdev
times = [...]
print(mean(times), stdev(times))
```

Helps you understand variance and robustness for randomized algorithms.

---

### 2.8 `enum.Enum` for state machines

We mentioned it quickly; in practice it cleans up BFS/DFS state handling:

```python
from enum import Enum, auto
class Color(Enum):
    WHITE = auto()
    GRAY = auto()
    BLACK = auto()
```

Instead of using `0/1/2`, you now write `Color.GRAY`, which is much clearer.

---

### 2.9 `collections.UserDict`, `UserList`, `UserString`

For **custom data structures** that behave like dict/list/string but with extra logic, without re-implementing the protocol:

```python
from collections import UserList

class TrackingList(UserList):
    def append(self, x):
        print("Appending", x)
        super().append(x)
```

Nice if you want to wrap a list with extra invariants or debugging.

---

### 2.10 Pattern matching (`match` / `case`, Python 3.10+)

Great for tree-like or variant data:

```python
match node:
    case ('leaf', value):
        ...
    case ('node', left, right):
        ...
```

This can express some recursive algorithms very cleanly (especially expression trees / AST problems).

---

## 3️⃣ Some more 3rd-party helpers (if allowed)

You’ve already seen `intervaltree`, `pygtrie`, `treelib`. A few more that some people like:

> These are **not** always allowed in online judges, but useful to know.

### 3.1 `sortedcontainers` (very practical “sorted list/set/dict”)

* `SortedList`, `SortedSet`, `SortedDict` – behave like built-ins but sorted.
* Operations like insert/search/remove in `O(log n)` Haskell/Tree-like.
* Convenient for:

  * “Find next greater/smaller element”
  * Sliding window with order statistics
  * Dynamic median structure

---

### 3.2 `networkx` (graph algorithms for learning)

* BFS, DFS, shortest path, flows, etc. built-in.
* Great for **learning** and prototyping, not usually for contests (too heavy/slow).

---

### 3.3 `numpy` (for numeric-heavy DP / matrices)

Not classic DSA, but if allowed, can speed up:

* Matrix exponentiation
* Convolution-like operations
* Some vectorized DP

Most competitive programming environments don’t allow it, but for personal projects/interviews it can be convenient.

---

### 3.4 `pyrsistent` (immutable data structures)

Purely functional / immutable structures:

* Persistent list, vector, map, set.
* Useful if you want to share state between many versions (e.g. path-copying, persistent segment tree–style logic) without manually implementing trees.

---

## 4️⃣ How to actually use all this without drowning

My suggestion:

1. **Lock in the essentials**

   * `list`, `dict`, `set`, `heapq`, `bisect`, `deque`, `Counter`, `defaultdict`, `lru_cache`, `itertools` basics, `range/sorted/enumerate/zip/any/all`.

2. **Add “sugar” that makes code shorter / clearer**

   * Walrus operator `:=`, `for...else`, f-strings with `=`, `iter`/`next` sentinel pattern, `namedtuple`/`dataclass`, `enum`.

3. **Sprinkle specialized tools as needed**

   * Geometry / numeric: `Fraction`, `Decimal`, `math` special functions.
   * Intervals / tries: `intervaltree`, `pygtrie`.
   * Graph learning: `networkx` (more for study, not contests).

