
# TABLE OF CONTENTS

1. **Speed & memory hacks**
2. **Better control over recursion, errors, and I/O**
3. **Advanced iteration & code-structuring tricks**
4. **Standard-library tools for variations of common DS**
5. **3rd-party “serious mode” helpers (if allowed)**



---

## 1️⃣ Speed & memory hacks

### 1.1 `__slots__` + small custom classes

We briefly mentioned `__slots__`, but for **really big** trees/graphs or “state” objects, using it correctly can be a huge memory & speed win.

```python
class Node:
    __slots__ = ('val', 'children', 'dist')
    def __init__(self, val):
        self.val = val
        self.children = []
        self.dist = 0
```

* Cuts per-instance memory (no `__dict__`).
* Faster attribute access.
* Huge difference when you have 10^5–10^6 nodes.

Use it for **Node**, **Edge**, **State** classes in heavy graph/DP problems.

---

### 1.2 `memoryview` + `bytearray` for Big Data DP / I/O

If you ever do DP/string processing directly over bytes:

```python
b = bytearray(sys.stdin.buffer.read())
view = memoryview(b)
sub = view[1000:2000]  # no copy
```

* `memoryview` lets you slice a big buffer **without copying**.
* Very helpful in problems with big binary strings / large grids in a single blob.

---

### 1.3 Picking the right interpreter: CPython vs PyPy

Not a function, but a **huge practical trick**:

* On some judges, **PyPy** (JIT) is much faster for heavy Python loops, especially integer-heavy DSA.
* On others, CPython wins with heavy C-accelerated modules (`heapq`, `math`, etc.).

If allowed, check both; sometimes the difference decides whether you TLE or not.

---

### 1.4 “Vectorized” operations with `array` (instead of list of ints)

You already know `array('i', ...)`, but a pattern:

* Use `array('b')` or `array('I')` as compact bit/flag arrays for BFS/DP (visited, color, etc.) when memory is tight.
* They’re denser than lists of Python ints/booleans.

Example:

```python
from array import array
visited = array('b', [0]) * n   # 0/1 flags
```

---

## 2️⃣ Control over recursion, errors, and I/O

### 2.1 `sys.setrecursionlimit` + tail-recursion elimination by hand

For deep DFS:

```python
import sys
sys.setrecursionlimit(10**7)
```

But **advanced trick**: rewrite obvious recursion as a manual stack:

```python
stack = [root]
while stack:
    u = stack.pop()
    ...
    for v in adj[u]:
        stack.append(v)
```

* Use this template to avoid recursion depth issues entirely.
* Especially for trees with height up to 10^5.

---

### 2.2 `try/except` for “fail fast but cleanly”

Sometimes best DSA pattern is:

```python
try:
    i = a.index(x)  # O(n) but okay for small n
except ValueError:
    i = -1
```

Or more interesting:

```python
try:
    # Use fast path / assumption
    ...
except SomeError:
    # Fallback path
    ...
```

For example, try greedy assumption, if impossible, fall back to DP, etc.

---

### 2.3 Ultra-fast I/O: `sys.stdin.buffer`, `sys.stdout.write`

For *really* big input/output:

```python
import sys

data = sys.stdin.buffer.read().split()
it = iter(data)
n = int(next(it))

out_lines = []
for _ in range(n):
    # parse using next(it)
    ...

sys.stdout.write("\n".join(out_lines))
```

* `stdin.buffer.read()` is one of the fastest ways to ingest huge inputs.
* `stdout.write` avoids overhead of many `print()` calls.

---

## 3️⃣ Advanced iteration & code-structuring tricks

### 3.1 `yield` / generators as lazy pipelines

Instead of building giant lists:

```python
def neighbors(u):
    for v in adj[u]:
        if not blocked[v]:
            yield v

for v in neighbors(u):
    ...
```

Or multi-stage pipelines:

```python
def tokens():
    for line in sys.stdin:
        for tok in line.split():
            yield tok

def ints():
    for t in tokens():
        yield int(t)

it = ints()
n = next(it)
...
```

Keeps memory usage low, allows streaming-style solutions.

---

### 3.2 `yield from` to flatten recursion

For recursive enumerations:

```python
def dfs(u):
    yield u
    for v in adj[u]:
        yield from dfs(v)
```

