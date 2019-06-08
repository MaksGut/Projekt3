from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
#from kivy.properties import ObjectProperty
from kivy.garden.mapview import MapMarker
from math import sin, cos, sqrt, atan2, pi

class Okno(BoxLayout):  
    def draw_marker(self):
        self.list_of_points=[['paris.jpg', 48,2],
                             ['london.jpg', 51,0],
                             ['madrid.jpg', 40, -3],
                             ['moscow.jpg', 55,37],
                             ['rome.jpg', 42,13],
                             ['amsterdam.jpg', 52,5],
                             ['warsaw.jpg', 52,21],
                             ['berlin.jpg', 52,13],
                             ['prague.jpg', 50,14],
                             ['tokyo.jpg', 35,139]]
        try:
            self.my_map.remove_marker(self.marker)
        except:
            pass         
                             
        self.latitude = self.my_map.lat
        self.longitude = self.my_map.lon
        
        self.marker = MapMarker(lat=self.latitude, lon=self.longitude)
        self.my_map.add_marker(self.marker)
        
        self.search_lat.text = "{:10.5f}".format(self.latitude)
        self.search_long.text = "{:10.5f}".format(self.longitude)

        
    def check_points(self):        
        
        self.latitude = self.my_map.lat
        self.longitude = self.my_map.lon
        R=6381
        lat1=(self.latitude)*pi/180
        lon1=(self.longitude)*pi/180
        lat2=(self.list_of_points[self.i][1])*pi/180
        lon2=(self.list_of_points[self.i][2])*pi/180            
        
        dlon=lon1-lon2
        dlat=lat1-lat2
        
        a=sin(dlat/2)**2+cos(lat1)*cos(lat2)*sin(dlon/2)**2
        c=2*atan2(sqrt(a),sqrt(1-a))        

        odl=R*c
        
        self.odleglosc=odl
        self.odleglosc2.text = "{:10.5f}".format(self.odleglosc)
        self.i=self.i+1
        self.my_image.source=self.list_of_points[self.i][0]
        
    def sprawdzanko(self):
        self.latitude = self.my_map.lat
        self.longitude = self.my_map.lon
        R=6381
        lat1=(self.latitude)*pi/180
        lon1=(self.longitude)*pi/180
        lat2=(self.list_of_points[self.i][1])*pi/180
        lon2=(self.list_of_points[self.i][2])*pi/180            
        
        dlon=lon1-lon2
        dlat=lat1-lat2
        
        a=sin(dlat/2)**2+cos(lat1)*cos(lat2)*sin(dlon/2)**2
        c=2*atan2(sqrt(a),sqrt(1-a))        

        odl=R*c
        self.odleglosc=odl
        self.odleglosc2.text = "{:10.5f}".format(self.odleglosc)
    
    def Poczatek(self):
        self.i=0
        self.odleglosc=[]
        self.my_image.source=self.list_of_points[self.i][0]
        

    
class MapViewApp(App):  
    pass

MapViewApp().run()
