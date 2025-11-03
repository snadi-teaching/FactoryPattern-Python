class Ship:
    def __init__(self, name: str, capacity_tons: float):
        self.name = name
        self.capacity_tons = capacity_tons

    def ship(self, cargo_weight: float, destination: str):
        if cargo_weight > self.capacity_tons:
            print(f"Error: Cargo exceeds ship capacity of {self.capacity_tons} tons.")
            return
        print(f"Ship {self.name} transporting {cargo_weight} tons to {destination}.")
