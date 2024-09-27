from utils.table import Table,Seat
import random
class Openspace:
    def __init__(self , number_of_tables :int):
        self.tables = []
        for i in range(number_of_tables):
            self.tables.append( Table(4, i+1))#crate Objects = no_of_tables inserted with the capacity of every tables 
        #To Random the tables here
        

    def organize(self,names):
        """randomly assign people to Seat 
        objects in the different 
        Table objects."""
        last_name_index =0
        random.shuffle(names)
        for table in self.tables:
            while  table.has_free_spot():
                    for name_index in range (last_name_index,len(names)):#chec
                        table.assign_seat(names[name_index])
                        last_name_index += 1#to mark last one had seated 
                        if table.left_capacity() ==0:
                            name_index +=1
                            break
                        

                    
        if last_name_index < len(names):
            print("some poeple not seated")

        
    
    def display(self):
        
        """display the different tables
        and there occupants in a
        nice and readable """
        """for tableNo in range(len(self.tables)):
            table = self.tables[tableNo]"""
        for table in self.tables:
            print(table.tablename + " Poeple: ")
            
            for seat in table.seats:
                if seat.free == False:
                    print(seat.occupant)

        remaining_seats = 0
        for table in self.tables:
            while  table.has_free_spot():
                remaining_seats += table.left_capacity()

        if remaining_seats > 0:
            print("Remaining seats:"+str(remaining_seats))
        else:
             print("No Remaining Seats")
        return True
              
    
    def store(self , filename):
        """store the repartition 
        in an excel file"""
        return True
    
