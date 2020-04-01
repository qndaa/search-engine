

class Pages(object):
    def __init__(self, result_set, n):
        self.result_set = result_set
        self.n = n
        self.i = 0


    def show_page(self):
        while True:
            print("--" * 70)
            print("{:130}      {:4}".format("HTML page", "RANG"))

            for index in range(self.i * self.n, self.i * self.n + self.n):
                if index < len(self.result_set):
                    line = self.result_set[index]
                    print("{:130}      {:4}".format(str(line[0]), str(line[1])))

            print("--" * 70)
            print("Next (+)")
            print("Previous (-)")
            print("Change n (n)")
            print("Exit (anything else)")

            user_input = input(">> ")

            if user_input == "+":
                self.next()
            elif user_input == "-":
                self.prev()
            elif user_input == "n":
                self.change_n()
            else:
                return

    def next(self):
        print(len(self.result_set) // self.n)
        if self.i + 1 < len(self.result_set) // self.n:
            self.i += 1

    def prev(self):
        if self.i - 1 > -1 :
            self.i -= 1

    def change_n(self):
        try:
            new_n = int(input("Unesite broj HTML linkova po stranici prikaza: "))
        except ValueError:
            return

        self.n = new_n
        self.i = 0
