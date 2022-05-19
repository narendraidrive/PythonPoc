class Phonebook():

    def __init__(self):
        self.entries = {}

    def add(self, name, number):
        self.entries[name] = number

    def lookup(self, name):
        return self.entries[name]

    def get_names(self):
        return self.entries.keys()

    def get_numbers(self):
        return self.entries.values()

    def get_entries(self):
        return(self.entries)

    def is_consistent(self):
        numbers = list(self.get_numbers())

        for i in range(len(numbers) - 1):
            for j in range(i + 1, len(numbers)):
                if numbers[j].startswith(numbers[i]) or\
                   numbers[i].startswith(numbers[j]):
                    return False
        return True 

    def clear(self):
        self.entries = {}