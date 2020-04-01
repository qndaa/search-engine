
class Graph(object):
    def __init__(self):
        self._outgoing = {}
        self._ingoing = {}

    def insert(self, src, dest):
        if src in self._outgoing:
            self._outgoing[src].append(dest)
        else:
            self._outgoing[src] = [dest]

        if dest in self._ingoing:
            self._ingoing[dest].append(src)
        else:
            self._ingoing[dest] = [src]

    def ingoing_links(self, html):
        return self._ingoing[html]

    def all_vertex(self):
        return self._outgoing.keys()