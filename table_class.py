class Table:
    def __init__(self, table_number, capacity, availability=True) -> None:
        self.table_number = table_number
        self.capacity = capacity
        self.availability = availability

    def mark_as_occupied(self):
        self.availability = False

    def mark_as_available(self):
        self.availability = True




 
time_slots = ["12:00", "12:30", "13:00", "13:30", "14:00", "14:30", "15:00", "15:30", "16:00", "16:30", "17:00", "17:30", "18:00", "18:30", "19:00", "19:30", "20:00", "20:30", "21:00", "21:30", "22:00"]

tables = {"Nr1": 2, "Nr2": 2, "Nr3": 3, "Nr4": 3, "Nr5": 4, "Nr6": 5, "Nr7": 6, "Nr8": 8}

def check_availability(time, num_people):
    if time in time_slots:
        for table, capacity in tables.items():
            if capacity >= num_people:
                return table
    return None

def make_reservation():
    print("Welcome to the table reservation system!")
    num_people = int(input("Enter the number of people: "))
    # preferred_time = from time.py

  
    available_table = check_availability(preferred_time, num_people)
    if available_table:
        print(f"Table {available_table} is available for {num_people} people at {preferred_time}.")
        confirm = input("Confirm? (yes/no): ")
        if confirm.lower() == "yes":
            
            print("Reservation confirmed")
        else:
            print("Reservation not confirmed")
    else:
        print(f"There are no available tables for {num_people} people at {preferred_time}.")

make_reservation()


# for i, k in tables.items():
#     if k >= 3:
#         print(i, k)

 


     
