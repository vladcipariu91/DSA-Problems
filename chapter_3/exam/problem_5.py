"""
Building a Trie in Python

Before we start let us reiterate the key components of a Trie or Prefix Tree. A trie is a tree-like data structure that
stores a dynamic set of strings. Tries are commonly used to facilitate operations like predictive text or autocomplete
features on mobile phones or web search.

Before we move into the autocomplete function we need to create a working trie for storing strings. We will create two
classes:

    A Trie class that contains the root node (empty string)
    A TrieNode class that exposes the general functionality of the Trie, like inserting a word or finding the node which
     represents a prefix.

Finding Suffixes

Now that we have a functioning Trie, we need to add the ability to list suffixes to implement our autocomplete feature.
To do that, we need to implement a new function on the TrieNode object that will return all complete word suffixes that
exist below it in the trie. For example, if our Trie contains the words ["fun", "function", "factory"] and we ask for
suffixes from the f node, we would expect to receive ["un", "unction", "actory"] back from node.suffixes().

Using the code you wrote for the TrieNode above, try to add the suffixes function below. (Hint: recurse down the trie,
collecting suffixes as you go.)

"""


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

    def insert(self, char):
        if char not in self.children:
            self.children[char] = TrieNode()

    def suffixes(self, suffix=''):
        result = []
        if self.is_word and suffix != '':
            result.append(suffix)

        for char in self.children:
            child = self.children[char]

            result.extend(child.suffixes(suffix + char))

        return result


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current_node = self.root
        for char in word:
            current_node.insert(char)
            current_node = current_node.children[char]

        current_node.is_word = True

    def find(self, prefix):
        current_node = self.root
        for char in prefix:
            if char in current_node.children:
                current_node = current_node.children[char]
            else:
                return None

        return current_node


trie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym",
    "fun", "function", "factory", "functioz",
    "trie", "trigger", "trigonometry", "tripod"
]

for word in wordList:
    trie.insert(word)

node = trie.find("fun")
print(node.suffixes())

node = trie.find("tr")
print(node.suffixes())
