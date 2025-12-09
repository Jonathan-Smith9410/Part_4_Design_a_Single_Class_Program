class ToDo():
    def __init__(self):
        self._todo_dict = {}
        self._index_counter = 1
    
    def add(self, item):
        if item == "":
            raise Exception("No task present to add.")
        self._todo_dict[self._index_counter] = item
        self._index_counter += 1
    
    def show_list(self):
        if len(self._todo_dict) == 0:
            raise Exception("No tasks present in list.")
        return self._todo_dict
    
    def complete_task(self, key):
        del self._todo_dict[key]