Automatic “flattening”; handy for enumerating paths, ordering nodes, etc.

---

### 3.3 Using decorators to wrap DSA “templates”

Example: timing decorator, or memoization around a complex solver:

```python
import functools, time

def timed(fn):
    @functools.wraps(fn)
    def wrapper(*a, **k):
        t0 = time.perf_counter()
        res = fn(*a, **k)
        print("time:", time.perf_counter() - t0)
        return res
    return wrapper

@timed
def solve():
    ...
```

Helps benchmark different implementations **without touching** their logic.

---

### 3.4 Using `globals()` / `locals()` carefully for speed

Sometimes you’ll see patterns like:

```python
def solve():
    import sys
    input = sys.stdin.readline
    ...
```

or

```python
def solve():
    from math import sqrt
    ...
```

Because **local variables are faster than globals**. Having `input`/`sqrt` locally can shave some overhead inside tight loops.

---

## 4️⃣ Standard-library tools for DS variants

Here’s some more “lesser-known, but nice” stuff.

### 4.1 `collections.OrderedDict` for LRU-ish structures

Even though normal dicts keep insertion order now, `OrderedDict` has **`move_to_end`**:

```python
from collections import OrderedDict

class LRUCache:
    def __init__(self, cap):
        self.cap = cap
        self.od = OrderedDict()

    def get(self, key):
        if key not in self.od:
            return -1
        self.od.move_to_end(key)
        return self.od[key]

    def put(self, key, value):
        if key in self.od:
            self.od.move_to_end(key)
        self.od[key] = value
        if len(self.od) > self.cap:
            self.od.popitem(last=False)
```

Classic interview favorite: LRU cache in ~10 lines using `OrderedDict`.

---

### 4.2 `collections.UserList` / `UserDict` as DS base classes

Great when you want to **extend list/dict behavior** (for debugging or custom invariants) without re-implementing every method:

```python
from collections import UserList

class Stack(UserList):
    def push(self, x):
        self.append(x)
    def pop(self):  # can override if you want more checks / logging
        return super().pop()
```

This is more “clean design” than performance, but can speed debugging.

---

### 4.3 `pathlib` for file-based problems / offline testing

Sometimes you prototype with local test files:

```python
from pathlib import Path

for file in Path("tests").glob("*.in"):
    data = file.read_text().splitlines()
    ...
```

Not directly performance, but makes it easier to run your solution on many offline testcases (which is **super important** for tricky DPs/graphs).

---

### 4.4 `struct` for binary problems (less common, but powerful)

If you ever get binary-encoded integer sequences:

```python
import struct

data = sys.stdin.buffer.read()
n = len(data) // 4
ints = struct.unpack('!' + 'I' * n, data)  # network-order 4-byte unsigned ints
```

* Rare in contest settings, but very powerful if you do any binary-protocol style tasks or custom compressed input.

---

## 5️⃣ 3rd-party “serious mode” helpers (advanced)

> These are for when you’re not constrained by contest rules and want serious power.

### 5.1 `sortedcontainers` (must-know if allowed)

If you’re allowed external libs, this is practically cheating (in a good way):

```python
from sortedcontainers import SortedList

sl = SortedList()
sl.add(x)            # O(log n)
sl.remove(x)         # O(log n)
sl.bisect_left(x)    # O(log n)
sl[0], sl[-1]        # min, max
```

Perfect for:

* Order statistics
* Sliding window with dynamic min/max
* “Next greater/smaller” kind of tasks when updates happen

Also `SortedDict`, `SortedSet` exist.

---

### 5.2 `numba` for JIT compiling hot loops

For DP / loops that are pure Python but numeric-heavy:

```python
from numba import njit

@njit
def solve_dp(n, arr):
    ...
```

* JIT-compiles to machine code.
* Can give **C-like speed** in tight loops, but you lose some dynamic features.
* Amazing for running “Python algorithms at C speed” for your own practice.

---

### 5.3 `graphlib.TopologicalSorter` (Python 3.9+ stdlib)

Actually part of the standard library (`graphlib`), but specialized:

```python
from graphlib import TopologicalSorter

ts = TopologicalSorter()
ts.add('A', 'B', 'C')   # A depends on B and C
...
order = list(ts.static_order())  # topological order
```

