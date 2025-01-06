
from typing import List

class Solution:
    def findContentChildren(g, s) -> int:
        g.sort()
        s.sort()
        cookie = 0
        greed = 0
        while cookie < len(s) and greed < len(g):
            if s[cookie] >= g[greed]:
                greed += 1
            cookie += 1
        return(greed) 
        
    findContentChildren([1,3,3], [1,2,3])