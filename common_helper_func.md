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

If you tell me **what kind of DSA you’re focusing on** (graphs, DP, strings, geometry, etc.), I can:

* Pick a smaller “must-have” list just for that area, and
* Give you 2–3 tiny practice snippets using those tools.