Nice for DAG problems and verifying partial orders without writing your own topological sort each time.

---

### 5.4 `networkx` as a “graph algorithm library to learn from”

You don’t use this in contests, but for **learning / sanity-checking**:

```python
import networkx as nx

G = nx.Graph()
G.add_edge(u, v, weight=w)
dist = nx.shortest_path_length(G, source=0, target=5, weight='weight')
```

You can:

* Compare your Dijkstra/BFS outputs to `networkx` on random graphs.
* Prototype algorithms quickly, then port to hand-written Python for contests.

---

### 5.5 `hypothesis` for property-based testing

To test algorithms with random cases more intelligently:

```python
from hypothesis import given, strategies as st

@given(st.lists(st.integers(), max_size=20))
def test_sort(xs):
    assert my_sort(xs) == sorted(xs)
```

* Hypothesis will try to break your algorithm with weird edge cases, then shrink to minimal failing examples.
* Brilliant for verifying tricky DP/graph solutions.

---

## 6️⃣ How to actually *use* all this

For *advanced* DSA prep, I’d suggest this flow:

1. **Get raw correctness** with simple idioms.
2. Then apply **performance & clarity tools**:

   * Use `heapq`, `bisect`, `deque`, `defaultdict`, `lru_cache`, etc.
   * Add `__slots__` on high-volume classes.
   * Try `sys.stdin.buffer`, `sys.stdout.write` when IO is big.
3. For personal learning, occasionally:

   * Re-implement a classic algorithm,
   * Then validate its output with `networkx` / `hypothesis`,
   * Then profile with `timeit` and optimize using these tricks.

Here are some *even more* advanced, very DSA-flavored Python tricks and tools that we haven’t really dug into yet. I’ll stick to stuff that:

* Actually helps with **speed / clarity** in algorithms
* You probably **won’t see in beginner guides**
* Still stays “Pythonic” (no need to become a C dev overnight)

I’ll group them like this:

1. Advanced **integer / bit** tools
2. Advanced **string / bytes** tricks
3. Extra **standard modules & features** with DSA uses
4. Extra **3rd-party** helpers (for practice / non-contest work)

---

## 1️⃣ Advanced integer / bit tricks

These are super useful for bitmask DP, subsets problems, combinatorics, etc.

### 1.1 `int.bit_count()` (Python 3.8+)

Counts how many bits are set to `1` in the binary representation.

```python
x = 0b101101
x.bit_count()   # 4
```

Use cases in DSA:

* **Subset DP**: number of elements in subset represented by `mask`.
* **Hamming distance**: ` (a ^ b).bit_count()`.
* **Parity** checks: `mask.bit_count() % 2`.

---

### 1.2 `int.bit_length()`

Number of bits needed to represent the integer (excluding sign).

```python
(15).bit_length()   # 4  (1111)
(16).bit_length()   # 5  (10000)
```

Use cases:

* Fast way to approximate `log2(n)`:

  ```python
  k = n.bit_length() - 1  # floor(log2(n)) for positive n
  ```
* deciding array sizes in segment trees / sparse tables.

---

### 1.3 Common bitmask idioms

Some classic patterns:

```python
# Check if i-th bit set
bool(mask & (1 << i))

# Set i-th bit
mask |= (1 << i)

# Clear i-th bit
mask &= ~(1 << i)

# Toggle i-th bit
mask ^= (1 << i)

# Iterate over submasks of a mask
sub = mask
while sub:
    ...
    sub = (sub - 1) & mask
# (often also want to process sub = 0 separately)
```

This pattern is huge for “iterate over all subsets of a given set”.

---

### 1.4 `pow` for modular arithmetic (more advanced use)

We already mentioned `pow(a, b, mod)`, but for DSA:

* Fast modular exponentiation in 1 line:

  ```python
  pow(a, b, mod)   # (a^b) % mod, done in O(log b)
  ```
* Modular inverse mod prime `p` (when `a` and `p` are coprime):

  ```python
  inv_a = pow(a, p - 2, p)   # Fermat's little theorem
  ```
* Efficient exponentiation in combinatorics, matrix exponent, etc.

---

### 1.5 `int.to_bytes` / `int.from_bytes` (rare but powerful)

