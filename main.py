from utils.table import Table
from utils.table import Seat
from utils.openspace import Openspace

no_of_tables = int(input("Enter number of tables"))
Capacity_for_table = int(input("Enter capacity for each table"))
names =['Adheeba','Anastasiia','Basma','Dhrisya','Ihor','Izabela'
        ,'Kelli','Kevin' , 'Levin','Maarten'
        ,'Majid','Minh'
        ,'Moustafa','Muntadher','Nicolaas','Petra'
        ,'Rasmita','Rik','Soha','Tom'
        ,'Urson','Veena'
        ,'Wouter','Yeliz']

    #,'test1','test2']
openSpace= Openspace(no_of_tables,Capacity_for_table)
all_Seated = openSpace.organize(names)
openSpace.display()
openSpace.store("")