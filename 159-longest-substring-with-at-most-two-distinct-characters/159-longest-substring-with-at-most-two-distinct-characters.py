class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        res=0
        cur=Counter()  #counter
        l=0
        for r in range(len(s)):
            #if s[r] in cur:
            cur[s[r]]+=1
            
            while len(cur)>2 and l<r:
                cur[s[l]]-=1
                +cur
                if cur[s[l]]==0:del cur[s[l]]
                l+=1
            
            res=max(res,r-l+1)
        return res
                
                