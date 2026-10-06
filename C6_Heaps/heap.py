class Heap:
    """A general heap data structure container."""
    def __init__(self, max_capacity):
        # Index 0 is a placeholder to preserve clean 1-based indexing calculations
        self.A = [None] * (max_capacity + 1)
        self.max_capacity = max_capacity
        self.heap_size = 0

    def left(self, i):
        """Returns the 1-based index of the left child."""
        return 2 * i

    def right(self, i):
        """Returns the 1-based index of the right child."""
        return 2 * i + 1

    def parent(self, i):
        """Returns the 1-based index of the parent node."""
        return i // 2


# --- Standalone Max-Heapify Algorithm ---
def max_heapify(A, i):
    """
    Maintains the max-heap property.
    Takes a Heap instance 'A' and a 1-based index 'i' as arguments.
    """
    l = A.left(i)
    r = A.right(i)
    
    # 3-5: Is left child larger than the parent?
    if l <= A.heap_size and A.A[l] > A.A[i]:
        largest = l
    else:
        largest = i
        
    # 6-7: Is right child larger than the largest found so far?
    if r <= A.heap_size and A.A[r] > A.A[largest]:
        largest = r
        
    # 8-10: If structural violation exists, exchange elements and recurse
    if largest != i:
        # Explicit exchange step
        temp = A.A[i]
        A.A[i] = A.A[largest]
        A.A[largest] = temp
        
        # Recursive execution down the affected subtree
        max_heapify(A, largest)
