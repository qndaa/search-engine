

class Set(object):
    def __init__(self):
        self.data = dict()

    def set_data(self, data):
        self.data = data

    def insert_data(self, key, value):
        self.data[key] = value

    def operator_and(self, set_data):
        result = Set()

        for html in self.data.keys():
            if html in set_data.data.keys():
                result.insert_data(html, self.data[html] + set_data.data[html])

        return result

    def operator_or(self, set_data):
        result = Set()
        for html in self.data.keys():
            result.insert_data(html, self.data[html])

        for html in set_data.data.keys():
            if html not in self.data.keys():
                result.insert_data(html, set_data.data[html])
            else:
                result.data[html] += set_data.data[html]

        return result

    def operator_not(self, set_data):
        result = Set()
        for html in self.data.keys():
            result.insert_data(html, self.data[html])

        for html in set_data.data.keys():
            if html in self.data.keys():
                del result.data[html]

        return result

    def getData(self):
        return self.data.copy()

    def get_list_data(self):
        return list(self.data.items())

    def __len__(self):
        return len(self.data)
