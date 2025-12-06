# Core built-in helpers (super common in DSA)

| Method / Operation                             | What it does                                     | Example                                               | Special errors / corner cases                                                                                         |
| ---------------------------------------------- | ------------------------------------------------ | ----------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `range(stop)` / `range(start, stop[, step])`   | Lazy sequence of integers (often used in loops). | `for i in range(0, n, 2): ...`                        | `step` cannot be `0` (`ValueError`); very large ranges are fine (lazy) but converting to list uses memory.            |
| `enumerate(iterable, start=0)`                 | Iterate with index and value.                    | `for i, x in enumerate(arr): ...`                     | Index is an int counter, independent of iterable’s type; no special errors.                                           |
| `sorted(iterable, *, key=None, reverse=False)` | Return new sorted list.                          | `sorted(arr)`; `sorted(words, key=len, reverse=True)` | Elements must be comparable under key; mixing incomparable types (e.g. `int` and `str`) → `TypeError`.                |
| `reversed(seq)`                                | Iterator over sequence in reverse order.         | `for x in reversed(arr): ...`                         | Works on sequences & objects implementing `__reversed__`; for general iterables use `reversed(list(iterable))`.       |
| `zip(*iterables)`                              | Pair up items by index (shortest length).        | `for a,b in zip(A,B): ...`                            | Stops at shortest iterable; for unequal lengths, tail of longer ones is ignored.                                      |
| `map(func, *iterables)`                        | Apply function elementwise; returns iterator.    | `map(lambda x:x*x, arr)`                              | Stops at shortest iterable if multiple; `func` must accept as many args as iterables; exceptions in `func` propagate. |
| `filter(func, iterable)`                       | Keep items where `func(item)` is true.           | `filter(lambda x:x%2==0, arr)`                        | If `func` is `None`, keeps truthy items; returns iterator.                                                            |
| `any(iterable)`                                | `True` if *any* element is truthy.               | `any(x>0 for x in arr)`                               | Short-circuits; empty iterable → `False`.                                                                             |
| `all(iterable)`                                | `True` if *all* elements are truthy.             | `all(x>=0 for x in arr)`                              | Short-circuits; empty iterable → `True`.                                                                              |
| `min(iterable, *, key=None, default=_)`        | Smallest element.                                | `min(arr)`, `min(arr, key=abs)`                       | `ValueError` for empty iterable **unless** `default` is given; elements must be comparable under key.                 |
| `max(iterable, *, key=None, default=_)`        | Largest element.                                 | `max(arr)`, `max(points, key=lambda p:p[0])`          | Same behavior as `min` for empties & comparability.                                                                   |
| `sum(iterable, start=0)`                       | Sum of elements plus optional start.             | `sum(arr)`, `sum(arr, start=0)`                       | For floats, use `math.fsum` for high precision; don’t use with strings or general objects.                            |
| `len(obj)`                                     | Number of items.                                 | `len(arr)`, `len(graph[u])`                           | Works if object implements `__len__`; otherwise `TypeError`.                                                          |
| `list(iterable)`                               | Make list from iterable.                         | `arr = list(range(10))`                               | Consumes entire iterable; can be heavy for infinite/huge iterables.                                                   |
| `set(iterable)`                                | Make set (unique elements).                      | `seen = set(arr)`                                     | Elements must be hashable; unhashable (like lists) → `TypeError`.                                                     |
| `dict(pairs_or_mapping)`                       | Make dict from key–value pairs or mapping.       | `d = dict([('a',1), ('b',2)])`                        | Pairs must be 2-item iterables; duplicate keys → last one wins.                                                       |

# collections.namedtuple – lightweight struct type: from collections import namedtuple

