class Solution:
    def canPlaceFlowers(lst, n):
        count = 0
        triples = [(lst[i], lst[i+1], lst[i+2]) for i in range(0, len(lst)-2, 3)]

        print(triples)
        for i in triples:
            if i == (1, 0, 0) or i == (0, 0, 0):
                count += 1
        if count == n:
            print('True')
        else:
            print('False')
    
    canPlaceFlowers([1,0,0,0,0,1], 1)