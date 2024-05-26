class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # haystack = "is great sai"
        # needle = "sai"
        index = haystack.find(needle)
        print(f"index : {index}")

        return index