| Method / Operation                                                               | What it does                                   | Example                                  | Special errors / corner cases                                                                                                                                        |
| -------------------------------------------------------------------------------- | ---------------------------------------------- | ---------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `namedtuple(typename, field_names, *, rename=False, defaults=None, module=None)` | Create a new tuple subclass with named fields. | `Point = namedtuple('Point', ['x','y'])` | `field_names` can be list of strings or space-separated string; invalid names (keywords / duplicates) → `ValueError` unless `rename=True` (then they’re auto-fixed). |
| Create instance                                                                  | Make a record instance.                        | `p = Point(2, 3)`                        | Like tuple: fixed length; too many/few args → `TypeError`.                                                                                                           |
| Attribute access                                                                 | Access fields by name.                         | `p.x`, `p.y`                             | Fields are read-only (immutable); assignment `p.x = 5` → `AttributeError`.                                                                                           |
| Tuple behavior                                                                   | Works like a tuple too.                        | `p[0]  # 2`, `x, y = p`                  | Compared and hashed by contents; safe to use as dict keys or set elements.                                                                                           |
| `_fields`                                                                        | Tuple of field names.                          | `Point._fields  # ('x','y')`             | Introspection only.                                                                                                                                                  |
| `_replace(**kwargs)`                                                             | Return new instance with some fields changed.  | `p2 = p._replace(x=10)`                  | Old instance unchanged; invalid field name in kwargs → `ValueError`.                                                                                                 |
| `_asdict()`                                                                      | Return `OrderedDict` of field→value.           | `p._asdict()`                            | Useful for debugging / serialization.                                                                                                                                |
| `typename._make(iterable)`                                                       | Create instance from iterable.                 | `Point._make([2,3])`                     | Length of iterable must match field count; otherwise `TypeError`.                                                                                                    |
| Use in DSA                                                                       | Use for edges, states, etc.                    | `Edge = namedtuple('Edge', 'u v w')`     | Very memory-efficient vs custom class; immutable (so great for keys).                                                                                                |

# queue.PriorityQueue – thread-safe priority queue
You already know heapq; this is a thread-safe wrapper over a heap

| Method / Operation                       | What it does                                      | Example                                | Special errors / corner cases                                                                                                                                            |
| ---------------------------------------- | ------------------------------------------------- | -------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `PriorityQueue(maxsize=0)`               | Create a thread-safe min-priority queue.          | `pq = PriorityQueue()`                 | `maxsize <= 0` → infinite capacity; positive `maxsize` → `put` may block if full.                                                                                        |
| `pq.put(item, block=True, timeout=None)` | Insert `item`; blocks if full and `block=True`.   | `pq.put((dist, node))`                 | If `block=False` and full → `queue.Full`; with `timeout` and still full → `queue.Full`. Items must be comparable (if not using a tuple `(priority, tie_breaker, data)`). |
| `pq.put_nowait(item)`                    | Non-blocking put.                                 | `pq.put_nowait((1, 'task'))`           | Equivalent to `put(..., block=False)`; `queue.Full` if full.                                                                                                             |
| `pq.get(block=True, timeout=None)`       | Remove and return smallest item; blocks if empty. | `priority, node = pq.get()`            | If `block=False` and empty → `queue.Empty`; with `timeout` and still empty → `queue.Empty`.                                                                              |
| `pq.get_nowait()`                        | Non-blocking get.                                 | `item = pq.get_nowait()`               | Same as `get(..., block=False)`; `queue.Empty` if empty.                                                                                                                 |
| `pq.qsize()`                             | Approximate number of items.                      | `n = pq.qsize()`                       | In multi-threaded code, it’s only approximate (race conditions).                                                                                                         |
| `pq.empty()`                             | True if queue is (probably) empty.                | `if pq.empty(): ...`                   | Can be false immediately after check (another thread inserts).                                                                                                           |
| `pq.full()`                              | True if queue is (probably) full.                 | `if pq.full(): ...`                    | Same race condition caveat.                                                                                                                                              |
| `pq.task_done()`                         | Indicate that `get()`’s task is complete.         | `item = pq.get(); ...; pq.task_done()` | Calling more times than items fetched by `get()` → `ValueError`.                                                                                                         |
| `pq.join()`                              | Block until all enqueued tasks are marked done.   | `pq.join()`                            | Requires matching `task_done()` for each `put()`; otherwise `join()` never returns.                                                                                      |

# copy – shallow & deep copy of structures
Very handy so your algorithm doesn’t accidentally mutate shared structures
import copy

