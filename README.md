# Capstone 4 Project

Code a Python program that will read from the text file inventory.txt and perform the following on the data, to prepare for presentation to your managers:
o We’ve provided a template for you in a file named inventory.py.
o Inside this file, you will find a class named Shoe with the following attributes:
● country,
● code,
● product,
● cost, and
● quantity.
o Inside this class define the following methods:
▪ get_cost - Returns the cost of the shoes.
▪ get_quantity - Returns the quantity of the shoes.
▪ __str__ - This method returns a string representation of a class.
o Outside this class create a variable with an empty list. This variable will be used to store a list of shoes objects
o Then you must define the following functions outside the class:
▪ read_shoes_data - This function will open the file inventory.txt and read the data from this file, then create a
 
shoes object with this data and append this object into the shoes list. One line in this file represents data to create one object of shoes. You must use the try-except in this function for error handling. Remember to skip the first line using your code.
▪ capture_shoes - This function will allow a user to capture data about a shoe and use this data to create a shoe object and append this object inside the shoe list.
▪ view_all - This function will iterate over the shoes list and print the details of the shoes returned from the __str__ function. Optional: you can organise your data in a table format by using Python’s tabulate module.
▪ re_stock - This function will find the shoe object with the lowest quantity, which are the shoes that need to be re-stocked. Ask the user if they want to add this quantity of shoes and then update it. This quantity should be updated on the file for this shoe.
▪ seach_shoe - This function will search for a shoe from the list using the shoe code and return this object so that it will be printed.
▪ value_per_item - This function will calculate the total value for each item . Please keep the formula for value in mind; value = cost * quantity. Print this information on the console for all the shoes.
▪ highest_qty - Write code to determine the product with the highest quantity and print this shoe as being for sale.
o Now in your main create a menu that executes each function above. This menu should be inside the while loop. 
