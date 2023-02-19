# CapstoneIV
Shoe Inventory Application
The Shoe Inventory Application is a program designed to manage shoe inventory. The program allows the user to read, edit, and delete shoe inventory. The inventory is stored in a text file named inventory.txt.

Shoe Class
The Shoe class contains the following attributes:

Country of origin
Unique product code
Name of the shoe (product)
Cost of the shoe
Number of shoes in stock

The Shoe class contains the following methods:

get_cost(): This method returns the cost of the shoe.
get_quantity(): This method returns the number of shoes in stock.
__str__(): This method returns a string containing all the information of the Shoe object.
Shoe Inventory Management System Functions

The Shoe Inventory Application contains the following functions:

read_shoes_data()
This function reads the data from the inventory.txt file and stores it in a list. The list is returned by the function.

capture_shoes()
This function allows the user to add a new shoe to the inventory list. The user is prompted to enter the following information:

Country of origin
Unique product code
Name of the shoe
Cost of the shoe
Number of shoes in stock
If the user enters an incorrect value for the cost or quantity, they will be prompted to enter the value again.

view_all()
This function prints all the shoes in the inventory list.

re_stock()
This function finds the shoe with the minimum quantity in stock and prompts the user to restock it. The user is prompted to enter a new stock number, which is then written to the inventory.txt file.

search_shoe()
This function allows the user to search for a shoe in the inventory list using the product code. If the shoe is found, the information about the shoe is displayed. If the shoe is not found, the user is prompted to try again.

value_per_item()
This function calculates the value of each item in the inventory and the total value of all items in the inventory. The value of each item is calculated by multiplying the cost of the shoe by the number of shoes in stock. The total value is the sum of the value of each item.

How to use
Clone or download the repository.
Open the terminal and navigate to the directory where the repository is stored.
Run the following command to start the program: python shoe_inventory.py.
Follow the prompts in the program to read, add, search, or delete shoes in the inventory.
