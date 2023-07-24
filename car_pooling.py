def car_pooling(trips: list[list[int]], capacity: int) -> bool:
    passengers_at_kilometer = {}
    for num_passengers, start_km, end_km in trips:
        for i in range(start_km, end_km):
            passengers_at_kilometer[i] = passengers_at_kilometer.get(i, 0) + num_passengers
            if passengers_at_kilometer[i] > capacity:
                return False
    return True


num_trips = int(input("Enter the number of trips : "))
trips: list = []
for i in range(num_trips):
    trip = []
    trip.append(int(input(f"Enter the number of passengers for the trip {i + 1} : ")))
    trip.append(int(input(f"Enter the starting kilometer for the trip {i + 1} : ")))
    trip.append(int(input(f"Enter the ending kilometer for the trip {i + 1} : ")))
    trips.append(trip)
capacity = int(input("Enter the capacity of the vehicle: "))
print(car_pooling(trips, capacity))
