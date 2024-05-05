class Solution:
    # function to increment or decrement based on operation
    def options(self, s: str, x: int) -> int:
        if s == "--X":
            x -= 1
        elif s == "X--":
            x -= 1
        else:
            x += 1
        return x

    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x = 0 # init value of x
        for option in operations:
            x = self.options(option, x) # get new value of x after operation
        return x

    