# TODO:
#  # - search histroy list

class Search:
    def __init__(self):
        self.search_list = []

    def view_history(self):
        return ", ".join(self.search_list)
    
    def add_history(self,search):
        self.search_list = self.search_list.extend(search)

    def remove_search(self,search):
        # this should ideally be triggered by something in weather or app file's
        if search not in self.search_list:
            return 'No history matches found'
        
        self.search_list = self.search_list.remove(search)
        self.view_history()
    
    def clear_history(self):
        self.search_list = self.search_list.clear()
        return 'Searches deleted'
