import math

class SegmentTree:
    def __init__(self, size):
        self.n = size
        # min_val and max_val track the range of values in a node
        # This allows us to know if '0' exists in this range via Intermediate Value Theorem
        self.min_val = [0] * (4 * size)
        self.max_val = [0] * (4 * size)
        self.lazy = [0] * (4 * size)

    def _push(self, node):
        """Pushes lazy updates down to children."""
        if self.lazy[node] != 0:
            lz = self.lazy[node]
            
            # Apply to left child
            self.lazy[2 * node] += lz
            self.min_val[2 * node] += lz
            self.max_val[2 * node] += lz
            
            # Apply to right child
            self.lazy[2 * node + 1] += lz
            self.min_val[2 * node + 1] += lz
            self.max_val[2 * node + 1] += lz
            
            # Reset current node
            self.lazy[node] = 0

    def update(self, node, start, end, l, r, val):
        """Range Update: Adds 'val' to indices [l, r]."""
        if l > end or r < start:
            return
        
        if l <= start and end <= r:
            self.lazy[node] += val
            self.min_val[node] += val
            self.max_val[node] += val
            return

        self._push(node)
        mid = (start + end) // 2
        self.update(2 * node, start, mid, l, r, val)
        self.update(2 * node + 1, mid + 1, end, l, r, val)
        
        # Pull up values
        self.min_val[node] = min(self.min_val[2 * node], self.min_val[2 * node + 1])
        self.max_val[node] = max(self.max_val[2 * node], self.max_val[2 * node + 1])

    def find_first_zero(self, node, start, end):
        """Finds the smallest index with value 0. Returns -1 if none."""
        # Optimization: If 0 is not in the range [min, max], it doesn't exist here.
        # This relies on the property that values change by at most 1 between adjacent indices.
        if self.min_val[node] > 0 or self.max_val[node] < 0:
            return -1
        
        if start == end:
            return start if self.min_val[node] == 0 else -1
        
        self._push(node)
        mid = (start + end) // 2
        
        # Try left child first (we want the longest subarray, so smallest L)
        res = self.find_first_zero(2 * node, start, mid)
        if res != -1:
            return res
            
        return self.find_first_zero(2 * node + 1, mid + 1, end)

class Solution:
    def longestBalanced(self, nums: list[int]) -> int:
        n = len(nums)
        st = SegmentTree(n)
        last_pos = {}
        max_len = 0
        
        # We process the array element by element (Sweep Line)
        for r in range(n):
            val = nums[r]
            
            # Determine previous occurrence
            prev = last_pos.get(val, -1)
            
            # Identify direction: +1 for Even, -1 for Odd
            direction = 1 if val % 2 == 0 else -1
            
            # UPDATE: Only indices (L) strictly after 'prev' see this as a NEW distinct number
            # Range is [prev + 1, r]
            st.update(1, 0, n - 1, prev + 1, r, direction)
            
            # Update last position
            last_pos[val] = r
            
            # QUERY: Find the smallest L such that Balance(L...R) == 0
            l_index = st.find_first_zero(1, 0, n - 1)
            
            if l_index != -1:
                max_len = max(max_len, r - l_index + 1)
                
        return max_len