For weird bitpacking problems:

```python
x = 123456
b = x.to_bytes(4, byteorder='big')
y = int.from_bytes(b, byteorder='big')   # == 123456
```

Useful when:

* You need to serialize states / masks.
* You want to hash bitmasks more compactly (e.g., as bytes for use with crypto/hashing libs).

---

## 2️⃣ Advanced string / bytes tricks

Mostly useful in **string algorithms**, parsing and sometimes hashing.

### 2.1 `str.translate` / `str.maketrans` for fast char mapping

Instead of doing slow loops:

```python
table = str.maketrans({'A': '1', 'B': '2'})
s2 = s.translate(table)
```

Great for:

* Normalizing characters
* Simple cipher/text transforms
* Quick mapping in string problems (e.g., map `'a'..'z'` to something else)

---

### 2.2 `bytes`, `bytearray`, and `memoryview` in combo

* `bytes` – immutable sequence of bytes.
* `bytearray` – mutable sequence of bytes.
* `memoryview` – “window” into `bytes`/`bytearray`/`array` without copying.

Pattern:

```python
import sys

data = sys.stdin.buffer.read()      # bytes
barr = bytearray(data)              # mutable
view = memoryview(barr)[1000:2000]  # no copy
```

Use cases:

* Very big text / binary problems.
* Custom substring / pattern search where copying would be too slow or memory-heavy.

---

### 2.3 Rolling hash / polynomial hash pattern

Not a built-in, but a **pattern** built on top of `int` and `ord`:

```python
MOD = 10**9 + 7
BASE = 911382323

def poly_hash(s):
    h = 0
    for c in s:
        h = (h * BASE + ord(c)) % MOD
    return h
```

Used for:

* String hashing (Rabin–Karp)
* Duplicate substring detection
* Hashing paths / states

Combine with `pow(BASE, k, MOD)` and prefix hashes for O(1) substring hashes.

---

## 3️⃣ Extra standard modules & features (advanced angle)

### 3.1 `cProfile` / `profile` / `pstats` for performance diagnosis

When your code is too slow and you genuinely don’t know *where*:

```python
import cProfile, pstats

def main():
    solve()

cProfile.run('main()', 'profile.out')
p = pstats.Stats('profile.out')
p.sort_stats('tottime').print_stats(20)
```

This shows which functions are hot; great for optimizing big DSA solutions locally.

---

### 3.2 `graphlib.TopologicalSorter` (DAGs)

Standard library (Python 3.9+):

```python
from graphlib import TopologicalSorter

ts = TopologicalSorter()
ts.add('A', 'B', 'C')   # A depends on B and C
ts.add('B', 'C')
ts.add('C')

order = list(ts.static_order())
```

Use cases:

* Dependency resolution problems.
* Topological sort where you’d otherwise implement Kahn’s algorithm manually.

---

### 3.3 `heapq` max-heap pattern (refined)

We talked about `heapq` but a powerful pattern is:

* Store **negated values** to simulate a max-heap:

```python
import heapq

h = []
heapq.heappush(h, -value)
max_val = -heapq.heappop(h)
```

* Or store `(priority_sign * key, extra info)` tuples.

For problems requiring:

* “Get max k elements repeatedly”
* “Greedy pick largest by some metric”

---

### 3.4 `bisect` + “parallel arrays” pattern

To simulate an ordered map without external libs:

```python
import bisect

keys = []
values = []

def insert(k, v):
    i = bisect.bisect_left(keys, k)
    if i < len(keys) and keys[i] == k:
        values[i] = v
    else:
        keys.insert(i, k)
        values.insert(i, v)

def lower_bound(k):
    i = bisect.bisect_left(keys, k)
    if i < len(keys):
        return keys[i], values[i]
    return None
```

This pattern is a poor man’s `TreeMap` / `SortedDict` using plain lists.

---

### 3.5 `collections.abc` Protocols & duck typing (for your own DS)

Using `collections.abc` + `typing` helps structure your own DS:

```python
from collections.abc import MutableMapping

class MyMap(MutableMapping):
    ...
```

Now your `MyMap` will behave like a dict (supports `in`, iter, etc.). For DSA practice, this is useful when:

