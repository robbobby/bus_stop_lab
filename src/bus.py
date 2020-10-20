class Bus:
    def __init__(self, route_number, destination):
        self.route_number = route_number
        self.destination = destination
        self.passengers  = []

    def drive(self):
        return "Brum brum"

    def passenger_count(self):
        return len(self.passengers)

    def pick_up(self, passenger):
        self.passengers.append(passenger)

    def drop_off(self, passenger):
        self.passengers.remove(passenger)

    def drop_off_specific(self, passenger, bus_stop):
        if passenger.destination == bus_stop.name:
            self.passengers.remove(passenger)

    def empty(self):
        self.passengers = []

    def pick_up_from_stop(self, bus_stop):
        self.passengers += bus_stop.queue
        bus_stop.clear()

    def pick_up_from_stop_specific(self, person, bus_stop):
        for person in persons:
            if self.destination == person.destination:
                self.passengers.append(person)
                bus_stop.remove_from_queue(person)