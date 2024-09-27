from utils.table import Table
from utils.table import Seat
from utils.openspace import Openspace

names =['Adheeba','Anastasiia','Basma','Dhrisya',
'Ihor','Izabela','Kelli','Kevin',
'Levin','Maarten','Majid','Minh',
'Moustafa','Muntadher','Nicolaas','Petra',
'Rasmita','Rik','Soha','Tom',
'Urson','Veena','Wouter','Yeliz']
openSpace= Openspace(6)
openSpace.organize(names)
openSpace.display()