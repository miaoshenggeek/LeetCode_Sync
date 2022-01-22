class Solution:
    def shortestSubarray(self, A: List[int], K: int) -> int:
        d = collections.deque([[0, 0]])
        res, cur = float('inf'), 0
        for i, a in enumerate(A):
            cur += a
            while d and cur - d[0][1] >= K:
                res = min(res, i + 1 - d.popleft()[0])
            while d and cur <= d[-1][1]:
                d.pop()
            d.append([i + 1, cur])
        return res if res < float('inf') else -1
    """
    Why keep the deque increase?
    If B[i] <= B[d.back()] and moreover we already know that i > d.back(),
    it means that compared with d.back(),
    B[i] can help us make the subarray length shorter and sum bigger. 
    So no need to keep d.back() in our deque."""
            