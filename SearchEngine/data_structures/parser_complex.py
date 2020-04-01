

class ComplexParser(object):
    def __init__(self, query):
        self.query = query
        self.lparen = 0
        self.rparen = 0
        self.parse_result = list()   # lista rezultata posle parsera
        self.parse_query = list()   # lista rezultata nakon provjere i ubacivanja or
        self.check = True       # indikator za pravilan unos
        self.stack = list()
        self.operators = {"!": 3, "&&": 2, "||": 1}
        self.items = ["!", "&&", "||", "(", ")"]


    def parse_input(self):
        for i in range(len(self.query)):
            if "(" in self.query[i]:
                if len(self.query[i]) > 1:
                    self.parse_result.append("(")
                    self.parse_result.append(self.query[i][1:len(self.query[i])])
                    self.lparen += 1

            elif ")" in self.query[i]:
                if len(self.query[i]) > 1:
                    self.parse_result.append(self.query[i][0:len(self.query[i]) - 1])
                    self.parse_result.append(")")
                    self.rparen += 1
            else:
                self.parse_result.append(self.query[i])

        if self.check_paren():
            self.check = False

    def check_paren(self):
        return self.rparen != self.lparen

    def check_query(self):
        for i in range(len(self.parse_result)):
            element = self.parse_result[i]
            self.parse_query.append(element)
            if element in ["&&", "||"]:
                if i - 1 < 0 or i + 1 >= len(self.parse_result):
                    self.check = False
                    return
                if self.parse_result[i - 1] in ["(", "&&", "!", "||"] or self.parse_result[i + 1] in [")", "&&", "||"]:
                    self.check = False
                    return

            elif element not in ["(", "&&", "!", "||", ")"]:
                try:
                    if self.parse_result[i + 1] not in ["(", "&&", "!", "||", ")"]:
                        self.parse_query.insert(i + 1, "||")
                except IndexError:
                    continue

            elif element == "!":
                try:
                    if self.parse_result[i + 1] in ["&&", "!", "||", ")"]:
                        self.check = False
                        return
                except IndexError:
                    self.check = False
                    return

            elif element == "(":
                try:
                    if self.parse_result[i + 1] == ")":
                        self.check = False
                        return
                except IndexError:
                    self.check = False
                    return


    def postfix_notation(self):
        self.parse_result = list()

        for item in self.parse_query:
            if item not in ["!", "&&", "||", "(", ")"]:
                self.parse_result.append(item)

            if item in self.operators.keys():
                while len(self.stack) > 0 and self.stack[len(self.stack) - 1] != "(" and self.operators[self.stack[len(self.stack) - 1]] > self.operators[
                    item]:
                    operator = self.stack.pop()
                    self.parse_result.append(operator)

                self.stack.append(item)
            if item == "(":
                self.stack.append(item)
            if item == ")":
                while self.stack[len(self.stack) - 1] != "(":
                    operator = self.stack.pop()
                    self.parse_result.append(operator)
                self.stack.pop()

        while len(self.stack) > 0:
            operator = self.stack.pop()
            self.parse_result.append(operator)
