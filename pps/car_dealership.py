class Car:
    def __init__(self, car_id, brand, model, year, price):
        self.car_id = car_id
        self.brand = brand
        self.model = model
        self.year = year
        self.price = price

    def __str__(self):
        return f"{self.car_id}: {self.brand} {self.model} ({self.year}) - ${self.price:,.2f}"


class Dealership:
    def __init__(self, name):
        self.name = name
        self.inventory = []

    def add_car(self, car):
        self.inventory.append(car)
        print(f"Car added: {car}")

    def remove_car(self, car_id):
        for car in self.inventory:
            if car.car_id == car_id:
                self.inventory.remove(car)
                print(f"Car sold: {car}")
                return
        print(f"Car ID {car_id} not found in inventory.")

    def display_inventory(self):
        if not self.inventory:
            print("No cars available in inventory.")
        else:
            print(f"Inventory of {self.name}:")
            for car in self.inventory:
                print(car)

    def process_sale(self, car_id, customer_name):
        for car in self.inventory:
            if car.car_id == car_id:
                print(f"Sale processed for {customer_name}: {car}")
                self.inventory.remove(car)
                return
        print(f"Car ID {car_id} not available for sale.")


# Example usage:
if __name__ == "__main__":
    # Create a dealership
    my_dealership = Dealership("SuperCars Dealership")

    # Add cars to inventory
    car1 = Car(101, "Toyota", "Camry", 2022, 25000)
    car2 = Car(102, "Honda", "Civic", 2023, 22000)
    car3 = Car(103, "Tesla", "Model 3", 2023, 45000)

    my_dealership.add_car(car1)
    my_dealership.add_car(car2)
    my_dealership.add_car(car3)

    # Display inventory
    my_dealership.display_inventory()

    # Process a sale
    my_dealership.process_sale(102, "John Doe")

    # Display inventory after sale
    my_dealership.display_inventory()

    # Try to remove a non-existent car
    my_dealership.remove_car(999)