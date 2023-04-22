class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        # input: phragraph, ""
        # split(), lower(), re.sub(), not in banned, []
        # collections.counter(), most_common()
        # ouput: most frequent word, not banned ""
        
        my_word = [word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split() if word not in banned] # ' '가 아닌 ''로 받으면 space가 전부 붙어버린다.
        my_counter = collections.Counter(my_word)
        return my_counter.most_common(1)[0][0].lower() # tuple이므로 key, value를 쓸 수 없고 index로 접근
        