| Method / Operation                | What it does                            | Example                             | Special errors / corner cases                                                                                                                                                   |
| --------------------------------- | --------------------------------------- | ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `copy.copy(x)`                    | Shallow copy of object.                 | `b = copy.copy(a)`                  | Container object is new, but **inner elements are the same objects** (shared). Mutating nested structures affects both.                                                         |
| `copy.deepcopy(x, memo=None)`     | Deep copy: recursively copy objects.    | `b = copy.deepcopy(a)`              | Follows references recursively; can be slow or hit recursion if structure has cycles; `memo` used internally to avoid infinite loops on self-referential objects.               |
| Custom `__copy__`, `__deepcopy__` | Classes can define how copy works.      | `python\ndef __copy__(self): ...`   | If defined incorrectly, your objects might not copy as you expect (e.g. sharing state unintentionally).                                                                         |
| When to use (DSA)                 | Duplicate graphs, trees, states safely. | `next_state = copy.deepcopy(state)` | In contests, prefer writing algorithms that don’t need deep copy (for speed), but it’s very useful in backtracking or search when correctness is more important than raw speed. |
| Assignment vs copy                | `b = a` just binds name; no copying.    | `b = a`                             | Both names reference same object; mutating through one affects the other—classic bug when using lists/dicts for DP tables.                                                      |

# timeit – quick performance measurement
Perfect for checking which of two solutions is faster.
import timeit

| Method / Operation                                                                          | What it does                                                | Example                                                                                | Special errors / corner cases                                                                                                                                    |
| ------------------------------------------------------------------------------------------- | ----------------------------------------------------------- | -------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `timeit.timeit(stmt='pass', setup='pass', timer=<default>, number=1_000_000, globals=None)` | Run `stmt` `number` times and return total time in seconds. | `t = timeit.timeit('sum(range(100))', number=10000)`                                   | `stmt` and `setup` are strings (or callables in newer usage); code runs in its own namespace unless you pass `globals`. Big `number` → more accurate but slower. |
| `timeit.repeat(stmt, setup, timer, repeat=5, number=1_000_000, globals=None)`               | Run `timeit` multiple times and return list of times.       | `times = timeit.repeat('f()', setup='from __main__ import f', repeat=5, number=10000)` | Helps see variance; often use `min(times)` as best estimate. May run for quite long if `repeat` and `number` large.                                              |
| `timeit.Timer(stmt='pass', setup='pass', timer=<default>)`                                  | Lower-level timer object.                                   | `timer = timeit.Timer('f()', 'from __main__ import f')`                                | You can call `timer.timeit(number)` or `timer.repeat(...)` later; similar caveats on namespace and strings.                                                      |
| CLI usage                                                                                   | Run from command line.                                      | `python -m timeit "sum(range(100))"`                                                   | Command-line options `-n`, `-r`, `-s` control number, repeats, setup; good for quick experiments.                                                                |
| GC handling                                                                                 | `timeit` disables garbage collector by default.             | `timeit.timeit(...)`                                                                   | This avoids GC “noise” but may not match real-world behavior exactly if your code allocates a lot.                                                               |
| When to use (DSA)                                                                           | Compare two implementations.                                | Measure `O(n)` vs `O(n log n)` on different input sizes.                               | Always run on multiple input sizes; don’t assume small `n` timings reflect asymptotic performance.                                                               |

# 1️⃣ Extra built-ins & language tricks

These are tiny but show up *everywhere* in competitive programming / DSA code.

## `any`, `all`, and generator expressions

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

# TOOLS

- itertools – iterators, combinatorics
- functools – memoization, custom sorting, functional tools
- operator – fast lambda replacements (itemgetter, etc.)
- random – randomness for algorithms / testing
- dataclasses – clean data containers for nodes / states

``` python
import itertools
import functools
import operator
import random
from dataclasses import dataclass, field, asdict, astuple, replace, is_dataclass, make_dataclass
```

# itertools – iterator / combinatorics toolbox

All of these return iterators, not lists. Most are in three groups: infinite, combinatoric, and “recipes”.

