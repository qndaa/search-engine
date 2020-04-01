from data_structures.set import Set


class ExpressionTreeNode(object):

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class ExpressionTree(object):
    def __init__(self, list_expression):
        self.list_expression = list_expression
        self.stack = list()
        self.root = None

    def construct_tree(self, trie):
        for item in self.list_expression:

            if self.is_operation(item) == 0:
                search_result = trie.find(item)
                if search_result:
                    set = Set()
                    set.set_data(search_result.getOccurrences())
                    operand = ExpressionTreeNode(set)
                else:
                    operand = ExpressionTreeNode(Set())
                self.stack.append(operand)
            elif self.is_operation(item) == 1:
                op = ExpressionTreeNode(item)
                operand1 = self.stack.pop()
                op.left = operand1

                self.stack.append(op)

            elif self.is_operation(item) == 2:
                op = ExpressionTreeNode(item)
                operand1 = self.stack.pop()
                operand2 = self.stack.pop()

                op.left = operand2
                op.right = operand1
                self.stack.append(op)

        self.root = self.stack.pop()

    def is_operation(self, op):
        if op in ["&&", "||"]:
            return 2

        if op == "!":
            return 1
        return 0

    def evaluacija_expression_tree(self, graph, trie, pointer):


        if pointer.left:
            self.evaluacija_expression_tree(graph, trie, pointer.left)

        if pointer.right:
            self.evaluacija_expression_tree(graph, trie, pointer.right)

        if pointer.value == "&&":
            op1 = pointer.left.value
            op2 = pointer.right.value


            pointer.value = op1.operator_and(op2)
        elif pointer.value == "||":
            op1 = pointer.left.value
            op2 = pointer.right.value
            pointer.value = op1.operator_or(op2)
        elif pointer.value == "!":
            res = Set()
            vertex = graph.all_vertex()
            for link in vertex:
                res.insert_data(link, 0)

            # unary not
            op = pointer.left.value.data
            for item in op:
                if item in res.data.keys():
                    res.data.pop(item)

            pointer.value = res




