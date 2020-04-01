from data_structures.set import Set


def rang(graph, result):
    ret = Set()

    for html in result.data.keys():

        incoming = graph.ingoing_links(html)
        number_links = len(incoming)
        number_words_in_links = 0
        for link in incoming:
            if link in result.data.keys():
                number_words_in_links += result.data[link]

        value = int(result.data[html] + number_links * 0.7 + number_words_in_links * 0.5)
        ret.insert_data(html, value)

    return ret
