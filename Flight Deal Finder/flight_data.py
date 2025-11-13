class FlightData:
    def __init__(self, price="N/A", origin_airport="N/A", destination_airport="N/A", out_date="N/A"):
        self.price = price
        self.origin_airport = origin_airport
        self.destination_airport = destination_airport
        self.out_date = out_date

    def __repr__(self):
        return f"Price: £{self.price}, Origin Airport Code: {self.origin_airport}, Destination Airport Code: {self.destination_airport}, Out Date: {self.out_date}\n"

