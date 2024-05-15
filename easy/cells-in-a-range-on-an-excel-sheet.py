class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        split = s.split(":")
        first = split[0]
        last = split[1]
        result = []
        for i in range(ord(first[0]), ord(last[0]) + 1):
            for j in range(int(first[1]) , int(last[1]) + 1 ):
                result.append(chr(i) + str(j))
        return result