class TrieNode(object):
    def __init__(self):
        self.word = None
        self.nodes = {} #recnik cvorova (karakter(jedno slovo) je kljuc a vrednost je TrieNode(objekat cvora) )
        self.occurrences = {} #recnik pojavljivanja stranica i putanja (broj pojavljivanja je vrednost i putanja je kljuc)

    def __str__(self):
        return self.word

    def add_node(self,char):
        self.nodes[char] = TrieNode()

    def getOccurrences(self):
        return self.occurrences.copy()

    def get_word(self):
        ret = []
        for char,node in self.nodes.items():
            if node.word is not None:
                ret.append(node.word)
            ret += node.get_word()
        return ret