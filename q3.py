class Solution(object):
    @staticmethod
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start,maxlen=0,0
        wordcount={}
        for i in range(len(s)):
            if s[i] in wordcount and wordcount[s[i]]>=start:
                start=wordcount[s[i]]+1
            wordcount[s[i]]=i
            maxlen=max(maxlen,i-start+1)
        return maxlen
L="abcabcbb"
print Solution.lengthOfLongestSubstring(L)