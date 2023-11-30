class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert_node(self,patterns):
        node = self.root
        for symbol in patterns:
            if symbol not in node.children:
                node.children[symbol] = TrieNode()
            node = node.children[symbol]
        node.is_end_of_word = True

    def search(self, word):
        node = self.root
        for symbol in word:
            if symbol not in node.children:
                return False
            node = node.children[symbol]
        return node.is_end_of_word

    def find_prefix(self,prefix):
        node = self.root
        for symbol in prefix:
            if symbol not in node.children:
                return False
            node = node.children[symbol]
        return True


def build_trie(patterns):
    trie = Trie()
    for pattern in patterns:
        trie.insert_node(pattern)
    return trie

