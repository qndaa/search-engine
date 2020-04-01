import os

from algorithm.paginacija import paginacija
from algorithm.parsiranje_stabla_direktorijuma import parsiranje_stabla_direktorijuma
from algorithm.pretraga import search_input_words
from data_structures.expression_tree import  ExpressionTree
from data_structures.graph import Graph
from data_structures.parser import Parser
from data_structures.parser_complex import ComplexParser
from data_structures.trie import Trie


def menu():
    running = True

    os.chdir("test-skup")
    os.chdir("python-2.7.7-docs-html/whatsnew")
    path = os.path.abspath("")

    print("Ucitavanje podataka!\n")
    graph = Graph()
    trie = Trie()
    parsiranje_stabla_direktorijuma(path, Parser(), graph,trie)

    while running:
        user_input = user_input_function()

        if user_input == "1":
            new_path, index = change_path(path)
            if index == 1:
                path = new_path
                graph = Graph()
                trie = Trie()
                print("Ucitavanje podataka!\n")
                parsiranje_stabla_direktorijuma(path, Parser(), graph, trie)
        elif user_input == "2":
            i = input("Unesite pretragu :")
            i = i.strip()
            result_set = search_input_words(i, trie)
            paginacija(result_set, graph)

        elif user_input == "3":
            user_input = str(input("upit >> "))
            user_input.strip()
            split_input = user_input.split()
            parser = ComplexParser(split_input)
            parser.parse_input()
            parser.check_query()

            if parser.check and len(parser.parse_query):
                parser.postfix_notation()
                #print(parser.parse_result)
                expression_tree = ExpressionTree(parser.parse_result)

                expression_tree.construct_tree(trie)

                expression_tree.evaluacija_expression_tree(graph, trie, expression_tree.root)
                paginacija(expression_tree.root.value, graph)






            else:
                print("Nepravilan upit!")

        elif user_input == "0":
            print("\nUgodan dan!")
            print(":D")
            return
        else:
            print("\nUnesite broj iz menija!\n")


def user_input_function():
    print("1- Promeni direktorijum")
    print("2- Pretraga")
    print("3- Complex pretraga ")
    print("0- Kraj programa")

    try:
        user_input = input(">> ")
    except KeyboardInterrupt:
        return 0

    return user_input


def change_path(path):
    new_path = os.path.abspath(input("Unesite putanju direktorijuma: "))
    print("\n" + "--" * 20)
    if os.path.exists(new_path) and os.path.isdir(new_path):
        os.chdir(new_path)
        print("Uspesna promena direktorijuma!")
        print("Tekuci direktorijum: \n{}".format(new_path))
        print("--" * 20)

        return new_path, 1
    else:
        print("Pogresan unos!")
        print("Tekuci direktorijum: \n{}".format(path))
        print("--" * 20)
        return path, 0
