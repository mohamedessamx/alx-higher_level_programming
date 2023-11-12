#!/usr/bin/python3
'''module for bas class'''


class Base:
    '''A representation of the best of our oop hierarchy.'''

    __nb_objects = 0

    def __init__(self, id=None):
        '''constructor.'''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

