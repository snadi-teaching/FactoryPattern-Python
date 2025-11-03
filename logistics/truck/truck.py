class Truck:
    def __init__(self, license_plate: str, capacity_tons: float):
        self.license_plate = license_plate
        self.capacity_tons = capacity_tons

    def transport(self, cargo_weight: float, destination: str):
        if cargo_weight > self.capacity_tons:
            print(f"Error: Cargo exceeds truck capacity of {self.capacity_tons} tons.")
            return
        print(
            f"Truck {self.license_plate} transporting {cargo_weight} tons to {destination}."
        )
