class Seat:
    """This is Seat which we allocate the pepole"""
    def __init__(self):
        self.free = True
        self.occupant = ""

    def set_occupant(self ,name): 
        """which allows the program to assign
          someone a seat if it's free"""
        if self.free :
            self.free= False
            self.occupant = name

    def remove_occupant(self): 
        """remove someone from a seat and return 
        the name of the person occupying the seat before"""
        self.free = True
        self.occupant=""

#seat_1 = Seat()
#seat_1.set_occupant("basma")



class Table:
    def __init__(self ,capacity:int, tableNo):
        self.tablename = "Table #"+ str(tableNo)
        self.capacity = capacity
        self.seats = []
        for i in range(capacity):
            self.seats.append( Seat())
        
    def has_free_spot(self):
        """returns a boolean
        checks if the table has free seats 
        then 
        Return yes
        Else No"""
        for seat in self.seats:
            if seat.free:
                return True
        return False
        
    
    def assign_seat(self,name):
        """that places someone at the table"""
        for seat in self.seats:
            if seat.free:
                seat.set_occupant(name)
                self.capacity -= 1
                return True
        return False
    
    def left_capacity(self):
         """that returns the ramining seats 
         available on that tablean integer
         """
         return self.capacity
         
"""new_table = Table()
new_table.assign_seat("Basma")"""