| Method/Operation                                                     | What it does                                                  | Example                                                                              | Special errors / corner cases                                                                   |
| -------------------------------------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------- |
| `itertools.count(start=0, step=1)`                                   | Infinite counter: `start, start+step, ...`.                   | `for i in itertools.count(0, 2): ...`                                                | **Infinite** – must break manually or slice, or you’ll loop forever.                            |
| `itertools.cycle(iterable)`                                          | Infinite cycle over elements.                                 | `colors = itertools.cycle(['R','G','B'])`                                            | Also infinite; stores a copy of the iterable internally (memory!).                              |
| `itertools.repeat(object, times=None)`                               | Repeat `object` `times` or forever.                           | `list(itertools.repeat(1, 3))  # [1,1,1]`                                            | Infinite if `times` is `None`.                                                                  |
| `itertools.accumulate(iterable, func=operator.add, *, initial=None)` | Running accumulation (prefix sums/products/etc).              | `list(itertools.accumulate([1,2,3]))  # [1,3,6]`                                     | `func` must be a 2-arg function; `initial` adds one extra element at start.                     |
| `itertools.chain(*iterables)`                                        | Chain iterables end-to-end.                                   | `list(itertools.chain([1,2], [3]))  # [1,2,3]`                                       | Lazy; doesn’t copy data.                                                                        |
| `itertools.chain.from_iterable(iterable_of_iterables)`               | Flatten one level.                                            | `chain = itertools.chain.from_iterable(list_of_lists)`                               | Good when iterable-of-iterables comes from elsewhere.                                           |
| `itertools.compress(data, selectors)`                                | Filter `data` by boolean `selectors`.                         | `list(itertools.compress('ABCDE', [1,0,1,0,1]))  # ['A','C','E']`                    | Stops when either input is exhausted; selectors truthiness used.                                |
| `itertools.dropwhile(pred, iterable)`                                | Skip items while `pred(item)` true, then yield rest.          | `list(dropwhile(lambda x:x<3, [1,2,3,1]))  # [3,1]`                                  | Once predicate is false the first time, it’s never called again.                                |
| `itertools.takewhile(pred, iterable)`                                | Yield while `pred(item)` true, then stop.                     | `list(takewhile(lambda x<x<3, [1,2,3]))` → `[1,2]`                                   | Remaining items are **discarded**, not available later.                                         |
| `itertools.filterfalse(pred, iterable)`                              | Opposite of `filter`: keep items where `pred(item)` is false. | `list(filterfalse(lambda x:x%2, [1,2,3,4]))  # [2,4]`                                | If `pred` is `None`, keeps falsey items.                                                        |
| `itertools.islice(iterable, start, stop, step=1)`                    | Slice an iterator (like list slicing).                        | `list(islice(range(10), 2, 8, 2))  # [2,4,6]`                                        | Works on any iterable; once consumed, items are gone.                                           |
| `itertools.starmap(func, iterable_of_args)`                          | Like `map`, but unpacks args from tuples.                     | `list(starmap(pow, [(2,3),(3,2)]))  # [8,9]`                                         | Each element must be an iterable of arguments.                                                  |
| `itertools.zip_longest(*iterables, fillvalue=None)`                  | Zip to longest iterable; pad with `fillvalue`.                | `list(zip_longest('AB', '123', fillvalue='-'))` → `[('A','1'),('B','2'),('-', '3')]` | Beware of infinite iterables: zip_longest will be infinite too.                                 |
| `itertools.product(*iterables, repeat=1)`                            | Cartesian product.                                            | `list(product([1,2], ['a','b']))` → `[(1,'a'),(1,'b'),(2,'a'),(2,'b')]`              | Output size = `prod(len(it)*repeat)`; can blow up quickly.                                      |
| `itertools.permutations(iterable, r=None)`                           | All r-length permutations.                                    | `list(permutations([1,2,3], 2))`                                                     | Size ≈ `n!` if `r` not given → expensive fast.                                                  |
| `itertools.combinations(iterable, r)`                                | r-length combinations (no order, no repetition).              | `list(combinations('ABC', 2))`                                                       | Size = `nCr`; again can be large.                                                               |
| `itertools.combinations_with_replacement(iterable, r)`               | r-combinations allowing repeated elements.                    | `list(combinations_with_replacement('AB', 2))` → `[('A','A'),('A','B'),('B','B')]`   | Size = `nCr_r` (with repetition); can grow fast.                                                |
| `itertools.groupby(iterable, key=None)`                              | Group consecutive equal elements (by `key`).                  | `[(k, list(g)) for k,g in groupby('aaabb', key=lambda x:x)]`                         | **Only groups consecutive runs**; data must be pre-sorted by key for value-based grouping.      |
| `itertools.pairwise(iterable)`                                       | Overlapping pairs `(a0,a1), (a1,a2), ...`.                    | `list(pairwise([1,2,3,4]))  # [(1,2),(2,3),(3,4)]`                                   | Added in 3.10; don’t use if you need to support much older Pythons. ([Python documentation][1]) |
| `itertools.batched(iterable, n)`                                     | Yield fixed-size chunks (last may be smaller).                | `list(batched(range(7), 3))  # [(0,1,2),(3,4,5),(6,)]`                               | Added in 3.12; `n <= 0` raises `ValueError`. ([Python documentation][1])                        |

