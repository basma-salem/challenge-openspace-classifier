from utils.table import Table,Seat
import random
import pandas as pd
class Openspace:
    
    def __init__(self , number_of_tables :int,capacity:int):
        """creats objects of tables with there seats
        :Param self
        :Param number_of_tables :an int to Numbers of tables in our openspace
        :Param capacity: an int refers to capacity allowed to each table"""
        self.tables = []
        for i in range(number_of_tables):
            self.tables.append( Table(capacity, i+1))#create Objects = no_of_tables inserted with the capacity of every tables with tableNo.
        

    def organize(self,names:list):
        """randomly assign people to Seat 
        objects in the different Table objects.
        :Param self refers to the current object of class
        :Param names list of names to be assigned to seats"""
        random.shuffle(names) #random shuffle on names list
        name_index = 0  #indicator for current index of name  
        All_seated = True  #to endicate that all have a seat
        move_to_new_table =True
        for table in self.tables:
            while name_index < len(names): #loop if current index < length of names list
                if move_to_new_table == True: #if table 1st time in loop
                    table.assign_seat(names[name_index]+  ":Teamleader") #asign 1st seat as teamleader
                    move_to_new_table = False #now table not new in loop
                else:
                        if table.has_free_spot(): #searching for free seat
                            table.assign_seat(names[name_index]) #assign the seat with name
                name_index += 1 #increase name index after every loop to check 
                if table.left_capacity() ==0 : #check left capacity  in the table to move to new table
                    move_to_new_table = True
                    break
        if name_index < len(names): #check if the loop terminated at index < len(names)
            print("some people not seated") #then print some people not seated 
            All_seated = False #mark as false 
            for not_seated in range (name_index , len(names)): #display those names
                print (names[not_seated])
        return All_seated

        
    
    def display(self):
        """display the different tables
        and there occupants and remaining seats if found 
        :returns : print each table with its occupants 
                    and No. ofRemaining seats"""
        remaining_seats =0 #to calculate remaining seats
        for table in self.tables:
            occupants= []
            print(table.tablename + " has people: ")
            for seat in table.seats: #get names with related to assigned seats
                if seat.free == False:
                    #print(seat.occupant)
                    occupants.append(seat.occupant)
            print(*occupants, sep = ' ,') #display all ocuupants like list

            remaining_seats += table.left_capacity() #get remaining seats from eash table left capacity

        if remaining_seats > 0: #if ramaining sets >0 return them
            print("Remaining seats:"+str(remaining_seats))
        else:
             print("No Remaining Seats")    
        
    def store(self , filename):
        """store the repartition 
        in an excel file"""
        dict ={}
        for table in self.tables:
            occupants=[] #every time create list
            for seat in table.seats:
                if seat.free == False:
                    occupants.append(seat.occupant) #fill list with occupants for this table
                else :
                    occupants.append("Empty seat") #if no occupant mark as empty seat

            dict[table.tablename] = occupants # add table name as key and occupants as values

        df1 = pd.DataFrame(dict) # acctually i dont know well how the dataframe exactly working i googled to use it :D
        path = r"..\challenge-openspace-classifier\output.csv"
        df1.to_csv(path,sep ='\t')
        return True
    