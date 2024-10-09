from typing import List
class Solution:
    def playOfGlasses(self, c1: int, w1: int, c2: int, w2: int, c3: int, w3: int) -> List[int]:
        for i in range(100000):
                # Pour from a to b
                temp = min(w1, c2 - w2)
                w1 -= temp
                w2 += temp
                if (w1==0 or w2==c2) and i>=1:
                      break
                # Pour from b to c
                temp = min(w2, c3 - w3)
                w2 -= temp
                w3 += temp
                if (w1==0 or w2==c2) and i>=1:
                      break
                # Pour from c to a
                temp = min(w3, c1 - w1)
                w3 -= temp
                w1 += temp
                if (w1==0 or w2==c2) and i>=1:
                      break
        return [w1, w2, w3]


for _ in range(int(input())):
        c1, w1, c2, w2, c3, w3 = map(int, input().split())
        obj = Solution()
        res = obj.playOfGlasses(c1, w1, c2, w2, c3, w3)
        print(" ".join(map(str, res)))