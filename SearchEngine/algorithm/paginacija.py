from algorithm import sort
from algorithm.rang import rang
from data_structures.pages import Pages


def paginacija(result_set, graph):
    if len(result_set) > 0:

        set_rang_result = rang(graph, result_set)
        print("Pretraga je rangirana!")

        list_result = set_rang_result.get_list_data()

        print("\nKoliko imate vremena za sort?")
        print("--" * 25)
        print("   {:40}    {:15}".format("Name sort", "Average time"))
        print("1- {:40}    {:15}".format("Merge sort", "\u03F4(n log(n))"))
        print("2- {:40}    {:15}".format("Heap sort", "\u03F4(n log(n))"))
        print("3- {:40}    {:15}".format("Insertion sort", "\u03F4(n^2)"))
        print("4- {:40}    {:15}".format("Bubble sort", "\u03F4(n^2)"))
        print("--" * 25)

        while True:
            try:
                user_input = int(input(">> "))
            except ValueError:
                print("Unesite broj iz menija, gospodine Indjicu!")
                continue
            except KeyboardInterrupt:
                return 0

            if user_input == 1:
                sort.merge_sort(list_result, 0, len(list_result) - 1)
            elif user_input == 2:
                sort.heap_sort(list_result)
            elif user_input == 4:
                sort.bubble_sort(list_result)
            elif user_input == 3:
                sort.insertion_sort(list_result)
            else:
                print("Broj iz menija!")
                continue
            break

        pages = Pages(list_result, 5)

        pages.show_page()


    else:
        print("\nPretraga je neuspesna!\n")


