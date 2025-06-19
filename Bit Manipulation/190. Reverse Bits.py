class Solution:
    def reverseBits(self, n: int) -> int:
        return int(format(n, '032b')[::-1], 2)
    
    
class Solution:
    def reverseBits(self, n: int) -> int:
        binary_format = format(n, "032b")
        reversed_bin = binary_format[::-1]
        intiger = int(reversed_bin, 2)
        return intiger