# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 15:16:17 2019

@author: M4K5
"""

class Okno(BoxLayout):  
    def draw_marker(self):
        self.list_of_points=[['paris.jpg', 48,2],
                             ['london.jpg', 51,0],
                             ['madrid.jpg', 40, -3],
                             ['moscow.jpg', 55,37],
                             ['rome.jpg', 42,13]]
        try:
            self.my_map.remove_marker(self.marker)
        except:
            pass         
                             
        self.latitude = self.my_map.lat
        self.longitude = self.my_map.lon
        
        self.marker = MapMarker(lat=self.latitude, lon=self.longitude)
        self.my_map.add_marker(self.marker)
        
        self.search_lat.text = {:8,4f}
        self.search_long.text = {:8,4f}.format(self.longitude)
