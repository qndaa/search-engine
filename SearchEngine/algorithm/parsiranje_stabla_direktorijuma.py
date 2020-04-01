import os


def parsiranje_stabla_direktorijuma(path, parser, graph,trie):
    for file in os.listdir(path):
        file = os.path.join(path, file)
        if os.path.isdir(file):
            parsiranje_stabla_direktorijuma(file, parser,graph,trie)
        elif os.path.isfile(file) and file.endswith(".html"):
            links, words = parser.parse(file)

            for link in links:
                graph.insert(file, link)

            for word in words:
                trie.insert(word.lower(), file)



