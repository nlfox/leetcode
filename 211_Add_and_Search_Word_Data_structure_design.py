class WordDictionary(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.dics = []
        self.curId = 0
        self.wordList = []

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        if len(self.dics) < len(word):
            for i in xrange(len(word)-len(self.dics)):
                self.dics += [{".": []}]
        self.curId += 1
        self.wordList.append(word)
        for i, v in enumerate(list(word)):
            if not self.dics[i].has_key(v):
                self.dics[i][v] = [self.curId]
                self.dics[i]["."] += [self.curId]
            else:
                self.dics[i][v] += [self.curId]
                self.dics[i]["."] += [self.curId]

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could
        contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        if len(word) > len(self.dics):
            return False
        for i, v in enumerate(word):
            if i == 0:
                if not self.dics[i].has_key(v):
                    return False
                s = set(self.dics[i][v])
            if not self.dics[i].has_key(v):
                return False
            s = s & set(self.dics[i][v])
            if s == set([]):
                return False
            else:
                return True




# Your WordDictionary object will be instantiated and called as such:
# wordDictionary = WordDictionary()
# wordDictionary.addWord("word")
# wordDictionary.search("pattern")


wordDictionary = WordDictionary()
wordDictionary.addWord("word")
print wordDictionary.search("p..d")
