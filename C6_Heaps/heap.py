"""

Quick start:
    >>> from heap import MaxHeap
    >>> h = MaxHeap([3, 9, 2, 7])
    >>> h.push(10)
    >>> h.peek()
    10
    >>> h.pop()
    10
    >>> h.to_sorted_list()
    [9, 7, 3, 2]

Note on indexing: the pseudocode is 1-indexed (CLRS). Python lists
are 0-indexed, so LEFT/RIGHT/PARENT below are adjusted accordingly
(left = 2i+1, right = 2i+2). The logic of MAX-HEAPIFY is otherwise identical.
"""

from typing import Any, Iterable, Iterator, List, Optional


# --------------------------------------------------------------------------
# Index helpers
# --------------------------------------------------------------------------
def parent(i: int) -> int:
    return (i - 1) // 2


def left(i: int) -> int:
    return 2 * i + 1


def right(i: int) -> int:
    return 2 * i + 2


# --------------------------------------------------------------------------
# The heap data structure
# --------------------------------------------------------------------------
class MaxHeap:
    """Binary max-heap backed by a Python list.

    Attributes:
        data:      the underlying list
        heap_size: number of elements currently part of the heap
                   (can be smaller than len(data) during heap sort)
    """

    def __init__(self, items: Optional[Iterable[Any]] = None):
        self.data: List[Any] = list(items) if items is not None else []
        self.heap_size: int = len(self.data)
        if self.heap_size > 1:
            build_max_heap(self)

    # ---- core operations -------------------------------------------------
    def push(self, value: Any) -> None:
        """Insert a value. O(log n)."""
        self.data.append(value)
        self.heap_size += 1
        self._sift_up(self.heap_size - 1)

    insert = push  # alias

    def peek(self) -> Any:
        """Return the largest element without removing it. O(1)."""
        if self.heap_size == 0:
            raise IndexError("peek from an empty heap")
        return self.data[0]

    def pop(self) -> Any:
        """Remove and return the largest element. O(log n)."""
        if self.heap_size == 0:
            raise IndexError("pop from an empty heap")
        top = self.data[0]
        last = self.data.pop()
        self.heap_size -= 1
        if self.heap_size > 0:
            self.data[0] = last
            max_heapify(self, 0)
        return top

    extract_max = pop  # alias

    def pushpop(self, value: Any) -> Any:
        """Push value, then pop the max. Faster than push() + pop()."""
        if self.heap_size and self.data[0] > value:
            value, self.data[0] = self.data[0], value
            max_heapify(self, 0)
        return value

    def replace(self, value: Any) -> Any:
        """Pop the max, then push value. Faster than pop() + push()."""
        if self.heap_size == 0:
            raise IndexError("replace on an empty heap")
        top = self.data[0]
        self.data[0] = value
        max_heapify(self, 0)
        return top

    def increase_key(self, i: int, new_value: Any) -> None:
        """Increase the value at index i to new_value. O(log n)."""
        if not 0 <= i < self.heap_size:
            raise IndexError("index out of range")
        if new_value < self.data[i]:
            raise ValueError("new value is smaller than current value")
        self.data[i] = new_value
        self._sift_up(i)

    def remove(self, value: Any) -> None:
        """Remove the first occurrence of value. O(n)."""
        try:
            i = self.data.index(value, 0, self.heap_size)
        except ValueError:
            raise ValueError(f"{value!r} not in heap") from None
        last = self.data.pop()
        self.heap_size -= 1
        if i < self.heap_size:
            self.data[i] = last
            self._sift_up(i)
            max_heapify(self, i)

    def clear(self) -> None:
        self.data.clear()
        self.heap_size = 0

    # ---- conveniences ----------------------------------------------------
    def to_sorted_list(self) -> List[Any]:
        """Return all elements in descending order (heap is not modified)."""
        copy = MaxHeap.__new__(MaxHeap)
        copy.data = self.data[: self.heap_size]
        copy.heap_size = self.heap_size
        return [copy.pop() for _ in range(copy.heap_size)]

    def copy(self) -> "MaxHeap":
        new = MaxHeap.__new__(MaxHeap)
        new.data = self.data[: self.heap_size]
        new.heap_size = self.heap_size
        return new

    def is_valid(self) -> bool:
        """Check the max-heap property (useful for testing)."""
        for i in range(1, self.heap_size):
            if self.data[parent(i)] < self.data[i]:
                return False
        return True

    def __len__(self) -> int:
        return self.heap_size

    def __bool__(self) -> bool:
        return self.heap_size > 0

    def __contains__(self, value: Any) -> bool:
        return value in self.data[: self.heap_size]

    def __iter__(self) -> Iterator[Any]:
        """Iterate in internal (array) order - NOT sorted."""
        return iter(self.data[: self.heap_size])

    def __getitem__(self, i: int) -> Any:
        if not 0 <= i < self.heap_size:
            raise IndexError("index out of range")
        return self.data[i]

    def __repr__(self) -> str:
        return f"MaxHeap({self.data[: self.heap_size]})"

    # ---- internal --------------------------------------------------------
    def _sift_up(self, i: int) -> None:
        while i > 0 and self.data[parent(i)] < self.data[i]:
            p = parent(i)
            self.data[i], self.data[p] = self.data[p], self.data[i]
            i = p


# --------------------------------------------------------------------------
# MAX-HEAPIFY (from the pseudocode) - takes a heap as argument
# --------------------------------------------------------------------------
def max_heapify(A: MaxHeap, i: int) -> None:
    """Float A.data[i] down so the subtree rooted at i is a max-heap.

    Assumes the subtrees rooted at left(i) and right(i) are already max-heaps.
    """
    l = left(i)                                         # 1
    r = right(i)                                        # 2
    if l < A.heap_size and A.data[l] > A.data[i]:       # 3
        largest = l                                     # 4
    else:
        largest = i                                     # 5
    if r < A.heap_size and A.data[r] > A.data[largest]:  # 6
        largest = r                                     # 7
    if largest != i:                                    # 8
        A.data[i], A.data[largest] = A.data[largest], A.data[i]  # 9
        max_heapify(A, largest)                         # 10


def build_max_heap(A: MaxHeap) -> None:
    """Turn A.data into a max-heap in place. O(n)."""
    A.heap_size = len(A.data)
    for i in range(A.heap_size // 2 - 1, -1, -1):
        max_heapify(A, i)

# --------------------------------------------------------------------------
# Demo / self-test
# --------------------------------------------------------------------------
if __name__ == "__main__":
    import random

    h = MaxHeap([4, 1, 3, 2, 16, 9, 10, 14, 8, 7])
    print("Built heap:   ", h)
    print("Valid?        ", h.is_valid())
    h.push(20)
    print("After push 20:", h, "| peek =", h.peek())
    print("pop ->        ", h.pop())

    