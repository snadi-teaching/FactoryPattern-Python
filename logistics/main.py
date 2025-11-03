from truck.truck import Truck


def main():
    print("=== Logistics Management System v1.0 ===")

    # Create a truck
    truck = Truck(license_plate="ABC-123", capacity_tons=10.0)

    # Transport some cargo
    truck.transport(cargo_weight=8.5, destination="New York")

    # Attempt to overload
    truck.transport(cargo_weight=12.0, destination="Boston")


if __name__ == "__main__":
    main()
