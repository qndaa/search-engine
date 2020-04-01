from data_structures.trieNode import TrieNode
import os
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word, path):
        absolut_path = os.path.abspath(path)
        current = self.root
        lenght = len(word)

        for i in range(lenght):
            if word[i] not in current.nodes.keys():
                current.add_node(word[i])
            current = current.nodes[word[i]]

        current.word = word
        if absolut_path not in current.occurrences.keys():
            current.occurrences[absolut_path] = 1
        else:
            current.occurrences[absolut_path] += 1

    def get_word(self):
        return self.root.get_word()

    def getOccurrences(self):
        return self.root.getOccurrences()

    def find(self,word):
        nood = self.root
        for char in word:
            if char in nood.nodes.keys():
                nood = nood.nodes[char]
            else:
                return None
        return nood