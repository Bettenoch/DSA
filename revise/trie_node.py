# A trie node is a tree structure to store a sequence of strings. It has nodes with edges.

class TrieNode:
    def __init__(self):
        self.child = [None] * 27
        self.word_end = None


def insert_key(root, key):
    current = root

    for c in key:
        index = ord(c) - ord('a')

        if current.child[index] is not None:
            new_node = TrieNode()

            current.child[index] = new_node

        current = current.child[index]
    current.word_end = True
