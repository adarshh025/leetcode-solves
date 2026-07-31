class Solution:
    def minimumPushes(self, word: str) -> int:
        counts = sorted(Counter(word).values(), reverse=True)
        return sum(freq * ((i // 8) + 1) for i, freq in enumerate(counts))