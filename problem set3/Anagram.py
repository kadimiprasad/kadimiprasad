class anagram:
    def Checkanagram(self, word1, word2):
        if len(word1) == len(word2):
            if sorted(word1) == sorted(word2):
                return True
        return False
w1 = raw_input("Enter the word1:")
w2 = raw_input("Enter the Word2:")
Obj = anagram()
print Obj.Checkanagram(w1, w2)