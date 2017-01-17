# -*- coding: utf-8 -*-

class Screen(object):
    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    @width.setter
    def width(self, width):
        self._width = width 

    @height.setter
    def height(self, height):
        self._height = height

    @property
    def resolution(self):
        return self.height * self.width

s = Screen()
s.width = 1024
s.height = 768
print (s.width)
print (s.height)
print (s.resolution)
s.resolution = 1
