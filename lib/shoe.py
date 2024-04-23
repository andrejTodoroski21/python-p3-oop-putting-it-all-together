#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand:str, size:int):
        self.brand  = brand
        self._size = size

    def cobble(self):
        self.condition = "New"
        print("Your shoe is as good as new!")

    @property
    def size(self):
        return self._size


    @size.setter
    def size(self, value:int):
        if type(value) != int:
            print("size must be an integer")
        else:
            self.size = value


        