* You build your own structures (e.g., hash table, tree map)
* You want them to integrate smoothly with Python code (for reuse).

---

### 3.6 `typing.NamedTuple` (type-hinted namedtuple)

Similar to `collections.namedtuple` but friendlier with typing:

```python
from typing import NamedTuple

class Edge(NamedTuple):
    u: int
    v: int
    w: int

e = Edge(0, 1, 5)
```

Good for:

* Self-documenting edges/nodes with static typing.
* Immutable record-like objects.

---

### 3.7 `typing.TypeAlias` and `NewType` for semantics

Sometimes giving semantic names to primitive types helps avoid mistakes:

```python
from typing import NewType

Node = NewType('Node', int)
Weight = NewType('Weight', int)

# Now Node and Weight are both ints but they’re different types to type checkers
```

Not runtime performance, but helps you structure complex graph/DP code without mixing identifiers.

---

## 4️⃣ Extra 3rd-party helpers (advanced & optional)

These are more “serious mode” than common; very handy if you’re building projects or doing offline practice.

### 4.1 `bitarray` (dense bitsets, super fast)

A 3rd-party module (often called just `bitarray`) that gives you compact, fast bitsets:

```python
from bitarray import bitarray

b = bitarray(10)
b.setall(False)
b[3] = True
```

Use cases:

* Dense visited arrays / adjacency bitsets
* Fast set operations (AND/OR/XOR) at bit level

For big `n`, can be much more memory-efficient and faster than Python `set` or `list[bool]`.

---

### 4.2 `pyroaring` or `roaringbitmap` (compressed bitsets)

Roaring bitmaps: hybrid between bitsets and sorted lists:

* Very efficient for large sparse sets of integers.
* Fast union/intersection.

Good for advanced problems:

* Big integer sets (e.g. indexes, doc IDs, etc.).
* If you’re playing with inverted indexes / offline queries.

---

### 4.3 `pygraphblas` (linear algebra view of graphs)

Graph algorithms written as sparse linear algebra:

* `pygraphblas` uses GraphBLAS underneath (C/optimized).
* Many graph problems (BFS, shortest paths, transitive closure) can be expressed as matrix ops.

This is very advanced but cool:

* You can recast graph problems as matrix multiplications.
* Performance is often extremely good on large graphs.

---

### 4.4 `Cython` / `maturin` / `cffi` for hot spots

If you truly want C-level speed:

* **Cython**: compile typed Python‐ish code to C.
* **cffi** / **ctypes**: call C functions directly.
* **maturin**: compile Rust code as Python module.

Typical pattern:

* Prototype algorithm in Python
* Profile with `cProfile`
* Move **only the bottleneck loops** into a Cython or Rust function
* Call that from Python

This lets you keep Python flexibility but remove worst hot spots.

---

### 4.5 `numba` (JIT compile numeric loops)

We mentioned it before, but advanced pattern:

```python
from numba import njit

@njit
def dijkstra(n, edges, source):
    ...
```

* Very fast for numeric heavy loops (DP, BFS, Dijkstra on adjacency lists).
* Restrictions: no Python objects, limited features — you must stay in a “numba-friendly” subset.

---

## 5️⃣ How to leverage these for *advanced* DSA prep

At this point you don’t need *more names* so much as **patterns**. Things you can do:

1. **Pick a topic** (bitmask DP, geometry, strings, graphs…)
2. For each, design a small “toolkit” from these:

   * Bitmask DP → `int.bit_count`, bit patterns, `pow` modular, `Fraction`/`math` where needed
   * Graphs → `heapq` patterns, `deque`, `graphlib.TopologicalSorter`, maybe `networkx` (for verifying)
   * Strings → `str.translate`, rolling hash pattern, `re`, `bytes`/`bytearray`
3. Implement 2–3 classical problems **using those tools**:

   * And compare to a naive version to feel the difference.
4. Occasionally profile (`cProfile` / `timeit`) and try “upgrading” with:

   * `__slots__`, faster I/O, caching, better data structures.

If you tell me **which advanced topic you’re diving into next** (e.g. “bitmask DP”, “range queries (segment tree / Fenwick)”, “string pattern matching”), I can give you a **small, concrete kit** of 5–10 tricks specifically tailored to that topic, with sample code snippets.