[1]: https://docs.python.org/3/library/itertools.html?utm_source=chatgpt.com "itertools — Functions creating iterators for efficient looping — Python ..."

# functools – higher-order helpers & memoization

Very handy for DP/memoization and custom sorting

| Method/Operation                                          | What it does                                                                       | Example                                                                                    | Special errors / corner cases                                                                                                                   |
| --------------------------------------------------------- | ---------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| `@functools.lru_cache(maxsize=128, typed=False)`          | Memoize function results with LRU eviction.                                        | `python\n@functools.lru_cache(None)\ndef fib(n): return n if n<2 else fib(n-1)+fib(n-2)\n` | Arguments must be hashable; use `maxsize=None` for unbounded cache; `typed=True` treats `1` and `1.0` as different keys.                        |
| `@functools.cache`                                        | Unbounded cache (like `lru_cache(maxsize=None)`).                                  | `@functools.cache\ndef f(x): ...`                                                          | No LRU: memory can grow indefinitely if many distinct argument combos. ([Python documentation][1])                                              |
| `functools.reduce(func, iterable, initializer=_sentinel)` | Fold iterable into single value.                                                   | `reduce(lambda a,b:a+b, [1,2,3], 0)  # 6`                                                  | For empty iterable **without** `initializer` → `TypeError`. With initializer, result is initializer for empty iterable.                         |
| `functools.cmp_to_key(cmp)`                               | Convert old-style `cmp(a,b)` into `key` function for `sort` / `sorted`.            | `sorted(arr, key=cmp_to_key(cmp_func))`                                                    | `cmp` must return negative/zero/positive; misuse can break sort invariants.                                                                     |
| `functools.partial(func, *args, **kwargs)`                | Freeze some args, returning new function.                                          | `inc = partial(lambda x,y:x+y, 1)`                                                         | New function still checks argument counts; mis-matching leftover args → `TypeError`.                                                            |
| `functools.wraps(wrapped)`                                | Decorator to copy metadata to wrapper.                                             | `python\n@functools.wraps(func)\ndef wrapper(*a,**k): ...`                                 | Forgetting `@wraps` makes debugging / help text confusing, but no runtime error.                                                                |
| `functools.total_ordering`                                | Class decorator that fills in rich comparisons given `__eq__` and one ordering op. | `python\n@total_ordering\nclass Node: ...`                                                 | Must implement `__eq__` and **one** of `<, <=, >, >=`; wrong/partial implementation can give inconsistent ordering. ([Python documentation][1]) |
| `functools.singledispatch(func)`                          | Generic function based on first arg type.                                          | `python\n@singledispatch\ndef visit(x): ...`                                               | For DSA less common, but handy in visitor patterns; must register concrete types; works on runtime type of first arg only.                      |


# operator – operators & getters as functions

Great for sorting, key functions, and making code cleaner/faster vs lambdas.

