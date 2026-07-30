class Solution:
    def mapWordWeights(self, words: list[str], weights: list[int]) -> str:
        return "".join(chr(122 - (sum(weights[ord(c) - 97] for c in w) % 26)) for w in words)