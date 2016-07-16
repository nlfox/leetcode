class TrieNode(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.childs = {"#":False}


class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        node = self.root
        for i in list(word):
            if node.childs.has_key(i):
                node = node.childs[i]
            else:
                node.childs[i] = TrieNode()
                node = node.childs[i]
        node.childs["#"] = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node = self.root
        for i in list(word):
            if not node.childs.has_key(i):
                return False
            else:
                node = node.childs[i]
        if node.childs["#"]:
            return True
        else:
            return False

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie
        that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        node = self.root
        for i in list(prefix):
            if not node.childs.has_key(i):
                return False
            else:
                node = node.childs[i]
        return True


# Your Trie object will be instantiated and called as such:
trie = Trie()
trie.insert("somestring")
print trie.search("somestring")
print trie.startsWith("so")