| Method/Operation                                  | What it does                                            | Example                                               | Special errors / corner cases                                                                                        |
| ------------------------------------------------- | ------------------------------------------------------- | ----------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `operator.add(a, b)`                              | `a + b`.                                                | `operator.add(1, 2)  # 3`                             | Mirrors built-in operators; same errors (e.g. `TypeError` for incompatible types).                                   |
| `operator.sub(a, b)`                              | `a - b`.                                                | `operator.sub(5, 3)`                                  | –                                                                                                                    |
| `operator.mul(a, b)`                              | `a * b`.                                                | `operator.mul(2, 4)`                                  | –                                                                                                                    |
| `operator.truediv(a, b)`                          | `a / b`.                                                | `operator.truediv(5, 2)`                              | `ZeroDivisionError` if `b == 0`.                                                                                     |
| `operator.floordiv(a, b)`                         | `a // b`.                                               | `operator.floordiv(5, 2)`                             | Same as above.                                                                                                       |
| `operator.mod(a, b)`                              | `a % b`.                                                | `operator.mod(5, 2)`                                  | –                                                                                                                    |
| `operator.pow(a, b)`                              | `a ** b`.                                               | `operator.pow(2, 10)`                                 | Same caveats as `**`.                                                                                                |
| `operator.neg(a)` / `operator.pos(a)`             | Unary `-a` / `+a`.                                      | `operator.neg(3)`                                     | Depends on type implementing unary ops.                                                                              |
| `operator.eq(a, b)`, `ne`, `lt`, `le`, `gt`, `ge` | Comparison operators as functions.                      | `operator.lt(1, 2)  # True`                           | Good for building custom sort keys or predicates.                                                                    |
| `operator.itemgetter(*items)`                     | Return function that fetches element(s) by index/key.   | `get2 = itemgetter(2); get2([10,20,30])  # 30`        | For multiple keys, returns tuple; raises `IndexError`/`KeyError` same as indexing. ([GeeksforGeeks][1])              |
| `operator.attrgetter(*attrs)`                     | Return function that gets attribute(s).                 | `get_name = attrgetter('name'); get_name(obj)`        | Chained attributes like `'a.b.c'` allowed; missing attribute → `AttributeError`. ([Python documentation][2])         |
| `operator.methodcaller(name, *args, **kwargs)`    | Return function that calls named method on its operand. | `stripper = methodcaller('strip'); stripper('  hi ')` | If method doesn’t exist → `AttributeError`; any exception inside method propagates. ([Nkmk Note][3])                 |
| In-place ops: `iadd`, `isub`, ...                 | In-place versions of `+`, `-`, etc.                     | `operator.iadd(a_list, [4,5])`                        | Falls back to regular op if in-place not supported; mutates first arg if it is mutable and supports it (e.g. lists). |

[2]: https://docs.python.org/3/library/operator.html?utm_source=chatgpt.com "operator — Standard operators as functions — Python 3.14.1 documentation"
[3]: https://note.nkmk.me/en/python-operator-usage/?utm_source=chatgpt.com "The operator Module in Python: itemgetter, attrgetter, methodcaller"

# random – randomness for algorithms & tests

Useful for randomized quicksort/quickselect, test generation, etc.

