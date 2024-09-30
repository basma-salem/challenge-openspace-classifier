class Seat:
    """This is Seat which we allocate the pepole
        seat empty at initation and 
        has no occupant"""
    def __init__(self):
        self.free = True 
        self.occupant = "" 

    def set_occupant(self ,name): 
        """which allows the program to assign
        someone a seat if it's free
        :Param self:
        :Param name: the name of occupant """
        if self.free :
            self.free= False # Set seat to not free
            self.occupant = name #set occupant name

    def remove_occupant(self): 
        """remove someone from a seat and return 
        the name of the person occupying the seat before"""
        self.free = True #set seat to be free
        self.occupant="" #remove name of occupant


class Table:
    def __init__(self ,capacity:int, tableNo:int):
        """table with how many seats it encompasses
        :Param self
        :param capacity : an int which refers to table capacity
        :param tableNo :an int refers to  table No"""
        self.tablename = "Table #"+ str(tableNo) #each table has name
        self.capacity = capacity # full capacity for the table
        self.available_seats = capacity
        self.seats = [] #define objects of seats according to capacity
        for i in range(capacity):
            self.seats.append( Seat())
        
    def has_free_spot(self):
        """returns a boolean
        checks if the table has free seats 
        then 
        Return yes
        Else No
        """
        for seat in self.seats:
            if seat.free:
                return True #returns true if empty seat found
        return False #returns false if no empty seat found
        
    
    def assign_seat(self,name)-> str:
        """that places someone on the seat of a table
        Param:self 
        Param: name :str refers to name of occupant
        return :True after seated"""
        for seat in self.seats: #searching for empty seat
            if seat.free: #if found
                seat.set_occupant(name)
                self.available_seats -= 1 # available places reduced by 1
                return True
    
    def left_capacity(self)->int:
         """The ramining seats 
         available on that table
          Return : int refers to currnt capacity of table"""
         return self.available_seats