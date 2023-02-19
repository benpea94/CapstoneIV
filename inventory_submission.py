class Shoe:
    """
    class shoe with country, code, product, cost and quantity attributes
    """
    def __init__(self, country, code, product, cost, quantity):
        """
        initialise class with 5 different attributes
        :param country: country of origin for shoe
        :type country: string
        :param code: unique product code for shoe
        :type code: string
        :param product: name of shoe
        :type product: string
        :param cost: cost of shoe
        :type cost: float
        :param quantity: number of shoes in stock
        :type quantity: integer
        """
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    def get_cost(self):
        """
        method to get cost of shoe
        :return: cost attribute of shoe
        :rtype: float
        """
        return self.cost

    def get_quantity(self):
        """
        method to get quantity of stock
        :return: quantity attribute of stock
        :rtype: integer
        """
        return self.quantity

    def __str__(self):
        """
        create string containing all information of shoe object
        :return: string of shoe attributes
        :rtype: string
        """
        return f"{self.country}, {self.code}, {self.product}, {self.cost}, {self.quantity}"


"""
create empty shoe list
"""
shoe_list = []


def read_shoes_data(inv_list):
    """
    function to read shoe data from text file to empty list
    :param inv_list: empty list to store data from text file
    :type inv_list: list
    :return: list containing information from text file
    :rtype: list
    """
    try:
        with open("inventory.txt", "r") as file:
            next(file)
            for line in file:
                data = line.strip().split(",")
                shoe = Shoe(data[0], data[1], data[2], float(data[3]), int(data[4]))
                inv_list.append(shoe)
    except Exception as e:
        print("An error occurred:", e)
    return inv_list


def capture_shoes():
    """
    function to allow user to add new shoe to shoe list.  request all five attributes
    quantity should be an integer
    cost should be float
    """
    while True:
        try:
            country = input("Enter country of origin: ").capitalize()
            code = input("Enter product code: ").upper()
            product = input("Enter product name: ").capitalize()
            cost = float(input("Enter cost of pair of shoes: "))
            quantity = int(input("Enter quantity: "))
            print("\n")
            shoe = Shoe(country, code, product, cost, quantity)
            shoe_list.append(shoe)
            break
        except ValueError:
            print("\nPlease try again and make sure to only input a number for quantity and cost.\n")
            continue


def view_all():
    """
    function prints each item from shoe list as a string
    """
    for i in read_shoes_data(shoe_list):
        print(i.__str__())
    print('\n')


def re_stock():
    """
    find shoe with min quantity
    request user choice to restock
    if yes ask for new stock number and write the new quantity to file
    if no return to main menu
    error handle for incorrect inputs
    """
    min_shoe = min(shoe_list, key=lambda x: x.quantity)

    while True:
        choice = input(f"Would you like to re-stock '{min_shoe.code} {min_shoe.product}'? (Yes/No): ").lower()
        if choice == 'yes':
            try:
                add_quantity = int(input(f"\nCurrent quantity: {min_shoe.quantity}. Enter new quantity: "))
            except ValueError:
                print("\nError: Input must be a number.")
                continue
            print("\n")
            min_shoe.quantity = add_quantity
            with open("inventory.txt", "w") as f:
                f.write("country,code,product,cost,quantity\n")
                for shoe in shoe_list:
                    f.write(f"{shoe.country},{shoe.code},{shoe.product},{shoe.cost},{shoe.quantity}\n")
            break
        elif choice == 'no':
            break
        elif choice != 'yes' or 'no':
            print("\nPlease only choose either 'Yes' or 'No'")
        continue


def search_shoe():
    """
    request user input for shoe code
    if shoe code doesnt exist request again
    if shoe does exist print shoe information
    """
    while True:
        code = input("Enter product code to search: ")
        shoe_exists = False
        for shoe in shoe_list:
            if shoe.code == code:
                shoe_exists = True
                print(f"\n{shoe}\n")

        if not shoe_exists:
            print("\nShoe not found, double check your details and please search again!\n")
            continue
        break


def value_per_item():
    """
    function to find the total value of each stock item and then the total value of all stock
    value = 0
    For each shoe value equals shoe cost multiplied by shoe quantity
    add this value to total value
    print all information
    """
    total_value = 0
    for shoe in shoe_list:
        value = shoe.cost * shoe.quantity
        total_value += value
        print(f"Value for {shoe.product} {shoe.code}: R{value}")
    print(f"\nTotal value for all shoes: R{total_value}\n")


def highest_qty():
    """
    find max quantity shoe in list and print that shoe is on sale
    """
    max_shoe = max(shoe_list, key=lambda x: x.quantity)
    print(f"\n{max_shoe.product} is for sale!\n")


"""
menu to take user choice whether to view all shoes, add shoe to inventory, view highest stock, view lowest stock,
view value of stock or search for specific shoe
call read_shoes_data on shoe list to ensure list is full for further use
for each call specific function to each choice
add exit option to menu
handle invalid choices with error message
"""
while True:
    read_shoes_data(shoe_list)
    menu = input("Please select one of the following options\n"
                 "va - view all shoes\n"
                 "as - add shoe to inventory\n"
                 "vh - view shoe with highest stock\n"
                 "vl - view lowest stock item and re-stock\n"
                 "tv - view total value of each stock item and all stock\n"
                 "ss - search for specific stock item\n"
                 "ex - exit program\n"
                 ": "
                 )

    if menu == 'va':
        view_all()

    elif menu == 'as':
        capture_shoes()

    elif menu == 'vh':
        highest_qty()

    elif menu == 'vl':
        re_stock()

    elif menu == 'tv':
        value_per_item()

    elif menu == 'ss':
        search_shoe()

    elif menu == 'ex':
        print("\nGoodbye!")
        exit()

    else:
        print("\nPlease enter valid menu choice\n")

