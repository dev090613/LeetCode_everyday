# input: ["Hello","World"], output: ["Hello","World"]
class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        encoded_str = ''
        # ["Hello","World"] = > 5#Hello5#World
        for s in strs:
            size = len(s)
            encoded_str += str(size) + '#' + s
        return encoded_str
        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        # 5#Hello5#World => ["Hello","World"]
        decoded_str, i = [], 0
        
        while i<len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            decoded_str.append(s[j+1 : j+1+length])
            i = j + 1 + length
        return decoded_str
    
my_sol = Codec()
q = my_sol.encode(["C#","&","~Xp|F","R4QBf9g=_"])
# print(q) # 2#C# 1#& 5#~Xp|F 9#R4QBf9g=_ 
print(my_sol.decode(q))