# ------------------------------------------------------------
# Name: Seth Sorrell
# Date: March 31, 2025
# Purpose: This app collects and displays car information including
#          year, make, model, number of doors, and roof type,
#          using Vehicle and Automobile classes.
# ------------------------------------------------------------

# Define the Vehicle superclass
class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type

# Define the Automobile class that inherits from Vehicle
class Automobile(Vehicle):
    def __init__(self, vehicle_type, year, make, model, doors, roof):
        super().__init__(vehicle_type)  # Call the parent class constructor
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

    # Method to display the automobile details
    def display_info(self):
        print(f"Vehicle type: {self.vehicle_type}")
        print(f"Year: {self.year}")
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Number of doors: {self.doors}")
        print(f"Type of roof: {self.roof}")

# Main program
def main():
    # Get user input
    print("Please enter your car's details:")
    
    # Vehicle type is fixed as "car"
    vehicle_type = "car"
    
    # Get automobile details from user
    year = input("Enter the year: ")
    make = input("Enter the make: ")
    model = input("Enter the model: ")
    
    # Validate doors input
    while True:
        doors = input("Enter number of doors (2 or 4): ")
        if doors in ["2", "4"]:
            break
        print("Please enter either 2 or 4")
    
    # Validate roof input
    while True:
        roof = input("Enter type of roof (solid or sun roof): ").lower()
        if roof in ["solid", "sun roof"]:
            break
        print("Please enter either 'solid' or 'sun roof'")
    
    # Create an Automobile object with user input
    my_car = Automobile(vehicle_type, year, make, model, doors, roof)
    
    # Display the information
    print("\nHere are your car's details:")
    my_car.display_info()

# Run the program
if __name__ == "__main__":
    main()