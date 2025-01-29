class TrieNode:
    def __init__(self):
        self.child = [None] * 26
        self.word_end = False


def insert_key(root, key):
    curr = root

    for c in key:
        index = ord(c) - ord('a')
        if curr.child[index] is None:
            new_node = TrieNode()

            curr.child[index] = new_node
        # set pointer to the new node

        curr = curr.child[index]

    curr.word_end = True


def search_key(root, key):
    curr = root

    for c in key:
        index = ord(c) - ord('a')
        if curr.child[index] is None:
            return False
        curr = curr.child[index]
    return curr.word_end


root = TrieNode()

arr = ['me', 'ops', 'mil', 'me', 'sil', 'med']

for s in arr:
    insert_key(root, s)

search_keys = ['me', 'dog']

for s in search_keys:
    print("Key:" + s + " " + "is present") if search_key(root, s) else print("Key:" + s + " " "is absent")
