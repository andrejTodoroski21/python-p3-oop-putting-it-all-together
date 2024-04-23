#!/usr/bin/env python3

class Book:
    def __init__(self, title:str, page_count:int):
        self.title = title
        self._page_count = page_count

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")

    @property
    def page_count(self):
        return self._page_count


    @page_count.setter
    def page_count(self, value:int):
        if type(value) != int:
            print("page_count must be an integer")
        else:
            self.page_count = value



    
        