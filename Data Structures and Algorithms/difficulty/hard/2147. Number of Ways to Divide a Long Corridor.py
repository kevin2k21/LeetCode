class Solution:
    def numberOfWays(self, corridor: str) -> int:
        count = 0
        l = []
        c = 0
        for i in range(len(corridor)):
            if corridor[i] == 'S':
                count += 1
                l.append(i)
        
        if count % 2 == 1 or count == 0:
            return 0

        res = 1
        for i in range(1,count-1,2):
            res *= l[i+1]-l[i]


        return res%((10**9)+7)
