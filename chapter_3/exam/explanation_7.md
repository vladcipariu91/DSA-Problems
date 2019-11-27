## Explanation 
I assumed that when the router will be created there will be no paths added to it.
The RouteTrie functions: insert and find accept a list of strings, obtained from splitting the path string.

The Router's lookup function will return 404 Handler if there's no RouteTrieNode matching the given path.
The Router's insert function will check if the current path points to the root in which case it will set the root's
handler to the given handler otherwise it will perform an insert on the trie and replace or add the handler to an
existing node otherwise adding it to the newly inserted node. 