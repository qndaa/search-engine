import re
from data_structures.set import Set


def check_input(user_input):
    word_list = re.split("\s+",user_input.lower())
    simbols = ["and", "or", "not"]
    fleg = 0
    lista = []

    if len(word_list) == 1:
        if len(word_list) in simbols:
            return "Unos nije validan",""
        else:
            return word_list,""
    else:
        for i in word_list:
            if i !="":
                lista.append(i)

        if len(lista) <3:
            for i in lista:
                if i in simbols:
                    return "Unos nije validan",""
                else:
                    fleg = fleg + 1
            if fleg == 2:
                return lista,""

        if len(lista) == 3:
            for i in lista:
                if i in simbols:
                    break
                else:
                    fleg = fleg + 1

            if fleg == 3:
                return lista,""

            if lista[1] not in simbols:
                return "Unos nije validan",""

            if lista[1] == "and":
                if lista[0] in simbols:
                    return "Unos nije validan",""
                elif lista[2] in simbols:
                    return "Unos nije validan",""
                return lista,"and"
            if lista[1] == "or":
                if lista[0] in simbols:
                    return "Unos nije validan",""
                elif lista[2] in simbols:
                    return "Unos nije validan",""
                return lista,"or"
            if lista[1] == "not":
                if lista[0] in simbols:
                    return "Unos nije validan",""
                elif lista[2] in simbols:
                    return "Unos nije validan",""
                return lista,"not"

        if len(lista) > 3:
            for i in lista:
                if i in simbols:
                    return "Unos nije validan",""
            return lista, ""


def search_input_words(user_input, trie):
    set1 = Set()
    set2 = Set()
    words,simbol = check_input(user_input.lower())
    ret = Set()

    if words == "Unos nije validan":
        return ret

    if simbol == "":
        for word in words:
            find = trie.find(word)
            if find is None:
                dic1 = {}
            else:
                dic1 = find.getOccurrences()
            set2.set_data(dic1)
            ret = set1.operator_or(set2)
    else:
        word1 = trie.find(words[0])
        word2 = trie.find(words[2])

        if word1 is None:
            dic1 = {}
        else:
            dic1 = word1.getOccurrences()

        if word2 is None:
            dic2 = {}
        else:
            dic2 = word2.getOccurrences()

        set1.set_data(dic1)
        set2.set_data(dic2)
        if simbol == "and":
            ret = set1.operator_and(set2)
        elif simbol == "or":
            ret = set1.operator_or(set2)
        elif simbol == "not":
            ret = set1.operator_not(set2)

    return ret


