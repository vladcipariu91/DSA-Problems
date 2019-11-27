# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self):
        self.root = RouteTrieNode()

    def insert(self, path, handler):
        current_node = self.root
        for part in path:
            current_node.insert(part)
            current_node = current_node.children[part]

        current_node.handler = handler

    def find(self, path):
        current_node = self.root
        for part in path:
            if part in current_node.children:
                current_node = current_node.children[part]
            else:
                return None

        return current_node


class RouteTrieNode:
    def __init__(self, handler=None):
        self.handler = handler
        self.children = {}

    def insert(self, part):
        if part not in self.children:
            self.children[part] = RouteTrieNode()


class Router:
    def __init__(self):
        self.trie = RouteTrie()

    def add_handler(self, path, handler):
        split_path = self.split_path(path)
        if len(split_path) == 0:
            self.trie.root.handler = handler
        else:
            self.trie.insert(split_path, handler)

    def lookup(self, path):
        split_path = self.split_path(path)
        if len(split_path) == 0:
            return self.trie.root.handler

        node = self.trie.find(split_path)
        if node:
            return node.handler
        else:
            return "404 Handler"

    def split_path(self, path):
        if path == "" or path == "/":
            return []
        if path[-1] == "/":
            return self.split_path(path[0:len(path) - 1])
        if path[0] == "/":
            return self.split_path(path[1:len(path)])

        return path.split("/")


router = Router()
router.add_handler("/", "Home Handler")
router.add_handler("/about", None)
router.add_handler("/about/me", "About me Handler")

print(router.lookup("/"))
# expected Home Handler
print(router.lookup(""))
# expected Home Handler
print(router.lookup("/about/me/now"))
# expected 404 Handler
print(router.lookup("/about/me/"))
# expected About me Handler
print(router.lookup("/about/me/"))
# expected About me Handler
print(router.lookup("/about/"))
# expected None

router.add_handler("/about/me/now", "Now handler")
print(router.lookup("about/me/now"))
# expected Now handler
print(router.lookup("sadasd"))
# expected 404 Handler

router.add_handler("/about/me", "This is not me Handler")
print(router.lookup("/about/me/"))
# expected This is not me Handler
