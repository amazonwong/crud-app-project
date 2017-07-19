# CRUD APP PROJECT

menu = "Hi. Welcome. Please choose an operation: 'List', 'Show', 'Create', 'Update', 'Destroy'..."

chosen_operation = input(menu)

print(chosen_operation)
#
# CAPTURE USER INPUTS
#

print("-------------------------------")
print("PRODUCTS APPLICATION")
print("-------------------------------")
print("Welcome @amazonwong")

file_name = "products.csv" # refers to a file path relative to the path from which you invoke your your script.

with open(file_name, "r") as file: # NOTE: "r" means "open the file for reading"
    contents = file.read()
    print(contents)

import csv

csv_file_path = "products.csv"

with open(csv_file_path, "r") as csv_file:
    reader = csv.DictReader(csv_file) # assuming your CSV has headers, otherwise... csv.reader(csv_file)
    for row in reader:
        print(row["id"], row["product"])

    #writer = csv.DictWriter(csv_file, fieldnames=["id", "name", "aisle", "department", "price"])
    #writer.writeheader() # uses fieldnames set above
    #writer.writerow({"city": "New York", "name": "Yankees"})
    #writer.writerow({"city": "New York", "name": "Mets"})
    #writer.writerow({"city": "Boston", "name": "Red Sox"})
    #writer.writerow({"city": "New Haven", "name": "Ravens"})
