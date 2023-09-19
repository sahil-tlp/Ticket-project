
### TICKET PROJECT  ###

class Show:
    def __init__(self,show_id,show_time,duration):
        self.show_id=show_id
        self.show_time=show_time
        self.duration=duration

    
class Theater:
    def __init__(self,name,location,capacity):
        self.name=name
        self.location=location
        self.capacity=capacity
        self.avilable_seats=  [i for i in range(self.capacity)] 
        # self.lock = threading.Lock()
    
    
    def reserve_ticket(self,show_s,customer_s,seat_no): 

        if seat_no not in self.avilable_seats: 
            return False
       
        self.avilable_seats.remove(seat_no)
        ticket=Ticket(show_s,customer_s,seat_no)
        return ticket
    
    def check_seat_availability(self):
        return len(self.avilable_seats) 
    
class Customer:
    def __init__(self,name,email):
        self.name=name
        self.email=email
        # self.customer_id=customer_id
        # print("Name:",self.name,"|Email:",self.email)

class Ticket:
    def __init__(self,show,customer,seat_no):
        self.show=show 
        self.customer=customer 
        self.seat_no=seat_no

 
######## show inheritence
class Movies(Show):
    def __init__(self, show_id, show_time, duration,movie_name):
        super().__init__(show_id, show_time, duration)
        self.movie_name=movie_name
    # def movies_det(self):
    #     print(f"Movies details\nmovie id:{self.show_id}\nmovie timing:{self.show_time}\nmovie duration:{self.duration}\nmovie name:{self.movie_name}")


class Play(Show):
    def __init__(self, show_id, show_time, duration,play_name):
        super().__init__(show_id, show_time, duration)
        self.play_name=play_name
    # def play_det(self):
    #     print(f"Play details:-\nPlay id:{self.show_id}\nPlay timing:{self.show_time}\nPlay duration:{self.duration}\nPlay name:{self.play_name}")

class Concert(Show):
    def __init__(self, show_id, show_time, duration,concert_name):
        super().__init__(show_id, show_time, duration)
        self.concert_name=concert_name
    # def Concert_det(self):
    #     print(f"Concert details:-\nConcert id:{self.show_id}\nConcert timing:{self.show_time}\nConcert duration:{self.duration}\nConcert name:{self.concert_name}")



###### custumor inheritence
class RegularCustomer(Customer):
    def __init__(self, name, email,normal_discount):
        super().__init__(name, email)
        self.normal_discount=normal_discount
    # def regular_det(self):
    #     print(f"Regular Customer details:-\nName:{self.name}\nEmail:{self.email}\nNormal_discount:{self.normal_discount}\nRegular ID:{self.regular_id}")



class PremiumCustomer(Customer):
    def __init__(self, name, email,premium_discount):
        super().__init__(name, email)
        self.premium_discount=premium_discount
    # def premium_det(self):
    #     print(f"Regular Customer details:-\nName:{self.name}\nEmail:{self.email}\nPremium_discount:{self.premium_discount}\nRegular ID:{self.unique_id}")
        

show1 = Show("123as", "2023-07-10 10:00:00", "190mint")
customer1 = Customer("Sahil", "sahil123@gmail.com")
theater1 = Theater("PVR Theater", "New Delhi", 10)
seat_no = 1


ticket=theater1.reserve_ticket(show1,customer1,seat_no)

if ticket: 
    print("Ticket reserved successfully!")
    print(f"Show Time: {ticket.show.show_time}") 
    print(f"Customer: {ticket.customer.name}")
    print(f"Seat Number: {ticket.seat_no}")
else:
    print(f"Seat {seat_no} is already booked.")
    
print("no of seats avilable now:",theater1.check_seat_availability())
customer2 = Customer("Vijay", "sahil123@gmail.com")

seat_no = 7
ticket = theater1.reserve_ticket(show1, customer2, seat_no)


if ticket:
    print("Ticket reserved successfully!")
    print(f"Show Time: {ticket.show.show_time}")
    print(f"Customer: {ticket.customer.name}")
    print(f"Seat Number: {ticket.seat_no}")
else:
    print(f"Seat {seat_no} is already booked.")    
    
print(theater1.check_seat_availability())
print("no of seats avilable now:",theater1.check_seat_availability())
