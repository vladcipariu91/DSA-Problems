# The Trie data structure is part of the family of Tree data structures.
# It shines when dealing with sequence data, whether it's characters, words, or network nodes.
# When working on a problem with sequence data, ask yourself if a Trie is right for the job.


class TrieNode(object):
    def __init__(self):
        self.is_word = False
        self.children = {}


class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def add(self, word):
        current_node = self.root
        for c in word:
            if c not in current_node.children:
                current_node.children[c] = TrieNode()

            current_node = current_node.children[c]

        current_node.is_word = True

    # need a better name for this
    def exists(self, word):
        current_node = self.root

        for c in word:
            if c not in current_node.children:
                return False

            current_node = current_node.children[c]

        return current_node.is_word


valid_words = ['the', 'a', 'there', 'answer', 'any', 'by', 'bye', 'their']
word_trie = Trie()
for valid_word in valid_words:
    word_trie.add(valid_word)

# Tests
assert word_trie.exists('the')
assert word_trie.exists('any')
assert not word_trie.exists('these')
assert not word_trie.exists('zzz')
print('All tests passed!')
