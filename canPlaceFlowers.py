class Solution:
    def canPlaceFlowers(flowerbed, n):
        count = 0
        length = len(flowerbed)
        
        for i in range(length):
            if flowerbed[i] == 0:
                
                prev_empty = (i == 0) or (flowerbed[i-1] == 0)
                next_empty = (i == length - 1) or (flowerbed[i+1] == 0)
                
                if prev_empty and next_empty:
                    # Plant a flower here
                    flowerbed[i] = 1
                    count += 1
                    if count == n:
                        return True
    
    canPlaceFlowers([1,0,0,0,0,1], 1)