# Stack (implemented with list) stack = []

| Method/Operation                               | What it does                          | Example                         | Special errors / corner cases                                         |
| ---------------------------------------------- | ------------------------------------- | ------------------------------- | --------------------------------------------------------------------- |
| `stack = []` / `stack = list()`                | Create an empty stack.                | `stack = []`                    | –                                                                     |
| `stack.append(x)` (**push**)                   | Push element `x` onto top of stack.   | `stack.append(10)`              | Returns `None`. `TypeError` only if wrong number of arguments.        |
| `stack.pop()` (**pop**)                        | Remove and return top element.        | `top = stack.pop()`             | `IndexError: pop from empty list` if stack empty.                     |
| `stack[-1]` (**peek/top**)                     | Read top element without removing it. | `top = stack[-1]`               | `IndexError: list index out of range` if stack empty.                 |
| `not stack` / `len(stack) == 0` (**is_empty**) | Check if stack is empty.              | `if not stack: ...`             | Works even if stack is large; no error.                               |
| `len(stack)` (**size**)                        | Number of elements in stack.          | `n = len(stack)`                | –                                                                     |
| `stack.clear()`                                | Remove all elements.                  | `stack.clear()`                 | Returns `None`. `TypeError` if any argument is passed.                |
| `x in stack`                                   | Check if `x` is somewhere in stack.   | `if 5 in stack:`                | Linear search; may be slow for big stacks.                            |
| `reversed(stack)`                              | Iterate from top to bottom.           | `for x in reversed(stack): ...` | Returns an iterator; no error for empty stack.                        |
| `stack.copy()`                                 | Shallow copy of stack.                | `s2 = stack.copy()`             | List itself is new; inner mutable elements are shared (shallow copy). |


# Queue (thread-safe FIFO using queue.Queue)

```from queue import Queue

q = Queue(maxsize=0)   # 0 or less → infinite size```

| Method/Operation                        | What it does                                               | Example                              | Special errors / corner cases                                                                               |
| --------------------------------------- | ---------------------------------------------------------- | ------------------------------------ | ----------------------------------------------------------------------------------------------------------- |
| `Queue(maxsize=0)`                      | Create a new FIFO queue with optional max size.            | `q = Queue(5)`                       | `maxsize <= 0` means “infinite” size.                                                                       |
| `q.put(item, block=True, timeout=None)` | Enqueue `item`; blocks if full and `block=True`.           | `q.put(10)`                          | If `block=False` and full → `queue.Full`. If `block=True` with `timeout` and still full → `queue.Full`.     |
| `q.put_nowait(item)`                    | Non-blocking `put`.                                        | `q.put_nowait(10)`                   | Exactly `q.put(item, block=False)`. Raises `queue.Full` if full.                                            |
| `q.get(block=True, timeout=None)`       | Dequeue and return item; blocks if empty and `block=True`. | `item = q.get()`                     | If `block=False` and empty → `queue.Empty`. If `block=True` with `timeout` and still empty → `queue.Empty`. |
| `q.get_nowait()`                        | Non-blocking `get`.                                        | `item = q.get_nowait()`              | Exactly `q.get(block=False)`. Raises `queue.Empty` if empty.                                                |
| `q.qsize()`                             | Approximate number of elements.                            | `n = q.qsize()`                      | In multithreaded programs, value is **approximate**, not exact.                                             |
| `q.empty()`                             | `True` if queue is (probably) empty.                       | `if q.empty(): ...`                  | In multithreaded context it may become non-empty immediately after call.                                    |
| `q.full()`                              | `True` if queue is (probably) full.                        | `if q.full(): ...`                   | Same race condition caveat as `empty()`.                                                                    |
| `q.task_done()`                         | Signal that a previously `get()` item is processed.        | `item = q.get(); ...; q.task_done()` | `ValueError` if called more times than items taken by `get()`.                                              |
| `q.join()`                              | Block until all *enqueued* tasks are marked done.          | `q.join()`                           | Requires matching `task_done()` calls for each `put()`. Can block forever if forgotten.                     |

# Deque (collections.deque)

```
from collections import deque

dq = deque(iterable=(), maxlen=None)
```