| Method/Operation                                                     | What it does                                         | Example                        | Special errors / corner cases                                                                                        |
| -------------------------------------------------------------------- | ---------------------------------------------------- | ------------------------------ | -------------------------------------------------------------------------------------------------------------------- |
| `random.seed(a=None)`                                                | Seed the PRNG (reproducible randomness).             | `random.seed(42)`              | Same seed → same sequence; if `a` is `None`, uses system entropy.                                                    |
| `random.random()`                                                    | Float in `[0.0, 1.0)`.                               | `x = random.random()`          | Never returns `1.0`.                                                                                                 |
| `random.randint(a, b)`                                               | Random int in **inclusive** range `[a, b]`.          | `random.randint(1, 6)`         | `ValueError` if `a > b`.                                                                                             |
| `random.randrange(start, stop[, step])`                              | Like `range`, but returns one random element.        | `random.randrange(0, 10, 2)`   | Same constraints as `range` (e.g. non-zero step, proper ordering) or `ValueError`.                                   |
| `random.uniform(a, b)`                                               | Float in `[a, b]` or `[b, a]` (inclusive endpoints). | `random.uniform(1.0, 2.0)`     | Endpoints may be returned; distribution is continuous.                                                               |
| `random.choice(seq)`                                                 | Random element from non-empty sequence.              | `random.choice([1,2,3])`       | `IndexError` if sequence empty.                                                                                      |
| `random.choices(population, weights=None, k=1)`                      | Return list of `k` elements with replacement.        | `random.choices([1,2,3], k=5)` | For large `k`, items may repeat; weights must be non-negative.                                                       |
| `random.sample(population, k)`                                       | Choose `k` distinct elements (without replacement).  | `random.sample(range(10), 3)`  | `ValueError` if `k > len(population)` (except for sets where population can be treated specially in newer versions). |
| `random.shuffle(x)`                                                  | In-place shuffle of a mutable sequence.              | `random.shuffle(lst)`          | `x` must be mutable and indexable; use `random.sample` for immutables.                                               |
| `random.getrandbits(k)`                                              | Integer with `k` random bits.                        | `random.getrandbits(32)`       | `k` must be non-negative; big `k` → big int.                                                                         |
| `random.betavariate`, `gammavariate`, `gauss`, `normalvariate`, etc. | Continuous distributions for simulations.            | `random.gauss(0, 1)`           | For most DSA prep you rarely need these; beware of floating precision.                                               |
| `random.randbytes(n)` (3.9+)                                         | Return `n` random bytes.                             | `random.randbytes(16)`         | Not cryptographically secure; for security use `secrets` module.                                                     |

# dataclasses – lightweight data containers (great for nodes)

Extremely handy for defining tree nodes, graph nodes, states with minimal boilerplate.

| Method/Operation                          | What it does                                                                | Example                                                                | Special errors / corner cases                                                                                                                    |                 |                                                                                                                                                                        |
| ----------------------------------------- | --------------------------------------------------------------------------- | ---------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ | --------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `@dataclass(...)`                         | Decorator to auto-generate `__init__`, `__repr__`, `__eq__`, ordering, etc. | ```python\n@dataclass\nclass Node:\n    val: int\n    left: 'Node      | None'=None\n    right: 'Node                                                                                                                     | None'=None\n``` | Options: `order=True` adds comparisons; `frozen=True` makes instances immutable; `slots=True` reduces memory. Misusing `frozen` with mutation → `FrozenInstanceError`. |
| `dataclasses.field(...)`                  | Customize a single field (default, repr, compare, etc.).                    | `children: list[int] = field(default_factory=list)`                    | Using `default=[]` for mutables is a classic bug; use `default_factory` instead.                                                                 |                 |                                                                                                                                                                        |
| Auto-generated methods                    | `__init__`, `__repr__`, `__eq__`, optionally ordering methods.              | `a == b`, `sorted(nodes)`                                              | Ordering only if `order=True`; equality based on fields, not identity.                                                                           |                 |                                                                                                                                                                        |
| `asdict(instance)`                        | Deep-convert dataclass instance to dict.                                    | `asdict(node)`                                                         | Recurses into nested dataclasses, lists, tuples, dicts; behaves like a **deep copy** of those structures. Can be expensive. ([GeeksforGeeks][1]) |                 |                                                                                                                                                                        |
| `astuple(instance)`                       | Like `asdict` but as tuple.                                                 | `astuple(node)`                                                        | Also deep-recursive by default; uses `tuple_factory` if provided. ([Stack Overflow][2])                                                          |                 |                                                                                                                                                                        |
| `replace(instance, **changes)`            | Return a new instance with some fields changed.                             | `node2 = replace(node, val=42)`                                        | Shallow copy then override; nested objects reused.                                                                                               |                 |                                                                                                                                                                        |
| `is_dataclass(obj)`                       | Check if object or class is a dataclass.                                    | `is_dataclass(Node)` / `is_dataclass(node)`                            | Returns `True` also for instances.                                                                                                               |                 |                                                                                                                                                                        |
| `make_dataclass(name, fields, **options)` | Dynamically create a dataclass type.                                        | `python\nPoint = make_dataclass('Point', ['x','y'])\np = Point(1,2)\n` | Fields can be `(name, type, field_spec)` tuples; useful for meta-programming or contests where you build quick struct types.                     |                 |                                                                                                                                                                        |
