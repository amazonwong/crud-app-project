# CRUD APP PROJECT

menu = """
    Hi.

    Welcome to the products app.

    There are 100 products.

    Available operations: 'List', 'Show', 'Create', 'Update', 'Destroy'

    Please choose an operation:

"""

chosen_operation = input(menu)
chosen_operation = chosen_operation.title()

def list_product():
    print("LISTING PRODUCTS")

def show_product():
    print("SHOWING PRODUCTS")

def create_product():
    print("CREATING PRODUCTS")

def update_product():
    print("UPDATING PRODUCTS")

def destroy_product():
    print("DESTROYING PRODUCTS")



if chosen_operation == "List": list_product()
elif chosen_operation == "Show": show_product()
elif chosen_operation == "Create": create_product()
elif chosen_operation == "Update": update_product
elif chosen_operation == "Destroy": destroy_product
else: print("OOPS. PLEASE CHOOSE ONE OF THE RECOGNIZED OPERATIONS.")



#print("-------------------------------")
#print("PRODUCTS APPLICATION")
#print("-------------------------------")
#print("Welcome @amazonwong")


import csv

csv_file_path = "data/products.csv"

with open(csv_file_path, "r") as csv_file:
    reader = csv.DictReader(csv_file) # assuming your CSV has headers, otherwise... csv.reader(csv_file)
    #for row in reader:

    print("THERE ARE " + str(len(products)) + " PRODUCTS:")

products = sorted(products, key=operator.itemgetter('name'))

for product in products:
    price_usd = ' (${0:.2f})'.format(product["price"])
    print(" + " + product["name"] + price_usd)

    #writer = csv.DictWriter(csv_file, fieldnames=["id", "name", "aisle", "department", "price"])
    #writer.writeheader() # uses fieldnames set above
    #writer.writerow({"city": "New York", "name": "Yankees"})
    #writer.writerow({"city": "New York", "name": "Mets"})
    #writer.writerow({"city": "Boston", "name": "Red Sox"})
    #writer.writerow({"city": "New Haven", "name": "Ravens"})
