class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs: 
            encoded += s + "\t"
        return encoded 

    def decode(self, s: str) -> List[str]:
        result = []
        n = len(s)
        start = 0
        for i in range(n):
            if s[i] == "\t":
                result.append(s[start:i])
                start = i + 1
            
        return result