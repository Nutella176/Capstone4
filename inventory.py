from tabulate import tabulate


class Shoe:
    """
    Class that creates a shoe object and takes in the below instance attributes.
    """

    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    def get_cost(self):
        """
        Method that returns the cost of the shoe.
        """
        return self.cost

    def get_quantity(self):
        """
        Method that returns the stock quantities.
        """
        return self.quantity

    def __str__(self):
        """Method that returns a string representation of the Shoe class."""
        return f"Shoe(country={self.country}, code={self.code}, product={self.product}, cost={self.cost}, quantity={self.quantity})"


shoe_list = []


def read_shoes_data():
    """
    Function that opens and reads from inventory.txt, then create a shoes object with this data
    and appends it to the shoes list.
    """
    with open("inventory.txt", "r", encoding="utf-8") as inventory_file:
        next(inventory_file)  # skip first line
        for line in inventory_file:
            try:
                data = line.strip().split(",")
                country = data[0]
                code = data[1]
                product = data[2]
                cost = float(data[3])
                quantity = int(data[4])

                shoe = Shoe(country, code, product, cost, quantity)
                shoe_list.append(shoe)
            except Exception as e:
                print(f"Error reading line: {line}. {e}")


def capture_shoes():
    """
    Function that allows a user to capture data
    about a shoe and use this data to create a shoe object
    and append this object inside the shoe list.
    """
    country = input("Enter the country of the shoe: ").title()
    code = input("Enter the code of the shoe: ").upper()
    product = input("Enter the shoe name: ").title()
    cost = float(input("Enter the cost of the shoe: "))
    quantity = int(input("Enter the quantity of the shoe: "))

    shoe = Shoe(country, code, product, cost, quantity)
    shoe_list.append(shoe)
    print("Shoe successfully added.")


def view_all():
    """
    Function that iterates over the shoes list and
    prints the details of the shoes returned from the __str__
    function in a table format.
    """
    rows = []
    for shoe in shoe_list:
        rows.append([shoe.country, shoe.code, shoe.product, shoe.cost, shoe.quantity])

    table = tabulate(rows, headers=["Country", "Code", "Product", "Cost", "Quantity"])
    print(table)


def re_stock():
    """
    Function that finds the shoe object with the lowest quantity,
    asks the user if they want to add more stock to this and then updates it in inventory.txt.
    """
    min_qty = float("inf")
    min_qty_shoe = None
    for shoe in shoe_list:
        if shoe.get_quantity() < min_qty:
            min_qty = int(shoe.get_quantity())
            min_qty_shoe = shoe
    if min_qty_shoe:
        print(
            f"The shoe with the lowest quantity is {min_qty_shoe.product} with {min_qty_shoe.get_quantity()} units in stock."
        )
        response = input("Would you like to add stock for this shoe? (y/n) ")
        if response.lower() == "y":
            new_quantity = int(input("Enter the number of shoes to add to stock: "))
            min_qty_shoe.quantity += new_quantity
            with open("inventory.txt", "r+", encoding="utf-8") as inventory_file:
                contents = inventory_file.readlines()
                inventory_file.seek(0)
                inventory_file.truncate()
                inventory_file.write(contents[0])
                for line in contents[1:]:
                    if line.startswith(min_qty_shoe.country):
                        line_parts = line.strip().split(",")
                        line_parts[-1] = str(min_qty_shoe.quantity)
                        line = ",".join(line_parts) + "\n"
                    inventory_file.write(line)

            print(f"{new_quantity} {min_qty_shoe.product} added to stock.")
    else:
        print("There are no shoes in the inventory.")


def search_shoe():
    """
    Function that searches a shoe using the shoe code and prints it on the console.
    """
    code = input("Please enter the product code of the shoe you wish to search: ")
    shoe_found = False
    for shoe in shoe_list:
        if shoe.code == code:
            print(shoe)
            shoe_found = True
            break
    if not shoe_found:
        print(f"No shoe found with code {code}.")


def value_per_item():
    """
    Function that calculates the total value for each item and prints this information on the console.
    """
    print("Value per item:")
    for shoe in shoe_list:
        value = shoe.cost * shoe.quantity
        print(f"{shoe.product} ({shoe.code}): {value}")


def highest_qty():
    """
    Function that determines the product with the highest quantity and print this shoe as being for sale.
    """
    max_qty = 0
    max_qty_shoe = None
    for shoe in shoe_list:
        if shoe.get_quantity() > max_qty:
            max_qty = shoe.get_quantity()
            max_qty_shoe = shoe
    if max_qty_shoe:
        print(
            f"The shoe with the highest quantity is {max_qty_shoe.product} with {max_qty_shoe.quantity} units and it's on sale."
        )
    else:
        print("There are no shoes in the inventory.")


# Menu that executes each function above.
while True:
    read_shoes_data()
    choice = input(
        "\nPlease enter one of the following options:\n"
        "a = Add a shoe\n"
        "v = View all\n"
        "r = Restock the product with the lowest quantity\n"
        "s = Search products by code\n"
        "c = Calculate the total value of each stock item\n"
        "f = Find the product with the highest quantity\n"
    ).lower()

    if choice == "a":
        capture_shoes()

    elif choice == "v":
        view_all()

    elif choice == "r":
        re_stock()

    elif choice == "s":

        search_shoe()

    elif choice == "c":
        value_per_item()

    elif choice == "f":
        highest_qty()

    else:
        print("Incorrect input, try again.")
