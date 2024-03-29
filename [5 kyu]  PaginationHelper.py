# https://www.codewars.com/kata/515bb423de843ea99400000a

class PaginationHelper:
    def __init__(self, collection, items_per_page): 
        self.collection = collection
        self.items_per_page = items_per_page

        
    def item_count(self):
        return len(self.collection)

    
    def page_count(self):
        return len(self.collection) // int(self.items_per_page) + 1

    
    def page_item_count(self,page_index):
        if page_index < 0 or (self.page_count() < page_index + 1):
            return -1
        elif page_index + 1 < self.page_count():
            return self.items_per_page
        elif page_index + 1 == self.page_count():
            return len(self.collection) - page_index* self.items_per_page

    
    def page_index(self,item_index):
        if item_index < 0 or item_index >= len(self.collection):
            return -1
        else:
            return item_index // self.items_per_page