class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        batteries.sort()
        su=sum(batteries)
        while batteries[-1]>su//n:
            n-=1
            su-=batteries.pop()
        return su//n
        """
        Intuition
        The staright idea, is to use all baterial evenly.
        So we take advantage of all the energy wihout any left.
        In this case, we can run up to sum(A) / n minutes.
        This average value is an upper bounde of the final result.
        It's great to start with this enviromental intuition.

        Explanation
        However, there may be some betteries that has too much energy.
        They are in charge all the time,
        but still can't run out all they have,
        then their energy wastes.

        So we can compare the average value with the most powerful battery max(A).
        If max(A) is bigger, then we can use this battery to charge a computer all the time.
        Now we reduce the problem to the left bettery and n - 1 computers.

        We continue doing this process,
        until the most powerful bettery max(A) can not run average time sum(A) / n.
        Then the left betteries can help each other and be use evenly until the end.
        One key point of this problem, it's to find out, why betteries can be used "evenly" in this situation.

        One quick "prove" is that, the max(A) is smaller than the running time,
        so the maximum battery won't get wasted,
        the other smaller betteries won't even get easted."""