| Method/Operation                  | What it does                                                         | Example                         | Special errors / corner cases                                                                    |
| --------------------------------- | -------------------------------------------------------------------- | ------------------------------- | ------------------------------------------------------------------------------------------------ |
| `deque(iterable=(), maxlen=None)` | Create a new deque from iterable with optional max length.           | `dq = deque([1,2,3], maxlen=5)` | If `maxlen` is set and deque overflows, items are discarded from the opposite end automatically. |
| `dq.append(x)`                    | Add `x` to the **right** end.                                        | `dq.append(4)`                  | If `maxlen` is set and full, leftmost item is dropped.                                           |
| `dq.appendleft(x)`                | Add `x` to the **left** end.                                         | `dq.appendleft(0)`              | If `maxlen` is set and full, rightmost item is dropped.                                          |
| `dq.pop()`                        | Remove and return **rightmost** element.                             | `x = dq.pop()`                  | `IndexError: pop from an empty deque` if empty.                                                  |
| `dq.popleft()`                    | Remove and return **leftmost** element.                              | `x = dq.popleft()`              | `IndexError: pop from an empty deque` if empty.                                                  |
| `dq.extend(iterable)`             | Extend right side by elements of iterable.                           | `dq.extend([4,5])`              | With `maxlen`, some left items may be dropped if capacity exceeded.                              |
| `dq.extendleft(iterable)`         | Extend left side; iterable consumed left→right but added in reverse. | `dq.extendleft([0, -1])`        | The final order is reversed: `extendleft([0, -1])` adds `-1` then `0` on the left.               |
| `dq.clear()`                      | Remove all elements.                                                 | `dq.clear()`                    | Returns `None`.                                                                                  |
| `dq.copy()`                       | Shallow copy of deque.                                               | `dq2 = dq.copy()`               | Available in modern Python 3; shallow copy (inner objects shared).                               |
| `dq.count(x)`                     | Count occurrences of `x`.                                            | `dq.count(2)`                   | Linear time.                                                                                     |
| `dq.remove(x)`                    | Remove **first occurrence** of `x`.                                  | `dq.remove(2)`                  | `ValueError: deque.remove(x): x not in deque` if missing.                                        |
| `dq.rotate(n=1)`                  | Rotate right by `n` steps (left if `n` negative).                    | `dq.rotate(1)`                  | `n` can be any int; rotation by big `n` is effectively `n % len(dq)` (if non-empty).             |
| `dq.reverse()`                    | Reverse deque **in place**.                                          | `dq.reverse()`                  | Returns `None`.                                                                                  |
| `dq.maxlen` (attribute)           | Read-only maximum length (or `None`).                                | `m = dq.maxlen`                 | Cannot be changed after creation.                                                                |
| `dq[i]` (indexing)                | Access element at position `i`.                                      | `dq[0]`, `dq[-1]`               | `IndexError` if out of range. Indexing is allowed but slower than ends.                          |
| `len(dq)`                         | Number of elements.                                                  | `len(dq)`                       | –                                                                                                |
| `x in dq`                         | Membership test.                                                     | `if 2 in dq:`                   | Linear search.                                                                                   |
| Iteration `for x in dq:`          | Iterate from left to right.                                          | `for x in dq: ...`              | Order is the logical deque order.                                                                |
| Slicing (not supported)           | –                                                                    | `dq[1:3]`                       | `TypeError: sequence index must be integer, not 'slice'` – deques don’t support slicing.         |

# Linked list (custom implementation / abstract operations)

```
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
```

| Method/Operation              | What it does                                     | Example                 | Special errors / corner cases (typical)                                                                                                    |
| ----------------------------- | ------------------------------------------------ | ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| `ll = LinkedList()`           | Create an empty linked list.                     | `ll = LinkedList()`     | `ll.head` usually set to `None`.                                                                                                           |
| `ll.insert_front(value)`      | Insert new node at the beginning.                | `ll.insert_front(10)`   | Works even if list empty (new head).                                                                                                       |
| `ll.insert_back(value)`       | Insert new node at the end.                      | `ll.insert_back(20)`    | For empty list, same as insert at front. You must traverse to tail (O(n)) unless you store a tail pointer.                                 |
| `ll.insert_at(index, value)`  | Insert node at a given position.                 | `ll.insert_at(2, 99)`   | Commonly raises `IndexError` if `index < 0` or `index > length`. Inserting at index 0 usually equivalent to `insert_front`.                |
| `ll.delete_front()`           | Remove first node.                               | `ll.delete_front()`     | If list empty, typical to raise `IndexError` or do nothing (design choice).                                                                |
| `ll.delete_back()`            | Remove last node.                                | `ll.delete_back()`      | For empty list, `IndexError` / no-op; for single-node list, head becomes `None`. Need to handle those special cases carefully.             |
| `ll.delete_value(value)`      | Delete **first node** whose data equals `value`. | `ll.delete_value(10)`   | If value not found, typical to raise `ValueError` or silently do nothing (document behavior). Need special case when deleted node is head. |
| `ll.delete_at(index)`         | Delete node at position `index`.                 | `ll.delete_at(1)`       | Usually `IndexError` if out of range; deleting index 0 affects head pointer.                                                               |
| `ll.search(value)`            | Find node containing `value` (or return index).  | `node = ll.search(5)`   | If not found, often returns `None` or `-1`. No built-in error.                                                                             |
| `ll.is_empty()`               | Check if list is empty.                          | `if ll.is_empty(): ...` | Typically implemented as `return self.head is None`.                                                                                       |
| `ll.__len__()` / `len(ll)`    | Return number of nodes.                          | `n = len(ll)`           | If you count by traversal each time → O(n); or maintain `size` attribute.                                                                  |
| Iteration (`for x in ll:`)    | Traverse nodes in order.                         | `for value in ll: ...`  | Implement `__iter__` to yield `node.data`. Infinite loops possible if list accidentally cycles.                                            |
| `ll.get(index)` / `ll[index]` | Access element at position.                      | `ll[2]` or `ll.get(2)`  | Usually `IndexError` if out of range. Access is O(n) (must traverse).                                                                      |
| `ll.set(index, value)`        | Replace data at position.                        | `ll.set(1, 42)`         | Same index rules as `get`.                                                                                                                 |
| `ll.reverse()`                | Reverse the list links in place.                 | `ll.reverse()`          | Must handle empty and single-node lists safely.                                                                                            |
| `ll.clear()`                  | Remove all nodes.                                | `ll.clear()`            | Set `head = None`. Any external references to old nodes keep them alive.                                                                   |



